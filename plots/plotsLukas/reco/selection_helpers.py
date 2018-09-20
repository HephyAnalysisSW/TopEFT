#!/usr/bin/env python
''' helpers script for selection calculation
'''
#
# Standard imports and batch mode
#
import ROOT, os
ROOT.gROOT.SetBatch(True)
import itertools

from math                         import sqrt, cos, sin, pi, acos, cosh
from RootTools.core.standard      import *
from TopEFT.Tools.helpers         import deltaPhi, getObjDict, getVarValue, deltaR, deltaR2

MW = 80.385
Mt = 172.5

def get3LeptonSelection( mode ):
    ''' define 3l selections of ttZ
    '''
    if   mode=="mumumu": return "nGoodMuons==3&&nGoodElectrons==0"
    elif mode=="mumue":  return "nGoodMuons==2&&nGoodElectrons==1"
    elif mode=="muee":   return "nGoodMuons==1&&nGoodElectrons==2"
    elif mode=="eee":    return "nGoodMuons==0&&nGoodElectrons==3"
    elif mode=='all':    return "nGoodMuons+nGoodElectrons==3"

def get2LeptonSelection( mode ):
    ''' define 2l selections of ttgamma
    '''
    if   mode=="mumu":   return "nGoodMuons==2&&nGoodElectrons==0"
    elif mode=="mue":    return "nGoodMuons==1&&nGoodElectrons==1"
    elif mode=="ee":     return "nGoodMuons==0&&nGoodElectrons==2"
    elif mode=='all':    return "nGoodMuons+nGoodElectrons==2"

def get1LeptonSelection( mode ):
    ''' define 1l selections of ttgamma
    '''
    if   mode=="mu":     return "nGoodMuons==1&&nGoodElectrons==0"
    elif mode=="e":      return "nGoodMuons==0&&nGoodElectrons==1"
    elif mode=='all':    return "nGoodMuons+nGoodElectrons==1"


def getDPhiZLep( event, sample ):
    event.dPhiZLep = deltaPhi(event.lep_phi[event.nonZ_l1_index], event.Z_phi)

def getDPhiZJet( event, sample ):
    event.dPhiZJet = deltaPhi(event.jet_phi[0], event.Z_phi) if event.njet>0 and event.Z_mass>0 else float('nan') #nJetSelected

def getSelectedJets( event, sample ):
    jetVars     = ['eta','pt','phi','btagCSV','DFbb', 'DFb', 'id']
    event.selectedJets  = [getObjDict(event, 'jet_', jetVars, i) for i in range(int(getVarValue(event, 'njet'))) if ( abs(event.jet_eta[i])<=2.4 and event.jet_pt[i] > 30 and event.jet_id[i])] #nJetSelected

def getJets( event, sample ):
    jetVars     = ['eta','pt','phi','btagCSV']
    event.jets_sortbtag  = [getObjDict(event, 'jet_', jetVars, i) for i in range(int(getVarValue(event, 'nJetSelected')))] #nJetSelected
    event.jets_sortbtag.sort( key = lambda l:-l['btagCSV'] )

def getAllJets( event, sample ):
    jetVars     = ['eta','pt','btagCSV']
    event.allJets = [getObjDict(event, 'jet_', jetVars, i) for i in range(int(getVarValue(event, 'njet')))]

def getForwardJets( event, sample ):
    event.nJetForward30  = len([j for j in event.allJets if (j['pt']>30 and abs(j['eta'])>2.4) ])
    event.nJetForward40  = len([j for j in event.allJets if (j['pt']>40 and abs(j['eta'])>2.4) ])
    event.nJetForward50  = len([j for j in event.allJets if (j['pt']>50 and abs(j['eta'])>2.4) ])
    event.nJetForward60  = len([j for j in event.allJets if (j['pt']>60 and abs(j['eta'])>2.4) ])
    event.nJetForward70  = len([j for j in event.allJets if (j['pt']>70 and abs(j['eta'])>2.4) ])

