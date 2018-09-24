#!/usr/bin/env python
''' plotList ttZ
'''
import ROOT, os
ROOT.gROOT.SetBatch(True)
import itertools

from math                         import sqrt, cos, sin, pi, acos, cosh
from RootTools.core.standard      import *
from TopEFT.Tools.helpers         import deltaPhi, getObjDict, getVarValue, deltaR, deltaR2


#
# ttZ Variables
#
def ttZVariables():
    ''' return read_variables list for ttZ 3l plots
    '''

    read_variables = ["weight/F",
                      "jet[pt/F,eta/F,phi/F,btagCSV/F,DFb/F,DFbb/F,id/I]", "njet/I","nJetSelected/I",
                      "lep[pt/F,eta/F,phi/F,pdgId/I]", "nlep/I",
                      "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I",
                      "Z_l1_index/I", "Z_l2_index/I", "nonZ_l1_index/I", "nonZ_l2_index/I",
                      "Z_phi/F","Z_pt/F", "Z_mass/F", "Z_eta/F","Z_lldPhi/F", "Z_lldR/F"
                      ]

    return read_variables


#
# ttZ Sequence functions
#

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
    
    #print event.O2, event.O3, event.O4, event.O7

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

def get_powheg_reweight( histo_pow, histo_amc ):
    def get_histo_reweight(Z_pt):
        return histo_pow.GetBinContent(histo_amc.FindBin( Z_pt ))/histo_amc.GetBinContent(histo_amc.FindBin( Z_pt ) )
    return get_histo_reweight


#
# ttZ Sequence
#

def ttZSequence():
    ''' return sequence list for ttZ 3l plots
    '''

    sequence = []

    sequence.append( getSelectedJets )
    #sequence += [ getAllJets, getForwardJets, getForwardJets_eta3, getForwardJetEta ]
    sequence += [ getDPhiZLep, getDPhiZJet,getJets ]
    #sequence.append( getCPVars )
    sequence.append( getL )
    #sequence.append( reconstructLeptonicTop )
    sequence.append( getCosThetaStar )
    sequence.append( getM3l )
    sequence.append( getWpt )
    sequence.append( getLooseLeptonMult )

    return sequence


#
# ttZ Plots
#

