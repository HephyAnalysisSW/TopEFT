#!/usr/bin/env python
''' Analysis script for gen plots
'''
#
# Standard imports and batch mode
#
import ROOT, os
ROOT.gROOT.SetBatch(True)
import itertools
from math                                import sqrt, cos, sin, pi, acos
import imp

#RootTools
from RootTools.core.standard             import *

#TopEFT
from TopEFT.tools.user                   import skim_directory
from TopEFT.tools.GenSearch              import GenSearch
from TopEFT.tools.helpers                import deltaR2

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--small',              action='store_true', help='Run only on a small subset of the data?')#, default = True)
argParser.add_argument('--targetDir',          action='store',      default='v1')
argParser.add_argument('--sample',             action='store',      default='fwlite_ttZ_LO_C2VA_0p2')
args = argParser.parse_args()

#
# Logger
#
import TopEFT.tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small: 
    args.targetDir += "_small"
    maxN = 100

sample_file = "$CMSSW_BASE/python/TopEFT/samples/benchmarks.py"
samples = imp.load_source( "samples", os.path.expandvars( sample_file ) )
sample = getattr( samples, args.sample )

output_directory = os.path.join(skim_directory, args.targetDir, sample.name) 
output_filename =  os.path.join(output_directory, sample.name + '.root') 

if not os.path.exists( output_directory ): 
    os.makedirs( output_directory )
    logger.info( "Created output directory %s", output_directory )

tmp_directory = ROOT.gDirectory
outputfile = ROOT.TFile.Open(output_filename, 'recreate')
tmp_directory.cd()

products = {
    'gp':{'type':'vector<reco::GenParticle>', 'label':("genParticles")},
    'genJets':{'type':'vector<reco::GenJet>', 'label':("ak4GenJets")},
    'genMET':{'type':'vector<reco::GenMET>', 'label':("genMetTrue")},
}

reader = sample.fwliteReader( products = products )

def varnames( vec_vars ):
    return [v.split('/')[0] for v in vec_vars.split(',')]

# dtandard variables
variables  = ["run/I", "lumi/I", "evt/l"]
# MET
variables += ["GenMet_pt/F", "GenMet_phi/F"]
# jet vector
jet_vars       =  "pt/F,eta/F,phi/F"
jet_varnames   =  varnames( jet_vars ) 
variables     += ["GenJet[%s]"%jet_vars]
# lepton vector 
lep_vars       =  "pt/F,eta/F,phi/F,pdgId/I"
lep_extra_vars =  "motherPdgId/I"
lep_varnames   =  varnames( lep_vars ) 
lep_all_varnames = lep_varnames + varnames(lep_extra_vars)
variables     += ["GenLep[%s]"%(','.join([lep_vars, lep_extra_vars]))]
# top vector
top_vars       =  "pt/F,eta/F,phi/F"
top_varnames   =  varnames( top_vars ) 
variables     += ["top[%s]"%top_vars]
# Z vector
Z_vars         =  "pt/F,eta/F,phi/F"
Z_varnames     =  varnames( Z_vars ) 
variables     += ["Z[%s]"%Z_vars]

def fill_vector( event, collection_name, collection_varnames, objects):
    setattr( event, "n"+collection_name, len(objects) )
    for i_obj, obj in enumerate(objects):
        for var in collection_varnames:
            getattr(event, collection_name+"_"+var)[i_obj] = obj[var]

def filler( event ):

    event.evt, event.lumi, event.run = reader.evt

    if reader.position % 100==0: logger.info("At event %i/%i", reader.position, reader.nEvents)

    # All gen particles
    gp      = reader.products['gp']

    # for searching
    search  = GenSearch( gp )

    # find heavy objects before they decay
    tops = map( lambda t:{var: getattr(t, var)() for var in top_varnames}, filter( lambda p:abs(p.pdgId())==6 and search.isLast(p),  gp) )
    fill_vector( event, "top", top_varnames, tops ) 
    Zs   = map( lambda Z:{var: getattr(Z, var)() for var in Z_varnames},   filter( lambda p:abs(p.pdgId())==23 and search.isLast(p), gp) )
    fill_vector( event, "Z", Z_varnames, Zs ) 
    #Ws   = filter( lambda p:abs(p.pdgId())==24 and search.isLast(p), gp)

    # find all leptons 
    leptons = [ (search.ascend(l), l) for l in filter( lambda p:abs(p.pdgId()) in [11, 13] and search.isLast(p) and p.pt()>25,  gp) ]
    leps    = []
    for first, last in leptons:
        mother_pdgId = first.mother(0).pdgId() if first.numberOfMothers()>0 else -1
        leps.append( {var: getattr(last, var)() for var in lep_varnames} )
        leps[-1]['motherPdgId'] = mother_pdgId
    fill_vector( event, "GenLep", lep_all_varnames, leps)

    # MET
    event.GenMet_pt = reader.products['genMET'][0].pt()
    event.GenMet_phi = reader.products['genMET'][0].phi()

    # jets
    jets = map( lambda t:{var: getattr(t, var)() for var in jet_varnames}, filter( lambda j:j.pt()>30, reader.products['genJets']) )

    # jet/lepton disambiguation
    jets = filter( lambda j: (min([999]+[deltaR2(j, l) for l in leps]) > 0.3**2 ), jets )

    fill_vector( event, "GenJet", jet_varnames, jets)

maker = TreeMaker(
    sequence  = [ filler ],
    variables = [ TreeVariable.fromString(x) for x in variables ],
    treeName = "Events"
    )

counter = 0
reader.start()
maker.start()

while reader.run( ):
    maker.run()

    counter += 1
    if counter == maxN:  break

logger.info( "Done with running over %i events.", reader.nEvents )

outputfile.cd()
maker.tree.Write()
outputfile.Close()

logger.info( "Written output file %s", output_filename )