def getForwardJets_eta3( event, sample ):
    event.nJetForward30_eta3  = len([j for j in event.allJets if (j['pt']>30 and abs(j['eta'])>3.0) ])
    event.nJetForward40_eta3  = len([j for j in event.allJets if (j['pt']>40 and abs(j['eta'])>3.0) ])
    event.nJetForward50_eta3  = len([j for j in event.allJets if (j['pt']>50 and abs(j['eta'])>3.0) ])
    event.nJetForward60_eta3  = len([j for j in event.allJets if (j['pt']>60 and abs(j['eta'])>3.0) ])
    event.nJetForward70_eta3  = len([j for j in event.allJets if (j['pt']>70 and abs(j['eta'])>3.0) ])

def getForwardJetEta( event, sample ):
    event.forwardJets = [j for j in event.allJets if j['btagCSV']<0.8484 ]
    event.forwardJet1_eta = -999
    event.forwardJet1_pt  = -999
    event.forwardJet2_eta = -999
    event.forwardJet2_pt  = -999
    if len(event.forwardJets) > 0:
        event.forwardJet1_eta = abs(event.forwardJets[0]['eta'])
        event.forwardJet1_pt  = event.forwardJets[0]['pt']
    
        if len(event.forwardJets) > 1:
            event.forwardJet2_eta = abs(event.forwardJets[1]['eta'])
            event.forwardJet2_pt  = event.forwardJets[1]['pt']

def getCPVars( event, sample ):
    lepton  = ROOT.TVector3()
    bjets = []
    nonbjets = []
    maxBJets = 2
    bjetCounter = 0
    mt_had = 0
    mw_had = 0
    
    # get the bjet and non-bjet collection
    for j in event.selectedJets:
        jet = ROOT.TLorentzVector()
        jet.SetPtEtaPhiM(j['pt'], j['eta'], j['phi'], 0)

        # get the 2 hardest b jets
        if j['btagCSV'] > 0.8484 and bjetCounter < 2:
            bjetCounter += 1
            bjets.append(jet)
        else:
            nonbjets.append(jet)

    # do a chi2 minimization to get the hadronic and leptonic top quarks. mjj and mbjj are not independent - is this still valid?
    chi2min = float('Inf')

    jetcombinations = [ x for x in itertools.combinations(range(len(nonbjets)),2) ]
    for i, b in enumerate(bjets):
        for j, jetComb in enumerate(itertools.combinations(nonbjets,2)):
            mbjj = ( b + jetComb[0] + jetComb[1] ).M()
            mjj  = ( jetComb[0] + jetComb[1] ).M()
            x = (mjj - MW)**2/MW + (mbjj - Mt)**2/Mt
            if x < chi2min:
                chi2min = x
                hadTopJetIndices = (i, jetcombinations[j][0], jetcombinations[j][1])
                leptonicTopJetIndex = 1 - i
                mt_had = mbjj
                mw_had = mjj

    # asign the b quarks accordingly
    leptonCharge = -event.lep_pdgId[event.nonZ_l1_index]/abs(event.lep_pdgId[event.nonZ_l1_index])
    if leptonCharge > 0:
        b       = bjets[leptonicTopJetIndex]
        bbar    = bjets[hadTopJetIndices[0]]
    else:
        b       = bjets[hadTopJetIndices[0]]
        bbar    = bjets[leptonicTopJetIndex]

    # also get the highest pt jet from the hadronic W, as well as the lepton and met
    jet         = nonbjets[hadTopJetIndices[1]]
    lepton      = ROOT.TLorentzVector()
    met         = ROOT.TLorentzVector()
    lepton.SetPtEtaPhiM( event.lep_pt[event.nonZ_l1_index], event.lep_eta[event.nonZ_l1_index], event.lep_phi[event.nonZ_l1_index], 0)
    met.SetPtEtaPhiM( event.met_pt, 0, event.met_phi, 0)
    
    event.mt_had = mt_had
    event.mw_had = mw_had
    event.mt_lep = (lepton + met + bjets[leptonicTopJetIndex]).M()
    event.mw_lep = (lepton + met).M()
    event.chi2min = chi2min
    
    # calculate the observables listed in arxiv:1611.08931
    b3      = ROOT.TVector3(b.X(), b.Y(), b.Z())
    bbar3   = ROOT.TVector3(bbar.X(), bbar.Y(), bbar.Z())
    jet3    = ROOT.TVector3(jet.X(), jet.Y(), jet.Z())
    lepton3 = ROOT.TVector3(lepton.X(), lepton.Y(), lepton.Z())

    O2 = (b3 + bbar3) * (lepton3.Cross(jet3))

    O4 = (b3 - bbar3) * (lepton3.Cross(jet3))
    O4 = O4*leptonCharge
        
    O7 = (b3 -bbar3).Z() * (b3.Cross(bbar3)).Z()
    
    event.O2 = int(O2/abs(O2))
    event.O4 = int(O4/abs(O4))
    event.O7 = int(O7/abs(O7))
    
    # to get O3, we need to boost in the b-bbar system
    bbbarsystem = (b + bbar).BoostVector()
    lepton.Boost(-bbbarsystem)
    b.Boost(-bbbarsystem)
    jet.Boost(-bbbarsystem)
    
    b3      = ROOT.TVector3(b.X(), b.Y(), b.Z())
    jet3    = ROOT.TVector3(jet.X(), jet.Y(), jet.Z())
    lepton3 = ROOT.TVector3(lepton.X(), lepton.Y(), lepton.Z())
    
    O3 = b3 * (lepton3.Cross(jet3))
    O3 = O3*leptonCharge
    
    event.O3 = int(O3/abs(O3))
    
