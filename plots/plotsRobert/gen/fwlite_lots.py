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

#RootTools
from RootTools.core.standard             import *

#TopEFT
from TopEFT.Tools.user                   import plot_directory
from TopEFT.Tools.GenSearch              import GenSearch
#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--small',                                   action='store_true',     help='Run only on a small subset of the data?', )
argParser.add_argument('--plot_directory',     action='store',      default='analysisPlots_v30_03Feb')
args = argParser.parse_args()

#
# Logger
#
import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:                        args.plot_directory += "_small"

maxN = -1

# Samples
from TopEFT.samples.fwlite_benchmarks import *

samples = [fwlite_ttZ_sm, fwlite_ttZ_bm1, fwlite_ttZ_bm2]
fwlite_ttZ_sm.color = ROOT.kBlack
fwlite_ttZ_bm1.color= ROOT.kRed
fwlite_ttZ_bm2.color=ROOT.kBlue

products = {
    'gp':{'type':'vector<reco::GenParticle>', 'label':("genParticles")}
#    'genJets':{'type':'vector<reco::GenJet>', 'label':("ak4GenJets")},
#    'genMET':{'type':'vector<reco::GenMET>', 'label':("genMetTrue")},
}

plots = []

top_pt      = {sample.name:ROOT.TH1D('top_pt', 'top_pt', 25, 0, 500) for sample in samples}
top_pt['texX'] = "top p_{T} (GeV)"
top_pt['name'] = "top_pt"
plots.append( top_pt )

Z_pt        = {sample.name:ROOT.TH1D('Z_pt', 'Z_pt', 25, 0, 500) for sample in samples}
Z_pt['texX'] = "Z p_{T} (GeV)"
Z_pt['name'] = "Z_pt"
plots.append( Z_pt )

Z_cosPhill  = {sample.name:ROOT.TH1D('Z_cosPhill', 'Z_cosPhill', 25, 0, pi) for sample in samples}
Z_cosPhill['texX'] = "#phi(ll)"
Z_cosPhill['name'] = "Z_cosPhill"
plots.append( Z_cosPhill )

for sample in samples:
    reader = sample.fwliteReader( products = products )

    n_non_standard = 0

    reader.start()
    while reader.run( ):

        if reader.position % 1000==0: logger.info("At event %i/%i", reader.position, reader.nEvents)
        if maxN>0 and reader.position > maxN: break
        # All gen particles
        gp      = reader.products['gp']
        # for searching
        search  = GenSearch( gp )

        tops = filter( lambda p:abs(p.pdgId())==6 and search.isLast(p),  gp)
        Zs   = filter( lambda p:abs(p.pdgId())==23 and search.isLast(p), gp)

        if not len(tops)==2:
            logger.warning( "Found %i tops at position %i!", len(tops), reader.position)
            n_non_standard += 1
            continue
        if not len(Zs)==1:
            logger.warning( "Found %i Zs at position %i!", len(Zs), reader.position)
            n_non_standard += 1
            continue

        # Z
        Z_pt[sample.name].Fill(Zs[0].pt())
        Z_daughters = search.daughters( Zs[0] )
        if len(Z_daughters)==2:
            cosPhill = cos(Z_daughters[0].phi() - Z_daughters[1].phi())
        else: 
            cosPhill = float('nan')

        Z_cosPhill[sample.name].Fill( acos(cosPhill) )

        # tops
        top_pt[sample.name].Fill(tops[0].pt())
        top_pt[sample.name].Fill(tops[1].pt())

    logger.info( "Done with running over %i events. Skipped %i events", reader.nEvents, n_non_standard )

for p in plots:
    histos = [ [p[sample.name]] for sample in samples ]
    for i_s, s in enumerate(samples):
        histos[i_s][0].legendText = s.texName
        histos[i_s][0].style = styles.lineStyle(s.color)

for p in plots:
    histos = [ [p[sample.name]] for sample in samples ]
    plot = Plot.fromHisto(name = p['name'], histos =  histos , texX = p['texX'], texY = "" )  
    plotting.draw(plot, plot_directory = "/afs/hephy.at/user/r/rschoefbeck/www/topEFT/gen/", logX = False, logY = False, sorting = False)
