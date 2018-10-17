#!/usr/bin/env python
''' plotList ttG
'''
import ROOT, os
ROOT.gROOT.SetBatch(True)
import itertools

from math                         import sqrt, cos, sin, pi, acos, cosh
from RootTools.core.standard      import *
from TopEFT.Tools.helpers         import deltaPhi, getObjDict, getCollection, getVarValue, deltaR, deltaR2, m3
from plot_helpers                 import *

#
# ttG Variables
#
def ttGVariables():
    ''' return read_variables list for ttG 1l and 2l plots
    '''

    read_variables = ["weight/F",
                      "jet[pt/F,eta/F,phi/F,btagCSV/F,DFb/F,DFbb/F,id/I]", "njet/I","nJetSelected/I",
                      "lep[pt/F,eta/F,phi/F,pdgId/I]", "nlep/I",
                      "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I",
                      #"Z_l1_index/I", "Z_l2_index/I", "nonZ_l1_index/I", "nonZ_l2_index/I",
                      "gamma_phi/F","gamma_pt/F", "gamma_eta/F",#"Z_lldPhi/F", "Z_lldR/F"
                      "Z_pt/F"
                      ]

    return read_variables

#
# ttG Sequence functions
#

def getJets( event, sample ):
    jetVars             = ['eta','pt','phi','btagCSV','DFbb', 'DFb', 'id']
    event.allJets       = getCollection( event, 'jet', jetVars, 'njet' )
    event.allJets.sort( key = lambda j:-j['pt'] )
    event.selectedJets  = list( filter( lambda j: isGoodJet(j), event.allJets ) )

    for p in event.selectedJets:
        addTransverseVector( p )
        addTLorentzVector( p )

    event.jets_sortbtag = event.selectedJets
    event.jets_sortbtag.sort( key = lambda l:-l['btagCSV'] )

def getM3j( event, sample ):
    # get the invariant mass of the 3j system
    event.m3, tmp1, tmp2, tmp3 = m3( event.selectedJets )

def getForwardJets( event, sample ):
    event.jetForward30  = list( filter( lambda j: j['pt']>30 and abs(j['eta'])>2.4, event.allJets ) )
    event.jetForward40  = list( filter( lambda j: j['pt']>40, event.jetForward30 ) )
    event.jetForward50  = list( filter( lambda j: j['pt']>50, event.jetForward40 ) )
    event.jetForward60  = list( filter( lambda j: j['pt']>60, event.jetForward50 ) )
    event.jetForward70  = list( filter( lambda j: j['pt']>70, event.jetForward60 ) )

def getForwardJets_eta3( event, sample ):
    event.jetForward30_eta3  = list( filter( lambda j: j['pt']>30 and abs(j['eta'])>3.0, event.allJets ) )
    event.jetForward40_eta3  = list( filter( lambda j: j['pt']>40, event.jetForward30 ) )
    event.jetForward50_eta3  = list( filter( lambda j: j['pt']>50, event.jetForward40 ) )
    event.jetForward60_eta3  = list( filter( lambda j: j['pt']>60, event.jetForward50 ) )
    event.jetForward70_eta3  = list( filter( lambda j: j['pt']>70, event.jetForward60 ) )

def getLeps( event, sample ):
    lepVars             = ['eta','pt','phi','charge', 'pdgId', 'sourceId','mediumMuonId']
    event.allLeps       = getCollection( event, 'lep', lepVars, 'nlep' )
    event.allLeps.sort( key = lambda l:-l['pt'] )
    event.lepLoose      = list( filter( lambda j: isGoodLooseLepton(j), event.allLeps ) )

    for p in event.lepLoose:
        addTransverseVector( p )
        addTLorentzVector( p )

    event.selectedLeps  = list( filter( lambda j: isGoodLepton(j), event.lepLoose ) )

def getPhotons( event, sample ):
    photonList = [ 'pt', 'eta', 'phi' ]
    event.gammas = getCollection( event, 'gamma', photonList, 'ngamma' )
    event.gammas = list( filter( lambda p: isGoodPhoton(p), event.gammas ) )
    event.gammas.sort( key = lambda p:-p['pt'] )

    for p in event.gammas:
        addTransverseVector( p )
        addTLorentzVector( p )

def getMll( event, sample ):
    # get the invariant mass of the 2l(+gamma) system 
    event.mll      = (event.selectedLeps[0]['vec4D'] + event.selectedLeps[1]['vec4D']).M()
#    event.mllgamma = (event.selectedLeps[0]['vec4D'] + event.selectedLeps[1]['vec4D'] + event.gammas[0]['vec4D']).M()

