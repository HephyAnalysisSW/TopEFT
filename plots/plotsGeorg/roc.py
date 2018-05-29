#standard imports
import ROOT
import os
from array import array

# RootTools
from RootTools.core.standard import * 

# User specific 
from TopEFT.Tools.user import plot_directory
plot_directory_=os.path.join(plot_directory, 'roc_plots')
plot_directory=plot_directory_

# data
samplelist=[]
# add samples

#QCD files
#samplelist.append(Sample.fromFiles( "QCD", texName = "QCD_Pt120to170", files = [
#"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/QCD_Pt120to170/treeProducer/tree.root"
#], treeName="tree"))

#TTJets files
#samplelist.append(Sample.fromFiles( "TTJets", texName = "TTJets_SingleLeptonFromTbar", files = [
#"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/TTJets_SingleLeptonFromTbar/treeProducer/tree.root"
#], treeName="tree"))

#QCD + TTJets
samplelist.append(Sample.fromFiles( "QCD+TTJets", texName = "QCD_Pt120to170+TTJets_SingleLeptonFromTbar", files = [
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/QCD_Pt120to170/treeProducer/tree.root",
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/TTJets_SingleLeptonFromTbar/treeProducer/tree.root",
"/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/TTJets_SingleLeptonFromTbar_1/treeProducer/tree.root"
], treeName="tree"))

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
"lep_mcMatchPdgId/I",
"lep_mcMatchId/I",
"lep_mcMatchAny/I",
"lep_mvaIdSpring16/F",
"lep_pt/F",

"lep_etaSc/F",                  #electrons (|etaSc|<=1.479 barrel cuts, |etaSc|>1.479 endcap cuts)              #Electron supercluster pseudorapidity for Leptons after the preselection : 0 at: 0x4109bd0
"lep_full5x5_sigmaIetaIeta/F",  #electrons (barrel: <0.0104,     endcap: <0.0305)                               #Electron full5x5_sigmaIetaIeta for Leptons after the preselection : 0 at: 0x411d5c0 
"lep_dEtaInSeed/F",             #electrons (barrel: | |<0.00353, endcap: | |<0.00567)                           #DeltaEta wrt ele SC seed for Leptons after the preselection : 0 at: 0x411e850
"lep_dPhiScTrkIn/F",            #electrons (barrel: | |<0.0499,  endcap: | |<0.0165)                            #Electron deltaPhiSuperClusterTrackAtVtx (without absolute value!) for Leptons after the preselection : 0 at: 0x41083f0
"lep_relIso03/F",               #electrons (barrel: <0.0361,     endcap: <0.094)       #muons <0.1              #PF Rel Iso, R=0.3, pile-up corrected for Leptons after the preselection : 0 at: 0x410f640
"lep_eInvMinusPInv/F",          #electrons (barrel: | |<0.0278,  endcap: | |<0.0158)                            #Electron 1/E - 1/p  (without absolute value!) for Leptons after the preselection : 0 at: 0x4108f90   
"lep_lostOuterHits/I",          #electrons (barrel: 1,           endcap: 1)                                     #Number of lost hits on inner track for Leptons after the preselection : 0 at: 0x4101ee0
"lep_convVeto/I",               #electrons yes                                                                  #Conversion veto (always true for muons) for Leptons after the preselection : 0 at: 0x410e5c0
"lep_hadronicOverEm/F",         #electrons                                                                      #Electron hadronicOverEm for Leptons after the preselection : 0 at: 0x4108990
"lep_rho/F",                    #electrons                                                                      #rho for Leptons after the preselection : 0 at: 0x4117d20
"lep_jetDR/F",                                                                         #(muons <=0.3)           #deltaR(lepton, nearest jet) for Leptons after the preselection : 0 at: 0x411ca70
"lep_dxy/F",                                                                           #mouns                   #d_{xy} with respect to PV, in cm (with sign) for Leptons after the preselection : 0 at: 0x410c4b0
"lep_dz/F",                                                                            #mouns                   #d_{z} with respect to PV, in cm (with sign) for Leptons after the preselection : 0 at: 0x410ca30
"lep_isGlobalMuon/I",                                                                  #muons yes               #Muon is global for Leptons after the preselection : 0 at: 0x4106c30
"lep_isPromptId/I",
"lep_isNonPromptId/I",
"lep_isFakeId/I",
]

