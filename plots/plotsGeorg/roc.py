#standard imports
import ROOT
import os
from array import array

# RootTools
from RootTools.core.standard import * 

# User specific 
from TopEFT.Tools.user import plot_directory

# data 
sample = Sample.fromFiles( "small", texName = "my first sample!", files = ["/afs/hephy.at/data/rschoefbeck01/cmgTuples/georg/TTJets_SingleLeptonFromTbar_1/treeProducer/tree.root"], treeName="tree")

# variables to read
variables = [ "run/I", "lumi/I", "evt/l", "lep_trackerHits/I", "lep_innerTrackChi2/F", "lep_pdgId/I", "lep_segmentCompatibility/F", "lep_sigmaIEtaIEta/F", "lep_etaSc/F", "lep_mcMatchPdgId/I", "lep_mcMatchId/I", "lep_mvaIdSpring16/F" ]
#lep_mcMatchId  Match to source from hard scatter (pdgId of heaviest particle in chain, 25 for H, 6 for t, 23/24 for W/Z), zero if non-prompt or fake for Leptons after the preselection : 0 at: 0x52e9680
#lep_mvaIdSpring16 EGamma POG MVA ID, Spring16; 1 for muons for Leptons after the preselection : 0 at: 0x51f8f50

# reader class
reader = sample.treeReader(  map( TreeVariable.fromString, variables ) )

#roc data
rocdata=[]
effdata=[]
p=array('d')
x=array('d')
y=array('d')

#match Id Signal
matchIdSignal=[6,23,24,25,37]
 
#calculate eS and eB
def eS(p, rocdata, matchIdSignal):
    ntruth=0.
    ntruthid=0.
    for data in rocdata:
        if data[0] in matchIdSignal:
            ntruth+=1.
            if data[1]>=p:
                ntruthid+=1.
    return 0. if ntruth==0. else  ntruthid/ntruth

def eB(p, rocdata, matchIdSignal):
    ntruth=0.
    ntruthid=0.
    for data in rocdata:
        if data[0] not in matchIdSignal:
            ntruth+=1.
            if data[1]>=p:
                ntruthid+=1.
    return 0. if ntruth==0. else  ntruthid/ntruth

 
# loop
reader.start()

counter=0
while reader.run():
    if reader.event.lep_pdgId==11:
        rocdata.append([abs(reader.event.lep_mcMatchId),abs(reader.event.lep_mvaIdSpring16)]) 
        #print "mcMatchId %i, mva %f" %(abs(reader.event.lep_mcMatchId), abs(reader.event.lep_mvaIdSpring16))
        counter+=1

    if counter>1000000: break

npmin=10
npmax=100
nmax=0
xymax=0.
for np in xrange(npmin,npmax,1):
    i=np-npmin
    p.append(np/100.)  
    x.append(eS(p[i], rocdata, matchIdSignal))
    y.append(1-eB(p[i], rocdata, matchIdSignal))
    effdata.append([p[i], x[i], y[i]])
    if ((x[i]*y[i])>xymax):
        xymax=x[i]*y[i]
        nmax=i
    print p[i], x[i], y[i]
print "maximum at: ", p[nmax], x[nmax], y[nmax]

# TGraph
#plot_directory_ = os.path.join(plot_directory, 'roc_plots')
#plot_directory=plot_directory_
c=ROOT.TCanvas()
n=len(x)
g=ROOT.TGraph(n,x,y)
g.Draw()
g.SetTitle( 'roc curve' )
g.GetXaxis().SetTitle( 'eS' )
g.GetYaxis().SetTitle( '1-eB' )
g.SetLineColor( 1 )
g.SetLineWidth( 1 )
g.SetMarkerColor( 4 )
g.SetMarkerStyle( 5 )
nmaxtext=ROOT.TLatex()
nmaxtext.SetTextSize(0.04)
nmaxtext.DrawLatex(x[nmax],y[nmax],"mvaId=%1.2f" % p[nmax])
#f1=ROOT.TF1("f1","[2]-([3]-[0]*(TMath::Exp([1]*x)))",0,1)
#f1.SetParLimits(2,0.8,0.9)
#f1.SetParLimits(0,0.8,0.9)
#f1.SetParLimits(3,0.8,0.9)
#g.Fit("f1","R")

c.Print(os.path.join(plot_directory, 'roc_plot.png'))