def getMET( event, sample ):
    ''' Make a MET vector to facilitate further calculations
    '''
    event.MET = {'pt':event.met_pt, 'phi':event.met_phi}
    addTransverseVector( event.MET )

def getW( event, sample ):
    # get the W boson candidate
    event.W           = {'vec2D':event.selectedLeps[0]['vec2D'] + event.MET['vec2D']}
    event.W['pt']     = event.W['vec2D'].Mod()
    event.W['phi']    = acos(event.W['vec2D'].X() / event.W['pt'])
    event.deltaPhi_Wl = deltaPhi(event.W['phi'], event.selectedLeps[0]['phi'])

def getL( event, sample ):
    # calculate Lp
    event.Lp = ( event.W['vec2D']*event.selectedLeps[0]['vec2D'] ) / ( event.W['vec2D']*event.W['vec2D'] )


#
# ttG Sequence
#

def ttG1lSequence():
    ''' return sequence list for ttG 1l plots
    '''

    sequence = []

    sequence.append( getJets )
#    sequence.append( getM3j )
    sequence.append( getForwardJets )
    sequence.append( getForwardJets_eta3 )
    sequence.append( getLeps )
#    sequence.append( getPhotons )
    sequence.append( getMET )
    sequence.append( getW ) #only for 1l ttgamma
    sequence.append( getL ) #only for 1l ttgamma

    return sequence

def ttG2lSequence():
    ''' return sequence list for ttG 2l plots
    '''

    sequence = []

    sequence.append( getJets )
#    sequence.append( getM3j )
    sequence.append( getForwardJets )
    sequence.append( getForwardJets_eta3 )
    sequence.append( getLeps )
#    sequence.append( getPhotons )
    sequence.append( getMll )
    sequence.append( getMET )

    return sequence


#
# ttG Plots
#

def ttG1lPlots( index ):
    ''' return plot list for ttG 1l plots
    '''

    plots = []
    
    plots.append(Plot(
        name = 'yield',
        texX = 'yield', texY = 'Number of Events',
        attribute = lambda event, sample: 0.5 + index,
        binning=[2, 0, 2],
    ))
    
    plots.append(Plot(
        name = 'nVtxs',
        texX = 'vertex multiplicity', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "nVert/I" ),
        binning=[50,0,50],
    ))
    
    plots.append(Plot(
        name = "MET",
        texX = 'E_{T}^{miss} (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "met_pt/F" ),
        binning=[400/20,0,400],
    ))
    
    plots.append(Plot(
        name = "MET_phi",
        texX = '#phi(E_{T}^{miss})', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "met_phi/F" ),
        binning=[10,-pi,pi],
    ))
    
#    plots.append(Plot(
#        name = 'Gamma_pt', texX = 'p_{T}(#gamma) (GeV)', texY = 'Number of Events / 20 GeV',
#        attribute = TreeVariable.fromString( "gamma_pt/F" ),
#        binning=[20,0,400],
#    ))
    
#    plots.append(Plot(
#        name = 'Gamma_pt_coarse', texX = 'p_{T}(#gamma) (GeV)', texY = 'Number of Events / 50 GeV',
#        attribute = TreeVariable.fromString( "gamma_pt/F" ),
#        binning=[16,0,800],
#    ))
    
#    plots.append(Plot(
#        name = 'Gamma_pt_superCoarse', texX = 'p_{T}(#gamma) (GeV)', texY = 'Number of Events',
#        attribute = TreeVariable.fromString( "gamma_pt/F" ),
#        binning=[3,0,600],
#    ))
    
#    plots.append(Plot(
#        name = 'Gamma_pt_analysis', texX = 'p_{T}(#gamma) (GeV)', texY = 'Number of Events / 100 GeV',
#        attribute = TreeVariable.fromString( "gamma_pt/F" ),
#        binning=[4,0,400],
#    ))
    
#    plots.append(Plot(
#        name = 'l0gammaDPhi',
#        texX = '#Delta#Phi(l_{0},#gamma)', texY = 'Number of Events',
#        attribute = lambda event, sample: deltaPhi(event.selectedLeps[0]['phi'], event.gammas[0]['phi']),
#        binning=[20,0,pi],
#    ))

