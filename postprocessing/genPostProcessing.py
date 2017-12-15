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
from TopEFT.Tools.user                   import skim_output_directory
from TopEFT.Tools.GenSearch              import GenSearch
from TopEFT.Tools.helpers                import deltaR2, cosThetaStar

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='DEBUG',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--small',              action='store_true', help='Run only on a small subset of the data?')#, default = True)
argParser.add_argument('--targetDir',          action='store',      default='v1')
argParser.add_argument('--sample',             action='store',      default='fwlite_ttZ_ll_LO_sm')
args = argParser.parse_args()

#
# Logger
#
import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

sample_file = "$CMSSW_BASE/python/TopEFT/samples/fwlite_benchmarks.py"
samples = imp.load_source( "samples", os.path.expandvars( sample_file ) )
sample = getattr( samples, args.sample )

maxN = -1
if args.small: 
    args.targetDir += "_small"
    maxN = 500
    sample.files=sample.files[:2]

output_directory = os.path.join(skim_output_directory, 'gen', args.targetDir, sample.name) 
output_filename =  os.path.join(output_directory, sample.name + '.root') 
if not os.path.exists( output_directory ): 
    os.makedirs( output_directory )
    logger.info( "Created output directory %s", output_directory )

products = {
    'gp':{'type':'vector<reco::GenParticle>', 'label':("genParticles")},
    'genJets':{'type':'vector<reco::GenJet>', 'label':("ak4GenJets")},
    'genMET':{'type':'vector<reco::GenMET>',  'label':("genMetTrue")},
}

reader = sample.fwliteReader( products = products )

def varnames( vec_vars ):
    return [v.split('/')[0] for v in vec_vars.split(',')]

# standard variables
variables  = ["run/I", "lumi/I", "evt/l"]
# MET
variables += ["GenMet_pt/F", "GenMet_phi/F"]
# jet vector
jet_read_vars       =  "pt/F,eta/F,phi/F"
jet_read_varnames   =  varnames( jet_read_vars )
jet_write_vars      = jet_read_vars+',matchBParton/I' 
jet_write_varnames  =  varnames( jet_write_vars )
variables     += ["GenJet[%s]"%jet_write_vars]
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
Z_read_varnames= [ 'pt', 'phi', 'eta', 'mass']
variables     += ["Z_pt/F", "Z_phi/F", "Z_eta/F", "Z_mass/F", "Z_cosThetaStar/F", "Z_daughterPdg/I"]

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

    tops.sort( key = lambda p:-p['pt'] )
    fill_vector( event, "top", top_varnames, tops ) 

    gen_Zs = filter( lambda p:abs(p.pdgId())==23 and search.isLast(p), gp)
    gen_Zs.sort( key = lambda p: -p.pt() )
    if len(gen_Zs)>0: 
        gen_Z = gen_Zs[0]
        for var in Z_read_varnames:
           setattr( event, "Z_"+var,  getattr(gen_Z, var)() )
    else:
        gen_Z = None
    
    if gen_Z is not None:

        d1, d2 = gen_Z.daughter(0), gen_Z.daughter(1)
        if d1.pdgId()>0: 
            lm, lp = d1, d2
        else:
            lm, lp = d2, d1
        event.Z_daughterPdg = lm.pdgId()
        event.Z_cosThetaStar = cosThetaStar(gen_Z.mass(), gen_Z.pt(), gen_Z.eta(), gen_Z.phi(), lm.pt(), lm.eta(), lm.phi())

    # find all leptons 
    leptons = [ (search.ascend(l), l) for l in filter( lambda p:abs(p.pdgId()) in [11, 13] and search.isLast(p) and p.pt()>10,  gp) ]
    leps    = []
    for first, last in leptons:
        mother_pdgId = first.mother(0).pdgId() if first.numberOfMothers()>0 else -1
        leps.append( {var: getattr(last, var)() for var in lep_varnames} )
        leps[-1]['motherPdgId'] = mother_pdgId

    leps.sort( key = lambda p:-p['pt'] )
    fill_vector( event, "GenLep", lep_all_varnames, leps)

    # MET
    event.GenMet_pt = reader.products['genMET'][0].pt()
    event.GenMet_phi = reader.products['genMET'][0].phi()

    # jets
    jets = map( lambda t:{var: getattr(t, var)() for var in jet_read_varnames}, filter( lambda j:j.pt()>30, reader.products['genJets']) )

    # jet/lepton disambiguation
    jets = filter( lambda j: (min([999]+[deltaR2(j, l) for l in leps]) > 0.3**2 ), jets )

    # find b's from tops:
    b_partons = [ b for b in filter( lambda p:abs(p.pdgId())==5 and p.numberOfMothers()==1 and abs(p.mother(0).pdgId())==6,  gp) ]

    for jet in jets:
        jet['matchBParton'] = ( min([999]+[deltaR2(jet, {'eta':b.eta(), 'phi':b.phi()}) for b in b_partons]) < 0.2**2 )

    jets.sort( key = lambda p:-p['pt'] )
    fill_vector( event, "GenJet", jet_write_varnames, jets)

tmp_dir     = ROOT.gDirectory
output_file = ROOT.TFile( output_filename, 'recreate')
output_file.cd()
#tree        = ROOT.TTree( "Events", "Events")
maker = TreeMaker(
    sequence  = [ filler ],
    variables = [ TreeVariable.fromString(x) for x in variables ],
    treeName = "Events"
    )

tmp_dir.cd()
#maker = maker_parent.cloneWithoutCompile( externalTree = tree )

counter = 0
reader.start()
maker.start()

while reader.run( ):
    #if abs(map( lambda p: p.daughter(0).pdgId(), filter( lambda p: p.pdgId()==23 and p.numberOfDaughters()==2, reader.products['gp']))[0])==13: 
    #    maker.run()
    #    break
    maker.run()

    counter += 1
    if counter == maxN:  break

logger.info( "Done with running over %i events.", reader.nEvents )

output_file.cd()
maker.tree.Write()
output_file.Close()

logger.info( "Written output file %s", output_filename )
