# Standard imports
import ROOT
from RootTools.core.standard import *

# data 
sample = Sample.fromFiles( "small", texName = "my first sample!", files = ["/afs/hephy.at/data/rschoefbeck01/cmgTuples/georg/TTJets_SingleLeptonFromTbar_1/treeProducer/tree.root"], treeName="tree")

# variables to read

variables = [ "run/I", "lumi/I", "evt/l", "lep_trackerHits/I", "innerTrackChi2/F", "pdgId/I", "segmentCompatibility/F", "sigmaIEtaIEta/F", "etaSc/F", "mcMatchPdgId/I" ]

# reader class
reader = sample.treeReader= map( TreeVariable.fromString, variables )

# loop
reader.initialize()

counter=0
while reader.run():
    print "run %i, lumi %i, event %i pdgId %i %6.5f" % (reader.event.run, reader.event.lumi, reader.event.evt, reader.event.pdgId, reader.event.segmentCompatibility) 
    counter+=1

    if counter>10: break
