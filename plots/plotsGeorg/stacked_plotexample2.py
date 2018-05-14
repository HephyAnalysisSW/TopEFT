
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

variables = [
"run/I", 
"lumi/I",
"evt/l", 
"lep_trackerHits/I", 
"lep_innerTrackChi2/F", 
"lep_pdgId/I", 
"lep_segmentCompatibility/F", 
"lep_sigmaIEtaIEta/F", 
"lep_etaSc/F", 
"lep_mcMatchPdgId/I", 
"lep_mcMatchId/I", 
"lep_mvaIdSpring16/F", 
"lep_pt/F"
]

#define plots
plots = [ 
    {'name':'MVA', 'var':'lep_mvaIdSpring16', 'binning':[200,-1,1]},
    {'name':'etaSC', 'var':'lep_etaSc', 'binning':[150,-3,3]},
]


# declare histogram
for p in plots:
    p['histo'] = ROOT.TH1F(p['name'], p['var'], *(p['binning']))
    p['samplehistos']=[]
    p['sample_prompt']=[]
    p['sample_non-prompt']=[]
    p['sample_fake']=[]
    for sample in samplelist:
        p['samplehistos'].append(ROOT.TH1F(p['name']+" samplehisto "+sample.texName, sample.texName, *(p['binning'])))
        p['sample_prompt'].append(ROOT.TH1F(p['name']+" prompt "+sample.texName, "prompt ("+sample.texName+")", *(p['binning'])))
        p['sample_non-prompt'].append(ROOT.TH1F(p['name']+" non-prompt "+sample.texName, "non-prompt ("+sample.texName+")", *(p['binning'])))
        p['sample_fake'].append(ROOT.TH1F(p['name']+" fake"+sample.texName, "fake ("+sample.texName+")", *(p['binning'])))

i=0
for sample in samplelist:

    # reader class
    reader = sample.treeReader(  map( TreeVariable.fromString, variables ) )
    
    # loop
    reader.start()

    #match Id for prompt leptons
    matchIdSignal=[6,23,24,25,37]
    matchIdFake=[]
    #selected PdgID
    PdgId=[11]
    particletype="electron"

    counter=0
    while reader.run():
        #print "run %i, lumi %i, event %i pdgId %i %6.5f" % (reader.event.run, reader.event.lumi, reader.event.evt, reader.event.lep_pdgId, reader.event.lep_segmentCompatibility) 
        counter+=1

        for p in plots:
           if abs(reader.event.lep_pdgId) in  PdgId:
                p['histo'].Fill(getattr(reader.event, p['var']))
                p['samplehistos'][i].Fill(getattr(reader.event, p['var']))
                if abs(reader.event.lep_mcMatchId) in matchIdSignal:
                    p['sample_prompt'][i].Fill(getattr(reader.event, p['var']))
                elif abs(reader.event.lep_mcMatchId) in matchIdFake:
                    p['sample_fake'][i].Fill(getattr(reader.event, p['var'])) 
                else:
                    p['sample_non-prompt'][i].Fill(getattr(reader.event, p['var']))
                    #if reader.event.lep_mvaIdSpring16 >= 0.99: print reader.event.lep_mcMatchId
           #if counter>1000: break
    i+=1

for p in plots:
    c=ROOT.TCanvas()
    c.Divide(2,1,0.01,0.01,0)

    #pad 1
    c.cd(1)
    hs1=ROOT.THStack()
    j=0
    for histo in p['samplehistos']:
        histo.SetFillColor(2+2*j)
        histo.SetLineColor(1)
        hs1.Add(histo)
        j+=1
    hs1.Draw('hist') 
    hs1.SetTitle(particletype+' - '+p['name'])
    hs1.GetXaxis().SetTitle(p['var'])
    hs1.GetYaxis().SetTitle("number of events")
    if p['var']=="lep_mvaIdSpring16": c.GetPad(1).SetLogy() 
    c.GetPad(1).BuildLegend(0.11,0.85,0.66,0.95,"").SetTextSize(0.03)

    #pad 2
    c.cd(2)
    hs2=ROOT.THStack()
    i=1
    p['sample_prompt'][i].Scale(1./p['sample_prompt'][i].Integral())
    p['sample_prompt'][i].SetFillColor(4)
    p['sample_prompt'][i].SetLineColor(1)
    hs2.Add(p['sample_prompt'][i])

    p['sample_non-prompt'][i].Scale(1./p['sample_non-prompt'][i].Integral())
    p['sample_non-prompt'][i].SetFillColor(7)
    p['sample_non-prompt'][i].SetLineColor(1)
    hs2.Add(p['sample_non-prompt'][i])

    #p['sample_fake'][i].Scale(1./p['sample_fake'][i].Integral())
    #p['sample_fake'][i].SetFillColor(2)
    #p['sample_fake'][i].SetLineColor(1)
    #hs2.Add(p['sample_fake'][i])

    hs2.Draw('hist')
    hs2.SetTitle(particletype+' - '+p['name'])
    hs2.GetXaxis().SetTitle(p['var'])
    hs2.GetYaxis().SetTitle("number of events")
    if p['var']=="lep_mvaIdSpring16": c.GetPad(2).SetLogy()
    c.GetPad(2).BuildLegend(0.11,0.85,0.86,0.95,"").SetTextSize(0.03)

    c.Print(os.path.join(plot_directory, particletype+'_'+p['name']+ '_stacked_plot.png'))



