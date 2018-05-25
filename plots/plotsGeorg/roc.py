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

#sample = Sample.fromFiles( "small", texName = "my first sample!", files = ["/afs/hephy.at/data/rschoefbeck01/cmgTuples/georg/TTJets_SingleLeptonFromTbar_1/treeProducer/tree.root"], treeName="tree")
samplelist.append(Sample.fromFiles( "small", texName = "QCD_Pt120to170", files = ["/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/QCD_Pt120to170/treeProducer/tree.root"], treeName="tree"))
samplelist.append(Sample.fromFiles( "small", texName = "TTJets_SingleLeptonFromTbar", files = ["/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/TTJets_SingleLeptonFromTbar/treeProducer/tree.root"], treeName="tree"))
samplelist.append(Sample.fromFiles( "small", texName = "QCD_Pt120to170+TTJets_SingleLeptonFromTbar", files = ["/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/QCD_Pt120to170/treeProducer/tree.root","/afs/hephy.at/work/g/gmoertl/CMSSW_9_4_6_patch1/src/CMSData/TTJets_SingleLeptonFromTbar/treeProducer/tree.root"], treeName="tree"))


# variables to read
variables = [ "run/I", "lumi/I", "evt/l", "lep_trackerHits/I", "lep_innerTrackChi2/F", "lep_pdgId/I", "lep_segmentCompatibility/F", "lep_sigmaIEtaIEta/F", "lep_etaSc/F", "lep_mcMatchPdgId/I", "lep_mcMatchId/I", "lep_mvaIdSpring16/F", "lep_pt/F" ]
#lep_mcMatchId  Match to source from hard scatter (pdgId of heaviest particle in chain, 25 for H, 6 for t, 23/24 for W/Z), zero if non-prompt or fake for Leptons after the preselection : 0 at: 0x52e9680
#lep_mvaIdSpring16 EGamma POG MVA ID, Spring16; 1 for muons for Leptons after the preselection : 0 at: 0x51f8f50

#match Id Signal
matchIdSignal=[6,23,24,25,37]
 
#define function to calculate eS and eB
def eS(p, rocdataset):
    ntruth=0.
    ntruthid=0.
    for data in rocdataset:
        if data[0] in matchIdSignal:
            ntruth+=1.
            if data[1]>=p:
                ntruthid+=1.
    return 0. if ntruth==0. else  ntruthid/ntruth

def eB(p, rocdataset):
    ntruth=0.
    ntruthid=0.
    for data in rocdataset:
        if data[0] not in matchIdSignal:
            ntruth+=1.
            if data[1]>=p:
                ntruthid+=1.
    return 0. if ntruth==0. else ntruthid/ntruth

for sample in samplelist:
    #roc data
    rocdata=[[],[]]
    pdata=[]
    xdata=[]
    ydata=[]
    nmaxdata=[]
    plotdata=["|pdgId|=11","|pdgId=11|, pt>=25"]
    # reader class
    reader = sample.treeReader(  map( TreeVariable.fromString, variables ) )

    # loop
    reader.start()

    counter=0
    while reader.run():
        if abs(reader.event.lep_pdgId)==11:
            rocdata[0].append([abs(reader.event.lep_mcMatchId), abs(reader.event.lep_mvaIdSpring16)]) 
            #print "pdgId %i, pt %f,  mcMatchId %i, mva %f" %(reader.event.lep_pdgId, reader.event.lep_pt, abs(reader.event.lep_mcMatchId), abs(reader.event.lep_mvaIdSpring16))

            if reader.event.lep_pt>=25:
                rocdata[1].append([abs(reader.event.lep_mcMatchId), abs(reader.event.lep_mvaIdSpring16)])
                #print "pdgId %i, pt %f,  mcMatchId %i, mva %f" %(reader.event.lep_pdgId, reader.event.lep_pt, abs(reader.event.lep_mcMatchId), abs(reader.event.lep_mvaIdSpring16))
            counter+=1

        #if counter>1000: break

    #calculate eS and eB
    for rocdataset in rocdata:
        p=array('d')
        x=array('d')
        y=array('d')

        npmin=10
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
    c.Print(os.path.join(plot_directory, sample.texName+'_roc_plot.png'))
