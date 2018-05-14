
#standard imports
import ROOT
import os

# RootTools
from RootTools.core.standard import *

# User specific 
from TopEFT.Tools.user import plot_directory
plot_directory_=os.path.join(plot_directory, 'stacked_plots')
plot_directory=plot_directory_
if not os.path.exists(plot_directory):
    os.makedirs(plot_directory)


# data
samplelist=[]
#add samples 
#sample = Sample.fromFiles( "small", texName = "my first sample!", files = ["/afs/hephy.at/data/rschoefbeck01/cmgTuples/georg/TTJets_SingleLeptonFromTbar_1/treeProducer/tree.root"], treeName="tree")
samplelist.append(Sample.fromFiles( "small", texName = "QCD_Pt120to170", files = ["/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/QCD_Pt120to170/treeProducer/tree.root"], treeName="tree"))
samplelist.append(Sample.fromFiles( "small", texName = "TTJets_SingleLeptonFromTbar", files = ["/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/TTJets_SingleLeptonFromTbar/treeProducer/tree.root"], treeName="tree"))
#samplelist.append(Sample.fromFiles( "small", texName = "QCD_Pt120to170+TTJets_SingleLeptonFromTbar", files = ["/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/QCD_Pt120to170/treeProducer/tree.root","/afs/hephy.at/work/g/gmoertl/y.at/work/g/gmoertl/y.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/TTJets_SingleLeptonFromTbar/treeProducer/tree.root"], treeName="tree"))

# variables to read

variables = [ "run/I", "lumi/I", "evt/l", "lep_trackerHits/I", "lep_innerTrackChi2/F", "lep_pdgId/I", "lep_segmentCompatibility/F", "lep_sigmaIEtaIEta/F", "lep_etaSc/F", "lep_mcMatchPdgId/I", "lep_mcMatchId/I", "lep_mvaIdSpring16/F", "lep_pt/F" ]

#define plots
plots = [ 
    {'name':'electronMVA', 'var':'lep_mvaIdSpring16', 'binning':[100,0,1]},
    #{'name':'trackerHits', 'var':'lep_trackerHits', 'binning':[30,0,30]},
]


# declare histogram
for p in plots:
    p['histo'] = ROOT.TH1F(p['var'], p['var'], *(p['binning']))
    p['samplehistos']=[]
    for sample in samplelist:
        p['samplehistos'].append(ROOT.TH1F(p['var'], sample.texName, *(p['binning'])))

i=0
for sample in samplelist:

    # reader class
    reader = sample.treeReader(  map( TreeVariable.fromString, variables ) )
    
    # loop
    reader.start()

    PdgId=11
    counter=0
    while reader.run():
        #print "run %i, lumi %i, event %i pdgId %i %6.5f" % (reader.event.run, reader.event.lumi, reader.event.evt, reader.event.lep_pdgId, reader.event.lep_segmentCompatibility) 
        counter+=1

        for p in plots:
           if abs(reader.event.lep_pdgId) == PdgId:
                p['histo'].Fill(getattr(reader.event, p['var']))
                p['samplehistos'][i].Fill(getattr(reader.event, p['var']))
           #if counter>1000: break
    i+=1

for p in plots:
    c=ROOT.TCanvas()
    hs=ROOT.THStack()
    j=0
    for histo in p['samplehistos']:
        histo.SetFillColor(2+2*j)
        histo.SetLineColor(1)
        hs.Add(histo)
        j+=1
    hs.Draw('hist') 
    hs.SetTitle(p['name'])
    hs.GetXaxis().SetTitle(p['var'])
    hs.GetYaxis().SetTitle("number of events")
    c.SetLogy()
    c.BuildLegend(0.05,0.75,0.3,0.95,"")
    c.Print(os.path.join(plot_directory, p['name']+ '_stacked_plot.png'))