#select electrons 11, or mouns 13
pdgIds=[11,13]
#pt cut >=
pt_cut=25

#define function to calculate eS and eB
def eS(p, rocdataset):
    ntruth=0.
    ntruthid=0.
    for data in rocdataset:
        if data[0]==1:
            ntruth+=1.
            if data[1]>=p:
                ntruthid+=1.
    return 0. if ntruth==0. else  ntruthid/ntruth

def eB(p, rocdataset):
    ntruth=0.
    ntruthid=0.
    for data in rocdataset:
        if not data[0]==1:
            ntruth+=1.
            if data[1]>=p:
                ntruthid+=1.
    return 0. if ntruth==0. else ntruthid/ntruth

for pdgId in pdgIds:
    lepType="_ele" if pdgId==11 else "_moun" if pdgId==13 else "_defineleptontype"

    for sample in samplelist:
        #roc data
        rocdata=[[],[]]
        pdata=[]
        xdata=[]
        ydata=[]
        nmaxdata=[]
        plotdata=["|pdgId|=%i" %pdgId,"|pdgId|=%i, pt>=%i" %(pdgId, pt_cut)]
        # reader class
        reader = sample.treeReader(  map( TreeVariable.fromString, variables ) )

        # loop
        reader.start()

        counter=0
        while reader.run():
            if abs(reader.event.lep_pdgId)==pdgId:
                rocdata[0].append([reader.event.lep_isPromptId, reader.event.lep_mvaIdSpring16]) 
                #print "pdgId %i, pt %f,  mcMatchId %i, mva %f" %(reader.event.lep_pdgId, reader.event.lep_pt, abs(reader.event.lep_mcMatchId), abs(reader.event.lep_mvaIdSpring16))

                if reader.event.lep_pt>=pt_cut:
                    rocdata[1].append([reader.event.lep_isPromptId, reader.event.lep_mvaIdSpring16])
                    #print "pdgId %i, pt %f,  mcMatchId %i, mva %f" %(reader.event.lep_pdgId, reader.event.lep_pt, abs(reader.event.lep_mcMatchId), abs(reader.event.lep_mvaIdSpring16))
                counter+=1

            #if counter>1000: break

        #calculate eS and eB
        for rocdataset in rocdata:
            p=array('d')
            x=array('d')
            y=array('d')

            npmin=-100
            npmax=100
            nmax=0
            xymax=0.
            for np in xrange(npmin,npmax,1):
                i=np-npmin
                p.append(np/100.)
                x.append(eS(p[i], rocdataset))
                y.append(1-eB(p[i], rocdataset))
                if ((x[i]*y[i])>xymax):
                    xymax=x[i]*y[i]
                    nmax=i
                #print p[i], x[i], y[i]
            print "maximum at: ", p[nmax], x[nmax], y[nmax]
            pdata.append(p)
            xdata.append(x)
            ydata.append(y)
            nmaxdata.append(nmax)

        #Draw TGraph
        c=ROOT.TCanvas()
        mg=ROOT.TMultiGraph()
        mg.Draw("APL")
        g=[]
        nmaxtext=ROOT.TLatex()
        for i in xrange(len(rocdata)):
            p=pdata[i]
            x=xdata[i]
            y=ydata[i]
            gname=plotdata[i]
            nmax=nmaxdata[i]
            n=len(x)
            g.append(ROOT.TGraph(n,x,y))
            g[i].SetName(gname)
            g[i].SetTitle(gname)
            g[i].SetLineColor( 1 )
            g[i].SetLineWidth( 1 )
            g[i].SetMarkerColor( 4+2*i )
            g[i].SetMarkerStyle( 5 )
            g[i].Draw("ALP")
            nmaxtext.DrawLatex(x[nmax],y[nmax],"mvaId=%f1.2" %p[nmax])
            mg.Add(g[i])
        mg.Draw("APL")
        mg.SetTitle( 'roc curve - '+sample.texName )
        mg.GetXaxis().SetTitle( 'eS' )
        mg.GetYaxis().SetTitle( '1-eB' )
        c.BuildLegend()
        if not os.path.exists(plot_directory): 
            os.makedirs(plot_directory)
        c.Print(os.path.join(plot_directory, sample.texName+lepType+'_roc_plot.png'))