#    plots.append(Plot(
#        name = 'l0gammaDR',
#        texX = '#Delta R(l_{0},#gamma)', texY = 'Number of Events',
#        attribute = lambda event, sample: deltaR(event.selectedLeps[0], event.gammas[0]),
#        binning=[20,0.3,3],
#    ))

    plots.append(Plot(
        name = "W_phi",
        texX = '#phi(W_{lep})', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample: event.W['phi'],
        binning=[10,-pi,pi],
    ))
    
    plots.append(Plot(
        name = "W_pt",
        texX = 'p_{T}(W_{lep}) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample: event.W['pt'],
        binning=[20,0,400],
    ))
    
    plots.append(Plot(
        name = "M3",
        texX = 'M_{3} (GeV)', texY = 'Number of Events',
        attribute = lambda event, sample:m3( event.selectedJets )[0] if len(event.selectedJets)>2 else float('nan'),
        binning=[25,0,500],
    ))

    plots.append(Plot(
        name = "nForwardJet_Pt30_eta3",
        texX = 'nJet p_{T}(j)>30 GeV', texY = 'Number of Events',
        attribute = lambda event, sample: len(event.jetForward30_eta3),
        binning=[10,0,10],
    ))
    
    plots.append(Plot(
        name = "nForwardJet_Pt40_eta3",
        texX = 'nJet p_{T}(j)>40 GeV', texY = 'Number of Events',
        attribute = lambda event, sample: len(event.jetForward40_eta3),
        binning=[10,0,10],
    ))

    plots.append(Plot(
        name = "nForwardJet_Pt50_eta3",
        texX = 'nJet p_{T}(j)>50 GeV', texY = 'Number of Events',
        attribute = lambda event, sample: len(event.jetForward50_eta3),
        binning=[10,0,10],
    ))

    plots.append(Plot(
        name = "nForwardJet_Pt60_eta3",
        texX = 'nJet p_{T}(j)>60 GeV', texY = 'Number of Events',
        attribute = lambda event, sample: len(event.jetForward60_eta3),
        binning=[10,0,10],
    ))

    plots.append(Plot(
        name = "nForwardJet_Pt70_eta3",
        texX = 'nJet p_{T}(j)>70 GeV', texY = 'Number of Events',
        attribute = lambda event, sample: len(event.jetForward70_eta3),
        binning=[10,0,10],
    ))
    
    plots.append(Plot(
      name = "nJets",
      texX = 'N_{jets}', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nJetSelected/I" ), #nJetSelected
      binning=[8,-0.5,7.5],
    ))
    
    plots.append(Plot(
      name = "nBJets",
      texX = 'N_{b-tag}', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nBTag/I" ), #nJetSelected
      binning=[4,-0.5,3.5],
    ))
    
    plots.append(Plot(
      name = "nLepLoose",
      texX = 'N_{l, loose}', texY = 'Number of Events',
      attribute = lambda event, sample: len(event.lepLoose),
      binning=[3,-0.5,2.5],
    ))
    
    plots.append(Plot(
      name = "nLep",
      texX = 'N_{lep}', texY = 'Number of Events',
      attribute = lambda event, sample: len(event.selectedLeps),
      binning=[3,-0.5,2.5],
    ))
    
    plots.append(Plot(
      texX = 'p_{T}(leading l) (GeV)', texY = 'Number of Events / 20 GeV',
      name = 'lep1_pt', attribute = lambda event, sample: event.selectedLeps[0]['pt'],
      binning=[400/20,0,400],
    ))

    plots.append(Plot(
      texX = 'p_{T}(leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
      name = 'jet1_pt', attribute = lambda event, sample: event.selectedJets[0]['pt'],
      binning=[600/30,0,600],
    ))
    
    plots.append(Plot(
      texX = 'p_{T}(2nd leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
      name = 'jet2_pt', attribute = lambda event, sample: event.selectedJets[1]['pt'],
      binning=[600/30,0,600],
    ))

    plots.append(Plot(
      texX = 'p_{T}(leading b-jet cand) (GeV)', texY = 'Number of Events / 20 GeV',
      name = 'bjet1_pt', attribute = lambda event, sample: event.jets_sortbtag[0]['pt'],
      binning=[20,0,400],
    ))

    plots.append(Plot(
      texX = 'p_{T}(2nd leading b-jet cand) (GeV)', texY = 'Number of Events / 20 GeV',
      name = 'bjet2_pt', attribute = lambda event, sample: event.jets_sortbtag[1]['pt'],
      binning=[20,0,400],
    ))
    
    plots.append(Plot(
      name = 'deltaPhi_bb',
      texX = '#Delta#phi(bb)', texY = 'Number of Events',
      attribute = lambda event, sample: deltaPhi( event.jets_sortbtag[0]['phi'], event.jets_sortbtag[1]['phi'] ),
      binning=[20,0,pi],
    ))

    plots.append(Plot(
      name = 'deltaR_bb',
      texX = '#DeltaR(bb)', texY = 'Number of Events',
      attribute = lambda event, sample: deltaR( event.jets_sortbtag[0], event.jets_sortbtag[1] ),
      binning=[20,0,6],
    ))

    return plots

