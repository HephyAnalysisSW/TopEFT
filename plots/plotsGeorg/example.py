# Standard imports
import ROOT
import os

# RootTools
from RootTools.core.standard import *

# User specific 
from TopEFT.Tools.user import plot_directory

# data 
sample = Sample.fromFiles( "small", texName = "my first sample!", files = ["/afs/hephy.at/data/rschoefbeck01/cmgTuples/georg/TTJets_SingleLeptonFromTbar_1/treeProducer/tree.root"], treeName="tree")

# variables to read

variables = [ "run/I", "lumi/I", "evt/l", "lep_trackerHits/I", "lep_innerTrackChi2/F", "lep_pdgId/I", "lep_segmentCompatibility/F", "lep_sigmaIEtaIEta/F", "lep_etaSc/F", "lep_mcMatchPdgId/I" ]

# reader class
reader = sample.treeReader(  map( TreeVariable.fromString, variables ) )

# loop
reader.start()

# declare histogram
h = ROOT.TH1F("segmentCompatibility", "segmentCompatibility", 20,0,1)

counter=0
while reader.run():
    print "run %i, lumi %i, event %i pdgId %i %6.5f" % (reader.event.run, reader.event.lumi, reader.event.evt, reader.event.lep_pdgId, reader.event.lep_segmentCompatibility) 
    counter+=1
    h.Fill(reader.event.lep_segmentCompatibility)
    if counter>10: break

c = ROOT.TCanvas()
h.Draw('hist')
c.Print(os.path.join(plot_directory, 'my_first_plot.png'))