def getL( event, sample):

    # get the lepton and met
    lepton  = ROOT.TLorentzVector()
    met     = ROOT.TLorentzVector()
    lepton.SetPtEtaPhiM(event.lep_pt[event.nonZ_l1_index], event.lep_eta[event.nonZ_l1_index], event.lep_phi[event.nonZ_l1_index], 0)
    met.SetPtEtaPhiM(event.met_pt, 0, event.met_phi, 0)

    # get the W boson candidate
    W   = lepton + met
    
    # calculate Lp
    event.Lp = ( W.Px()*lepton.Px() + W.Py()*lepton.Py() ) / (W.Px()**2 + W.Py()**2 )

    event.deltaPhi_Wl = acos( ( W.Px()*lepton.Px() + W.Py()*lepton.Py() ) / sqrt( (W.Px()**2 + W.Py()**2 ) * ( lepton.Px()**2 + lepton.Py()**2 ) ) )

def reconstructLeptonicTop( event, sample ):

    #print
    #print "Next event"
    lepton  = ROOT.TLorentzVector()
    met     = ROOT.TLorentzVector()
    n1      = ROOT.TLorentzVector()
    n2      = ROOT.TLorentzVector()
    b1      = ROOT.TLorentzVector()
    b2      = ROOT.TLorentzVector()

    MW = 80.385
    Mt = 172.5
    
    lepton.SetPtEtaPhiM(event.lep_pt[event.nonZ_l1_index], event.lep_eta[event.nonZ_l1_index], event.lep_phi[event.nonZ_l1_index], 0)
    met.SetPtEtaPhiM(event.met_pt, 0, event.met_phi, 0)

    # get the b from the top decay, assume back-to-back of the tops
    t1 = lepton + met + b1
    t2 = lepton + met + b2
    if t2.Pt() > t1.Pt(): b1, b2 = b2, b1

    a = lepton.Pz()*( 2*(lepton.Px()*met.Px() + lepton.Py()*met.Py()) - lepton.M()**2 + MW**2 )
    arg = lepton.E()**2 * ( ( 2*(lepton.Px()*met.Px() + lepton.Py()*met.Py()) - lepton.M()**2 + MW**2 )**2 - 4*met.Pt()**2 * (lepton.E()**2 - lepton.Pz()**2) )
    b = sqrt( arg ) if arg>0 else 0. # need this for events with MET mismeasurements
    c =  2 * (lepton.E()**2 - lepton.Pz()**2) 
    MET_z_1 = (a+b)/c
    MET_z_2 = (a-b)/c

    E_n1 = sqrt(met.Px()**2 + met.Py()**2 + MET_z_1**2)
    E_n2 = sqrt(met.Px()**2 + met.Py()**2 + MET_z_2**2)

    n1.SetPxPyPzE(met.Px(), met.Py(), MET_z_1, E_n1)
    n2.SetPxPyPzE(met.Px(), met.Py(), MET_z_2, E_n2)

    W1 = lepton + n1
    W2 = lepton + n2

    t1 = lepton + n1 + b1
    t2 = lepton + n2 + b1
    
    # get top candidate with mass closer to Mt
    if abs(t2.M() - Mt) < abs(t1.M() - Mt): t1, t2 = t2, t1
    #print t1.M(), t2.M()
    
    event.mt_1 = t1.Mt()
    event.mt_2 = t2.Mt()

    event.top1_mass = t1.M()
    event.top1_pt   = t1.Pt()
    event.top1_phi  = t1.Phi()

    event.top2_mass = t2.M()
    event.top2_pt   = t2.Pt()
    event.top2_phi  = t2.Phi()

    event.b1_pt     = b1.Pt()
    event.b1_phi    = b1.Phi()
    event.b2_pt     = b2.Pt()
    event.b2_phi    = b2.Phi()

    event.deltaPhi_tl = acos( ( t1.Px()*lepton.Px() + t1.Py()*lepton.Py() ) / sqrt( (t1.Px()**2 + t1.Py()**2 ) * ( lepton.Px()**2 + lepton.Py()**2 ) ) )
    lepton.Boost(-t1.BoostVector())
    event.deltaPhi_tl_topRF = deltaPhi( lepton.Phi(), t1.Phi() )
    event.deltaR_tl_topRF = deltaR( {'eta':lepton.Eta(), 'phi':lepton.Phi()}, {'eta':t1.Eta(), 'phi':t1.Phi()}  )
    event.deltaEta_tl_topRF = abs( lepton.Eta() - t1.Eta() )
    
