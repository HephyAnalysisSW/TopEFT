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
variables = [ "run/I", "lumi/I", "evt/l", "lep_trackerHits/I", "lep_innerTrackChi2/F", "lep_pdgId/I", "lep_segmentCompatibility/F", "lep_sigmaIEtaIEta/F", "lep_etaSc/F", "lep_mcMatchPdgId/I", "lep_mcMatchId/I", "lep_mvaIdSpring16/F" ]
#lep_mcMatchId  Match to source from hard scatter (pdgId of heaviest particle in chain, 25 for H, 6 for t, 23/24 for W/Z), zero if non-prompt or fake for Leptons after the preselection : 0 at: 0x52e9680
#lep_mvaIdSpring16 EGamma POG MVA ID, Spring16; 1 for muons for Leptons after the preselection : 0 at: 0x51f8f50

# reader class
reader = sample.treeReader(  map( TreeVariable.fromString, variables ) )

#roc data
rocdata=[]
effdata=[]

#match Id Signal
matchIdSignal=[6,23,24,25,37]
 
#calculate eS and eB
def eS(p, rocdata, matchIdSignal):
    ntruth=0.
    ntruthid=0.
    for i in range(len(rocdata)):
        if rocdata[i][1]>=p:
            ntruth+=1.
            if rocdata[i][0] in matchIdSignal:
                ntruthid+=1.
    return 0. if ntruth==0. else  ntruthid/ntruth

def eB(p, rocdata, matchIdSignal):
    ntruth=0.
    ntruthid=0.
    for i in range(len(rocdata)):
        if rocdata[i][1]<p:
            ntruth+=1.
            if rocdata[i][0] not in matchIdSignal:
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

for a in range(0,100,1):
    p=a/100.
    effdata.append([p, eS(p, rocdata, matchIdSignal),1-eB(p, rocdata, matchIdSignal)])
    print p, eS(p, rocdata, matchIdSignal),1-eB(p, rocdata, matchIdSignal)