def ttG2lPlots( index ):
    ''' return plot list for ttG 2l plots
    '''

    plots = []
    
    plots.append(Plot(
      name = 'yield', texX = 'yield', texY = 'Number of Events',
      attribute = lambda event, sample: 0.5 + index,
      binning=[3, 0, 3],
    ))
    
    plots.append(Plot(
      name = 'nVtxs', texX = 'vertex multiplicity', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nVert/I" ),
      binning=[50,0,50],
    ))
    
    plots.append(Plot(
        name = 'MET', texX = 'E_{T}^{miss} (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "met_pt/F" ),
        binning=[400/20,0,400],
    ))
    
    plots.append(Plot(
        name = 'MET_phi', texX = '#phi(E_{T}^{miss})', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "met_phi/F" ),
        binning=[10,-pi,pi],
    ))
    
#    plots.append(Plot(
#        name = 'Gamma_pt', texX = 'p_{T}(#gamma) (GeV)', texY = 'Number of Events / 20 GeV',
#        attribute = TreeVariable.fromString( "gamma_pt/F" ),
#        binning=[20,0,400],
#    ))
    
#    plots.append(Plot(
#        name = 'Gamma_pt_coarse', texX = 'p_{T}(#gamma) (GeV)', texY = 'Number of Events / 50 GeV',
#        attribute = TreeVariable.fromString( "gamma_pt/F" ),
#        binning=[16,0,800],
#    ))
    
#    plots.append(Plot(
#        name = 'Gamma_pt_superCoarse', texX = 'p_{T}(#gamma) (GeV)', texY = 'Number of Events',
#        attribute = TreeVariable.fromString( "gamma_pt/F" ),
#        binning=[3,0,600],
#    ))
    
#    plots.append(Plot(
#        name = 'Gamma_pt_analysis', texX = 'p_{T}(#gamma) (GeV)', texY = 'Number of Events / 100 GeV',
#        attribute = TreeVariable.fromString( "gamma_pt/F" ),
#        binning=[4,0,400],
#    ))
    
#    plots.append(Plot(
#        name = 'l0gammaDPhi',
#        texX = '#Delta#Phi(l_{0},#gamma)', texY = 'Number of Events',
#        attribute = lambda event, sample: deltaPhi(event.selectedLeps[0]['phi'], event.gammas[0]['phi']),
#        binning=[20,0,pi],
#    ))

#    plots.append(Plot(
#        name = 'l0gammaDR',
#        texX = '#Delta R(l_{0},#gamma)', texY = 'Number of Events',
#        attribute = lambda event, sample: deltaR(event.selectedLeps[0], event.gammas[0]),
#        binning=[20,0.3,3],
#    ))

    plots.append(Plot(
        name = "M3",
        texX = 'M_{3} (GeV)', texY = 'Number of Events',
        attribute = lambda event, sample: m3(event.selectedJets)[0] if len(event.selectedJets)>2 else float('nan'),
        binning=[25,0,500],
    ))
   
    plots.append(Plot(
        name = "dRll",
        texX = '#Delta R(ll)', texY = 'Number of Events',
        attribute = lambda event, sample: deltaR( event.selectedJets[0], event.selectedJets[1] ),
        binning=[20,0.3,3],
    ))

    plots.append(Plot(
        name = "dPhill",
        texX = '#Delta#phi(ll)', texY = 'Number of Events',
        attribute = lambda event, sample: deltaPhi( event.selectedJets[0]['phi'], event.selectedJets[1]['phi'] ),
        binning=[10,0,pi],
    ))

    plots.append(Plot(
        name = "nForwardJet_Pt30_eta3",
        texX = 'nJet p_{T}(j)>30 GeV', texY = 'Number of Events',
        attribute = lambda event, sample: len(event.jetForward30_eta3),
        binning=[10,0,10],
    ))
    
    plots.append(Plot(
        name = "nForwardJet_Pt40_eta3",
        texX = 'nJet p_{T}(j)>40 GeV', texY = 'Number of Events',
        attribute = lambda event, sample: len(event.jetForward40_eta3),
        binning=[10,0,10],
    ))

    plots.append(Plot(
        name = "nForwardJet_Pt50_eta3",
        texX = 'nJet p_{T}(j)>50 GeV', texY = 'Number of Events',
        attribute = lambda event, sample: len(event.jetForward50_eta3),
        binning=[10,0,10],
    ))

    plots.append(Plot(
        name = "nForwardJet_Pt60_eta3",
        texX = 'nJet p_{T}(j)>60 GeV', texY = 'Number of Events',
        attribute = lambda event, sample: len(event.jetForward60_eta3),
        binning=[10,0,10],
    ))

    plots.append(Plot(
        name = "nForwardJet_Pt70_eta3",
        texX = 'nJet p_{T}(j)>70 GeV', texY = 'Number of Events',
        attribute = lambda event, sample: len(event.jetForward70_eta3),
        binning=[10,0,10],
    ))
    
    plots.append(Plot(
        name = "M_ll", texX = 'M(ll) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.mll,
        binning=[20,0,200],
    ))

    plots.append(Plot(
        name = "M_ll_coarse", texX = 'M(ll) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = lambda event, sample:event.mll,
        binning=[10,0,200],
    ))