def getCosThetaStar( event, sample ):
    # get the negative-charge lepton from Z
    lm_index = event.Z_l1_index if event.lep_pdgId[event.Z_l1_index] > 0 else event.Z_l2_index
    
    # get the Z and lepton vectors
    Z   = ROOT.TVector3()
    l   = ROOT.TVector3()

    # set the values
    Z.SetPtEtaPhi(event.Z_pt,               event.Z_eta,                event.Z_phi)
    l.SetPtEtaPhi(event.lep_pt[lm_index],   event.lep_eta[lm_index],    event.lep_phi[lm_index])

    # get cos(theta)
    cosTheta = Z*l / (sqrt(Z*Z) * sqrt(l*l))
    
    # get beta and gamma
    gamma   = sqrt(1+event.Z_pt**2/event.Z_mass**2 * cosh(event.Z_eta)**2 )
    beta    = sqrt( 1 - 1/gamma**2 )
    
    cosThetaStar = (-beta + cosTheta) / (1 - beta*cosTheta)
    event.cosThetaStar = cosThetaStar

def getM3l( event, sample ):
    # get the invariant mass of the 3l system
    l = []
    for i in range(3):
        l.append(ROOT.TLorentzVector())
        l[i].SetPtEtaPhiM(event.lep_pt[i], event.lep_eta[i], event.lep_phi[i],0)
    event.threelmass = (l[0] + l[1] + l[2]).M()

def getWpt( event, sample):

    # get the lepton and met
    lepton  = ROOT.TLorentzVector()
    met     = ROOT.TLorentzVector()
    lepton.SetPtEtaPhiM(event.lep_pt[event.nonZ_l1_index], event.lep_eta[event.nonZ_l1_index], event.lep_phi[event.nonZ_l1_index], 0)
    met.SetPtEtaPhiM(event.met_pt, 0, event.met_phi, 0)

    # get the W boson candidate
    W   = lepton + met
    event.W_pt = W.Pt()

def getLooseLeptonMult( event, sample ):
    leptons = [getObjDict(event, 'lep_', ['eta','pt','phi','charge', 'pdgId', 'sourceId','mediumMuonId'], i) for i in range(len(event.lep_pt))]
    lepLoose = [ l for l in leptons if l['pt'] > 10 and ((l['mediumMuonId'] and abs(l['pdgId'])==13) or abs(l['pdgId'])==11)  ]
    event.nLepLoose = len(lepLoose)