def ttZPlots( index ):
    ''' return plot list for ttZ 3l plots
    '''

    plots = []
    
    plots.append(Plot(
      name = 'yield', texX = 'yield', texY = 'Number of Events',
      attribute = lambda event, sample: 0.5 + index,
      binning=[4, 0, 4],
    ))
    
    plots.append(Plot(
      name = 'nVtxs', texX = 'vertex multiplicity', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nVert/I" ),
      binning=[50,0,50],
    ))
    
    plots.append(Plot(
        texX = 'E_{T}^{miss} (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "met_pt/F" ),
        binning=[400/20,0,400],
    ))
    
    plots.append(Plot(
        texX = '#phi(E_{T}^{miss})', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "met_phi/F" ),
        binning=[10,-pi,pi],
    ))
    
    plots.append(Plot(
        texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[20,0,400],
    ))
    
    plots.append(Plot(
        name = "W_pt",
        texX = 'p_{T}(W) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample:event.W_pt,
        binning=[20,0,400],
    ))
    
    plots.append(Plot(
        name = 'Z_pt_coarse', texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 50 GeV',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[16,0,800],
    ))
    
    plots.append(Plot(
        name = 'Z_pt_superCoarse', texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[3,0,600],
    ))
    
    plots.append(Plot(
        name = 'Z_pt_analysis', texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 100 GeV',
        attribute = TreeVariable.fromString( "Z_pt/F" ),
        binning=[4,0,400],
    ))
    
    plots.append(Plot(
        name = "invM_3l",
        texX = 'M(3l) (GeV)', texY = 'Number of Events',
        attribute = lambda event, sample:event.threelmass,
        binning=[25,0,500],
    ))
    
    plots.append(Plot(
        texX = '#Delta#phi(ll)', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z_lldPhi/F" ),
        binning=[10,0,pi],
    ))

    plots.append(Plot(
        name = "dPhiZL",
        texX = '#Delta#phi(Z,l)', texY = 'Number of Events',
        attribute = lambda event, sample:event.dPhiZLep,
        binning=[10,0,pi],
    ))
    
    #plots.append(Plot(
    #    name = "O2_sign",
    #    texX = 'O2/|O2|', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.O2,
    #    binning=[2,-2,2],
    #))

    #plots.append(Plot(
    #    name = "O3_sign",
    #    texX = 'O3/|O3|', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.O3,
    #    binning=[2,-2,2],
    #))

    #plots.append(Plot(
    #    name = "O4_sign",
    #    texX = 'O4/|O4|', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.O4,
    #    binning=[2,-2,2],
    #))

    #plots.append(Plot(
    #    name = "O7_sign",
    #    texX = 'O7/|O7|', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.O7,
    #    binning=[2,-2,2],
    #))
    #
    #plots.append(Plot(
    #    name = "mt_had",
    #    texX = 'M(had. top)', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.mt_had,
    #    binning=[20,0,300],
    #))
    #
    #plots.append(Plot(
    #    name = "mt_lep",
    #    texX = 'M(lep. top)', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.mt_lep,
    #    binning=[20,0,300],
    #))

    #plots.append(Plot(
    #    name = "mw_had",
    #    texX = 'M(had. W)', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.mw_had,
    #    binning=[20,0,200],
    #))

    #plots.append(Plot(
    #    name = "mw_lep",
    #    texX = 'M(lep. W)', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.mw_lep,
    #    binning=[20,0,200],
    #))
    #
    #plots.append(Plot(
    #    name = "chi2min",
    #    texX = 'min(#chi^2)', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.chi2min,
    #    binning=[20,0,200],
    #))

    
    #plots.append(Plot(
    #    name = "nForwardJet_Pt30_eta3",
    #    texX = 'nJet p_{T}(j)>30 GeV', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.nJetForward30_eta3,
    #    binning=[10,0,10],
    #))
    #
    #plots.append(Plot(
    #    name = "nForwardJet_Pt40_eta3",
    #    texX = 'nJet p_{T}(j)>40 GeV', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.nJetForward40_eta3,
    #    binning=[10,0,10],
    #))

    #plots.append(Plot(
    #    name = "nForwardJet_Pt50_eta3",
    #    texX = 'nJet p_{T}(j)>50 GeV', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.nJetForward50_eta3,
    #    binning=[10,0,10],
    #))

    #plots.append(Plot(
    #    name = "nForwardJet_Pt60_eta3",
    #    texX = 'nJet p_{T}(j)>60 GeV', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.nJetForward60_eta3,
    #    binning=[10,0,10],
    #))

    #plots.append(Plot(
    #    name = "nForwardJet_Pt70_eta3",
    #    texX = 'nJet p_{T}(j)>70 GeV', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.nJetForward70_eta3,
    #    binning=[10,0,10],
    #))
    
    #plots.append(Plot( #FIXME -> what is this? Didn't understand the formula
    #    name = "dPhiZL_RF",
    #    texX = '#Delta#phi(Z,l) in Z RF', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.dPhiZLep_RF,
    #    binning=[10,0,pi],
    #))
    
    plots.append(Plot(
        name = "dPhiZJet",
        texX = '#Delta#phi(Z,j1)', texY = 'Number of Events',
        attribute = lambda event, sample:event.dPhiZJet,
        binning=[10,0,pi],
    ))
    
    plots.append(Plot(
        name = "lZ1_pt",
        texX = 'p_{T}(l_{1,Z}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l1_index],
        binning=[30,0,300],
    ))
    
    plots.append(Plot(
        name = "lZ1_pt_coarse",
        texX = 'p_{T}(l_{1,Z}) (GeV)', texY = 'Number of Events / 40 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l1_index],
        binning=[10,0,400],
    ))
    
    plots.append(Plot(
        name = 'lZ1_pt_ext', texX = 'p_{T}(l_{1,Z}) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l1_index],
        binning=[20,40,440],
    ))
    
    plots.append(Plot(
        name = "lZ2_pt",
        texX = 'p_{T}(l_{2,Z}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l2_index],
        binning=[20,0,200],
    ))
    
    plots.append(Plot(
        name = "lZ2_pt_coarse",
        texX = 'p_{T}(l_{2,Z}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l2_index],
        binning=[10,0,200],
    ))
    
    plots.append(Plot(
        name = 'lZ2_pt_ext', texX = 'p_{T}(l_{2,Z}) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z_l2_index],
        binning=[20,0,400],
    ))
    
    plots.append(Plot(
        name = 'lnonZ1_pt',
        texX = 'p_{T}(l_{1,extra}) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample:event.lep_pt[event.nonZ_l1_index],
        binning=[15,0,300],
    ))

    plots.append(Plot(
        name = 'lnonZ1_pt_coarse',
        texX = 'p_{T}(l_{1,extra}) (GeV)', texY = 'Number of Events / 60 GeV',
        attribute = lambda event, sample:event.lep_pt[event.nonZ_l1_index],
        binning=[3,0,180],
    ))

    plots.append(Plot(
        name = 'lnonZ1_pt_ext',
        texX = 'p_{T}(l_{1,extra}) (GeV)', texY = 'Number of Events / 30 GeV',
        attribute = lambda event, sample:event.lep_pt[event.nonZ_l1_index],
        binning=[6,0,180],
    ))
    
    
    plots.append(Plot(
        texX = 'M(ll) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "Z_mass/F" ),
        binning=[10,81,101],
    ))

    plots.append(Plot(
        name = "Z_mass_wide",
        texX = 'M(ll) (GeV)', texY = 'Number of Events / 2 GeV',
        attribute = TreeVariable.fromString( "Z_mass/F" ),
        binning=[50,20,120],
    ))
    
    plots.append(Plot(
      texX = 'N_{jets}', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nJetSelected/I" ), #nJetSelected
      binning=[8,-0.5,7.5],
    ))
    
    plots.append(Plot(
      texX = 'N_{b-tag}', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nBTag/I" ), #nJetSelected
      binning=[4,-0.5,3.5],
    ))
    
    plots.append(Plot(
      texX = 'N_{l, loose}', texY = 'Number of Events',
      name = 'nLepLoose', attribute = lambda event, sample: event.nLepLoose,
      binning=[5,2.5,7.5],
    ))
    
    plots.append(Plot(
      texX = 'p_{T}(leading l) (GeV)', texY = 'Number of Events / 20 GeV',
      name = 'lep1_pt', attribute = lambda event, sample: event.lep_pt[0],
      binning=[400/20,0,400],
    ))

    plots.append(Plot(
      texX = 'p_{T}(subleading l) (GeV)', texY = 'Number of Events / 10 GeV',
      name = 'lep2_pt', attribute = lambda event, sample: event.lep_pt[1],
      binning=[200/10,0,200],
    ))

    plots.append(Plot(
      texX = 'p_{T}(trailing l) (GeV)', texY = 'Number of Events / 10 GeV',
      name = 'lep3_pt', attribute = lambda event, sample: event.lep_pt[2],
      binning=[150/10,0,150],
    ))
    
    #plots.append(Plot(
    #  texX = 'p_{T}(Z l+) (GeV)', texY = 'Number of Events / 10 GeV',
    #  name = 'lZp_pt', attribute = lambda event, sample: event.lZp_pt,
    #  binning=[20,0,200],
    #))
    #
    #plots.append(Plot(
    #  texX = 'p_{T}(Z l-) (GeV)', texY = 'Number of Events / 10 GeV',
    #  name = 'lZm_pt', attribute = lambda event, sample: event.lZm_pt,
    #  binning=[20,0,200],
    #))
    
    plots.append(Plot(
      texX = 'p_{T}(leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
      name = 'jet1_pt', attribute = lambda event, sample: event.jet_pt[0],
      binning=[600/30,0,600],
    ))
    
    plots.append(Plot(
      texX = 'p_{T}(2nd leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
      name = 'jet2_pt', attribute = lambda event, sample: event.jet_pt[1],
      binning=[600/30,0,600],
    ))

    ##if len(event.forwardJets)>0:
    #plots.append(Plot(
    #  texX = 'p_{T}(leading jet) (GeV)', texY = 'Number of Events / 10 GeV',
    #  name = 'forwardJet1_pt', attribute = lambda event, sample: event.forwardJet1_pt,
    #  binning=[30,0,300],
    #))

    #plots.append(Plot(
    #  texX = '#eta(leading jet) (GeV)', texY = 'Number of Events',
    #  name = 'forwardJet1_eta', attribute = lambda event, sample: event.forwardJet1_eta,
    #  binning=[20,0.,5.],
    #))
    #
    ##if len(event.forwardJets)>1:
    #plots.append(Plot(
    #  texX = 'p_{T}(sub-leading jet) (GeV)', texY = 'Number of Events / 10 GeV',
    #  name = 'forwardJet2_pt', attribute = lambda event, sample: event.forwardJet2_pt,
    #  binning=[30,0,300],
    #))

    #plots.append(Plot(
    #  texX = '#eta(sub-leading jet) (GeV)', texY = 'Number of Events',
    #  name = 'forwardJet2_eta', attribute = lambda event, sample: event.forwardJet2_eta,
    #  binning=[20,0.,5.],
    #))


    #plots.append(Plot(
    #  texX = 'p_{T}(leading b-jet cand) (GeV)', texY = 'Number of Events / 20 GeV',
    #  name = 'bjet1_pt', attribute = lambda event, sample: event.b1_pt,
    #  binning=[20,0,400],
    #))

    #plots.append(Plot(
    #  texX = 'p_{T}(2nd leading b-jet cand) (GeV)', texY = 'Number of Events / 20 GeV',
    #  name = 'bjet2_pt', attribute = lambda event, sample: event.b2_pt,
    #  binning=[20,0,400],
    #))
    #
    #plots.append(Plot(
    #    name = "top_cand1_pt", texX = 'p_{T}(t cand1) (GeV)', texY = 'Number of Events / 30 GeV',
    #    attribute = lambda event, sample:event.top1_pt,
    #    binning=[20,0,600],
    #))

    #plots.append(Plot(
    #    name = "top_cand1_pt_coarse", texX = 'p_{T}(t cand1) (GeV)', texY = 'Number of Events / 200 GeV',
    #    attribute = lambda event, sample:event.top1_pt,
    #    binning=[3,0,600],
    #))
    #
    #plots.append(Plot(
    #    name = "top_cand1_pt_2bin", texX = 'p_{T}(t cand1) (GeV)', texY = 'Number of Events / 200 GeV',
    #    attribute = lambda event, sample:event.top1_pt,
    #    binning=[2,0,400],
    #))

    #plots.append(Plot(
    #    name = "top_cand1_mass", texX = 'M(t cand1) (GeV)', texY = 'Number of Events / 15 GeV',
    #    attribute = lambda event, sample:event.top1_mass,
    #    binning=[20,0,300],
    #))

    #plots.append(Plot(
    #    name = "top_cand1_phi", texX = '#phi(t cand1)', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.top1_phi,
    #    binning=[10,-pi,pi],
    #))

    #plots.append(Plot(
    #    name = "top_cand2_pt", texX = 'p_{T}(t cand2) (GeV)', texY = 'Number of Events / 30 GeV',
    #    attribute = lambda event, sample:event.top2_pt,
    #    binning=[20,0,600],
    #))
    #
    #plots.append(Plot(
    #    name = "top_cand2_pt_coarse", texX = 'p_{T}(t cand2) (GeV)', texY = 'Number of Events / 200 GeV',
    #    attribute = lambda event, sample:event.top2_pt,
    #    binning=[3,0,600],
    #))

    #plots.append(Plot(
    #    name = "top_cand2_mass", texX = 'p_{T}(t cand2) (GeV)', texY = 'Number of Events / 15 GeV',
    #    attribute = lambda event, sample:event.top2_mass,
    #    binning=[20,0,300],
    #))

    #plots.append(Plot(
    #    name = "top_cand2_phi", texX = '#phi(t cand1)', texY = 'Number of Events',
    #    attribute = lambda event, sample:event.top2_phi,
    #    binning=[10,-pi,pi],
    #))

    #plots.append(Plot(
    #    name = "mt_1", texX = 'M_{T}(var 1) (GeV)', texY = 'Number of Events / 20 GeV',
    #    attribute = lambda event, sample:event.mt_1,
    #    binning=[20,50,450],
    #))

    #plots.append(Plot(
    #    name = "mt_1_coarse", texX = 'M_{T}(var 1) (GeV)', texY = 'Number of Events / 100 GeV',
    #    attribute = lambda event, sample:event.mt_1,
    #    binning=[5,50,550],
    #))

    #plots.append(Plot(
    #    name = "mt_2", texX = 'M_{T}(var 2) (GeV)', texY = 'Number of Events / 20 GeV',
    #    attribute = lambda event, sample:event.mt_2,
    #    binning=[20,50,450],
    #))

    #plots.append(Plot(
    #    name = "mt_2_coarse", texX = 'M_{T}(var 2) (GeV)', texY = 'Number of Events / 100 GeV',
    #    attribute = lambda event, sample:event.mt_2,
    #    binning=[5,50,550],
    #))

    #plots.append(Plot(
    #    name = "minMLepB", texX = 'min M(l, b-jet) (GeV)', texY = 'Number of Events / 10 GeV',
    #    attribute = lambda event, sample:event.minMLepB,
    #    binning=[15,0,300],
    #))
    
    #plots.append(Plot(
    #    name = "LP_superCoarse", texX = 'L_{P}', texY = 'Number of Events / 0.6',
    #    attribute = lambda event, sample:event.Lp,
    #    binning=[3,-0.6,1.2],
    #))
    
    plots.append(Plot(
        name = "LP_coarse", texX = 'L_{P}', texY = 'Number of Events / 0.2',
        attribute = lambda event, sample:event.Lp,
        binning=[10,-1,1],
    ))
    
    plots.append(Plot(
        name = "LP", texX = 'L_{P}', texY = 'Number of Events / 0.1',
        attribute = lambda event, sample:event.Lp,
        binning=[20,-1,1],
    ))
    
    plots.append(Plot(
        name = "LP_wide", texX = 'L_{P}', texY = 'Number of Events / 0.2',
        attribute = lambda event, sample:event.Lp,
        binning=[25,-2,3],
    ))

    #plots.append(Plot(
    #    name = "deltaPhi_Wl", texX = '#Delta#phi_{W,l}', texY = 'Number of Events / 0.2',
    #    attribute = lambda event, sample:event.deltaPhi_Wl,
    #    binning=[16,0,3.2],
    #))

    #plots.append(Plot(
    #    name = "deltaPhi_Wl_coarse", texX = '#Delta#phi_{W,l}', texY = 'Number of Events / 0.8',
    #    attribute = lambda event, sample:event.deltaPhi_Wl,
    #    binning=[4,0,3.2],
    #))
    #
    #plots.append(Plot(
    #    name = "deltaPhi_tl", texX = '#Delta#phi_{t,l}', texY = 'Number of Events / 0.2',
    #    attribute = lambda event, sample:event.deltaPhi_tl,
    #    binning=[16,0,3.2],
    #))

    #plots.append(Plot(
    #    name = "deltaPhi_tl_coarse", texX = '#Delta#phi_{t,l}', texY = 'Number of Events / 0.8',
    #    attribute = lambda event, sample:event.deltaPhi_tl,
    #    binning=[4,0,3.2],
    #))
    
    #plots.append(Plot(
    #    name = "deltaPhi_tl_topRF", texX = '#Delta#phi_{t,l} in t RF', texY = 'Number of Events / 0.2',
    #    attribute = lambda event, sample:event.deltaPhi_tl_topRF,
    #    binning=[16,0,3.2],
    #))

    #plots.append(Plot(
    #    name = "deltaPhi_tl_topRF_coarse", texX = '#Delta#phi_{t,l} in t RF', texY = 'Number of Events / 0.8',
    #    attribute = lambda event, sample:event.deltaPhi_tl_topRF,
    #    binning=[4,0,3.2],
    #))
    #
    #plots.append(Plot(
    #    name = "deltaR_tl_topRF", texX = '#DeltaR_{t,l} in t RF', texY = 'Number of Events / 0.4',
    #    attribute = lambda event, sample:event.deltaR_tl_topRF,
    #    binning=[10,0,4],
    #))

    #plots.append(Plot(
    #    name = "deltaR_tl_topRF_coarse", texX = '#DeltaR_{t,l} in t RF', texY = 'Number of Events / 1.',
    #    attribute = lambda event, sample:event.deltaR_tl_topRF,
    #    binning=[4,0,4],
    #))

    #plots.append(Plot(
    #    name = "deltaEta_tl_topRF", texX = '#Delta#eta_{t,l} in t RF', texY = 'Number of Events / 0.4',
    #    attribute = lambda event, sample:event.deltaEta_tl_topRF,
    #    binning=[10,0,4],
    #))

    #plots.append(Plot(
    #    name = "deltaEta_tl_topRF_coarse", texX = '#Delta#eta_{t,l} in t RF', texY = 'Number of Events / 1.',
    #    attribute = lambda event, sample:event.deltaEta_tl_topRF,
    #    binning=[4,0,4],
    #))

    #plots.append(Plot(
    #    name = "dPhi_Zl1", texX = '#Delta#phi_{Z,l1}', texY = 'Number of Events / 0.2',
    #    attribute = lambda event, sample:event.dPhi_Zl1,
    #    binning=[16,0,3.2],
    #))

    #plots.append(Plot(
    #    name = "dPhi_Zl2", texX = '#Delta#phi_{Z,l2}', texY = 'Number of Events / 0.2',
    #    attribute = lambda event, sample:event.dPhi_Zl2,
    #    binning=[16,0,3.2],
    #))

    #plots.append(Plot(
    #    name = "dEta_Zl1", texX = '#Delta#eta_{Z,l1}', texY = 'Number of Events / 0.25',
    #    attribute = lambda event, sample:event.dEta_Zl1,
    #    binning=[16,0,4],
    #))

    #plots.append(Plot(
    #    name = "dEta_Zl2", texX = '#Delta#eta_{Z,l2}', texY = 'Number of Events / 0.25',
    #    attribute = lambda event, sample:event.dEta_Zl2,
    #    binning=[16,0,4],
    #))
    
    plots.append(Plot(
        name = "cosThetaStar", texX = 'cos#theta(l-)', texY = 'Number of Events / 0.2',
        attribute = lambda event, sample:event.cosThetaStar,
        binning=[10,-1,1],
    ))
    
    plots.append(Plot(
        name = "cosThetaStar_coarse", texX = 'cos#theta(l-)', texY = 'Number of Events / 0.4',
        attribute = lambda event, sample:event.cosThetaStar,
        binning=[5,-1,1],
    ))
    
    return plots