#    plots.append(Plot(
#        name = "M_llgamma", texX = 'M(ll#gamma) (GeV)', texY = 'Number of Events / 10 GeV',
#        attribute = lambda event, sample:event.mllgamma,
#        binning=[20,0,200],
#    ))

#    plots.append(Plot(
#        name = "M_llgamma_coarse", texX = 'M(ll#gamma) (GeV)', texY = 'Number of Events / 20 GeV',
#        attribute = lambda event, sample:event.mllgamma,
#        binning=[10,0,200],
#    ))

    plots.append(Plot(
      name = "nJets",
      texX = 'N_{jets}', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nJetSelected/I" ), #nJetSelected
      binning=[8,-0.5,7.5],
    ))
    
    plots.append(Plot(
      name = "nBJets",
      texX = 'N_{b-tag}', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nBTag/I" ), #nJetSelected
      binning=[4,-0.5,3.5],
    ))
    
    plots.append(Plot(
      name = "nLepLoose",
      texX = 'N_{l, loose}', texY = 'Number of Events',
      attribute = lambda event, sample: len(event.lepLoose),
      binning=[3,-0.5,2.5],
    ))
    
    plots.append(Plot(
      name = "nLep",
      texX = 'N_{lep}', texY = 'Number of Events',
      attribute = lambda event, sample: len(event.selectedLeps),
      binning=[3,-0.5,2.5],
    ))
    
    plots.append(Plot(
      texX = 'p_{T}(leading l) (GeV)', texY = 'Number of Events / 20 GeV',
      name = 'lep1_pt', attribute = lambda event, sample: event.selectedLeps[0]['pt'],
      binning=[400/20,0,400],
    ))

    plots.append(Plot(
      texX = 'p_{T}(subleading l) (GeV)', texY = 'Number of Events / 10 GeV',
      name = 'lep2_pt', attribute = lambda event, sample: event.selectedLeps[1]['pt'],
      binning=[200/10,0,200],
    ))

    plots.append(Plot(
      texX = 'p_{T}(leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
      name = 'jet1_pt', attribute = lambda event, sample: event.selectedJets[0]['pt'],
      binning=[600/30,0,600],
    ))
    
    plots.append(Plot(
      texX = 'p_{T}(2nd leading jet) (GeV)', texY = 'Number of Events / 30 GeV',
      name = 'jet2_pt', attribute = lambda event, sample: event.selectedJets[1]['pt'],
      binning=[600/30,0,600],
    ))

    plots.append(Plot(
      texX = 'p_{T}(leading b-jet cand) (GeV)', texY = 'Number of Events / 20 GeV',
      name = 'bjet1_pt', attribute = lambda event, sample: event.jets_sortbtag[0]['pt'],
      binning=[20,0,400],
    ))

    plots.append(Plot(
      texX = 'p_{T}(2nd leading b-jet cand) (GeV)', texY = 'Number of Events / 20 GeV',
      name = 'bjet2_pt', attribute = lambda event, sample: event.jets_sortbtag[1]['pt'],
      binning=[20,0,400],
    ))
    
    plots.append(Plot(
      name = 'deltaPhi_bb',
      texX = '#Delta#phi(bb)', texY = 'Number of Events',
      attribute = lambda event, sample: deltaPhi( event.jets_sortbtag[0]['phi'], event.jets_sortbtag[1]['phi'] ),
      binning=[20,0,pi],
    ))

    plots.append(Plot(
      name = 'deltaR_bb',
      texX = '#DeltaR(bb)', texY = 'Number of Events',
      attribute = lambda event, sample: deltaR( event.jets_sortbtag[0], event.jets_sortbtag[1] ),
      binning=[20,0,6],
    ))

    return plots

