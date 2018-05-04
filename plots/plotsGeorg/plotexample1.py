
#standard imports
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

# variables for plots

#varplot=["lep_trackerHits", "lep_innerTrackChi2", "lep_pdgId", "lep_segmentCompatibility", "lep_sigmaIEtaIEta", "lep_etaSc"]
#varplotbins={"lep_trackerHits": 100, "lep_innerTrackChi2": 100, "lep_pdgId": 50, "lep_segmentCompatibility": 100, "lep_sigmaIEtaIEta": 100, "lep_etaSc": 100}
#varplotmin={"lep_trackerHits": 0, "lep_innerTrackChi2": 0, "lep_pdgId": -25, "lep_segmentCompatibility": 0, "lep_sigmaIEtaIEta": 0, "lep_etaSc": 0}
#varplotmax={"lep_trackerHits": 1, "lep_innerTrackChi2": 1, "lep_pdgId": 25, "lep_segmentCompatibility": 1, "lep_sigmaIEtaIEta": 1, "lep_etaSc": 1}

plots = [ 
    {'name':'trackerHits', 'var':'lep_trackerHits', 'binning':[30,0,30]},
    #{'name':'trackerHits', 'var':'lep_trackerHits', 'binning':[30,0,30]},
]

# reader class
reader = sample.treeReader(  map( TreeVariable.fromString, variables ) )

# loop
reader.start()

# declare histogram

for p in plots:
    p['histo'] = ROOT.TH1F(p['var'], p['var'], *(p['binning']))

PdgId=11
counter=0
while reader.run():
    #print "run %i, lumi %i, event %i pdgId %i %6.5f" % (reader.event.run, reader.event.lumi, reader.event.evt, reader.event.lep_pdgId, reader.event.lep_segmentCompatibility) 
    counter+=1

    #reader_dict = {"lep_trackerHits/I": reader.event.lep_trackerHits,"lep_innerTrackChi2/F": reader.event.lep_innerTrackChi2,"lep_pdgId/I": reader.event.lep_pdgId,"lep_segmentCompatibility/F": reader.event.lep_segmentCompatibility,"lep_sigmaIEtaIEta/F": reader.event.lep_sigmaIEtaIEta,"lep_etaSc/F": reader.event.lep_etaSc}

    for p in plots:
       
        #if abs(reader.event.lep_pdgId) == PdgId: hdict[str("h_"+var)].Fill(reader_dict[str(var)])
        if abs(reader.event.lep_pdgId) == PdgId: p['histo'].Fill(getattr(reader.event, p['var']))

        if counter>1000: break

ptype='particle_type'
if PdgId==11: ptype='electron'
if PdgId==13: ptype='muon'

for p in plots:
    c=ROOT.TCanvas()
    p['histo'].Draw('hist') 
    c.SetLogy()
    c.SetLineColor(4)
    p['histo'].SetFillColor(7)
    c.Print(os.path.join(plot_directory, p['name']+'_plot.png'))



