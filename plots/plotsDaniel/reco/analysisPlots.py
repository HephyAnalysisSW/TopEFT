#!/usr/bin/env python
''' Analysis script for standard plots
'''
#
# Standard imports and batch mode
#
import ROOT, os
ROOT.gROOT.SetBatch(True)
import itertools

from math                         import sqrt, cos, sin, pi, acos, cosh
from RootTools.core.standard      import *
from TopEFT.Tools.user            import plot_directory
from TopEFT.Tools.helpers         import deltaPhi, getObjDict, getVarValue, deltaR, deltaR2
from TopEFT.Tools.objectSelection import getFilterCut
from TopEFT.Tools.cutInterpreter  import cutInterpreter
from TopEFT.Tools.triggerSelector import triggerSelector

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--signal',             action='store',      default=None,            nargs='?', choices=[None, "ewkDM", "ttZ01j"], help="Add signal to plot")
argParser.add_argument('--onlyTTZ',            action='store_true', default=False,           help="Plot only ttZ")
argParser.add_argument('--noData',             action='store_true', default=False,           help='also plot data?')
argParser.add_argument('--small',                                   action='store_true',     help='Run only on a small subset of the data?', )
argParser.add_argument('--TTZ_LO',                                   action='store_true',     help='Use LO TTZ?', )
argParser.add_argument('--reweightPtZToSM', action='store_true', help='Reweight Pt(Z) to the SM for all the signals?', )
argParser.add_argument('--plot_directory',     action='store',      default='80X_v20')
argParser.add_argument('--selection',          action='store',      default='trilep-Zcand-lepSelTTZ-njet3p-btag1p-onZ')
argParser.add_argument('--normalize',           action='store_true', default=False,             help="Normalize yields" )
argParser.add_argument('--WZpowheg',           action='store_true', default=False,             help="Use WZ powheg sample" )
args = argParser.parse_args()

#
# Logger
#
import TopEFT.Tools.logger as logger
import RootTools.core.logger as logger_rt
logger    = logger.get_logger(   args.logLevel, logFile = None)
logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

if args.small:                        args.plot_directory += "_small"
if args.noData:                       args.plot_directory += "_noData"
if args.signal:                       args.plot_directory += "_signal_"+args.signal
if args.onlyTTZ:                      args.plot_directory += "_onlyTTZ"
if args.TTZ_LO:                       args.plot_directory += "_TTZ_LO"
if args.WZpowheg:                     args.plot_directory += "_WZpowheg"
if args.normalize: args.plot_directory += "_normalize"
if args.reweightPtZToSM: args.plot_directory += "_reweightPtZToSM"
#
# Make samples, will be searched for in the postProcessing directory
#
data_directory = "/afs/hephy.at/data/rschoefbeck01/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_v20/trilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *
data_directory = "/afs/hephy.at/data/rschoefbeck01/cmgTuples/"
postProcessing_directory = "TopEFT_PP_2016_v20/trilep/"
from TopEFT.samples.cmgTuples_Data25ns_80X_03Feb_postProcessed import *

data_directory = "/afs/hephy.at/data/rschoefbeck01/cmgTuples/"
if args.signal == "ttZ01j":
    postProcessing_directory = "TopEFT_PP_v14/trilep/"
    from TopEFT.samples.cmgTuples_signals_Summer16_mAODv2_postProcessed import *

    ewkDM_30    = ewkDM_TTZToLL_LO
    ewkDM_31    = ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2

    ewkDM_30.style = styles.lineStyle( ROOT.kBlack, width=3, errors = True )
    ewkDM_31.style = styles.lineStyle( ROOT.kMagenta, width=3, errors = True )

    signals = [ewkDM_30, ewkDM_31]

elif args.signal == "ewkDM":
    data_directory = '/afs/hephy.at/data/rschoefbeck02/cmgTuples/'
    postProcessing_directory = "TopEFT_PP_v12/trilep/"
    from TopEFT.samples.cmgTuples_ttZ0j_Summer16_mAODv2_postProcessed import *
    
    SM          = ttZ0j_ll
    
    current1    = ttZ0j_ll_DC1A_1p000000
    current2    = ttZ0j_ll_DC1A_0p500000_DC1V_0p500000
    current3    = ttZ0j_ll_DC1A_0p500000_DC1V_m1p000000
    
    SM.style       = styles.lineStyle( ROOT.kBlack, width=3, errors = True )
    current1.style = styles.lineStyle( ROOT.kMagenta, width=3, errors = True )
    current2.style = styles.lineStyle( ROOT.kBlue, width=3, errors = True )
    current3.style = styles.lineStyle( ROOT.kGreen+1, width=3, errors = True )
 
    dipole1     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700
    dipole2     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700
    dipole3     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700
    dipole4     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700
    dipole5     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000
    dipole6     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000
    dipole7     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000
    dipole8     = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000
    
    dipoles = [ dipole1, dipole2, dipole3, dipole4, dipole5, dipole6, dipole7, dipole8 ]
    
    colors = [ ROOT.kMagenta+1, ROOT.kOrange, ROOT.kBlue, ROOT.kCyan+1, ROOT.kGreen+1, ROOT.kRed, ROOT.kViolet, ROOT.kYellow+2 ]
    for i, dipole in enumerate(dipoles):
        dipole.style = styles.lineStyle( colors[i], width=3 )
    
    #signals = [SM, current1, current2, current3]
    signals = [SM] + dipoles 

else:
    signals = []

#
# Text on the plots
#
def drawObjects( plotData, dataMCScale, lumi_scale ):
    tex = ROOT.TLatex()
    tex.SetNDC()
    tex.SetTextSize(0.04)
    tex.SetTextAlign(11) # align right
    lines = [
      (0.15, 0.95, 'CMS Preliminary' if plotData else 'CMS Simulation'), 
      (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV) Scale %3.2f'% ( lumi_scale, dataMCScale ) ) if plotData else (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV)' % lumi_scale)
    ]
    return [tex.DrawLatex(*l) for l in lines] 

scaling = { i+1:0 for i in range(len(signals)) }

def drawPlots(plots, mode, dataMCScale):
  for log in [False, True]:
    plot_directory_ = os.path.join(plot_directory, 'analysisPlots', args.plot_directory, mode + ("_log" if log else ""), args.selection)
    for plot in plots:
      if not max(l[0].GetMaximum() for l in plot.histos): continue # Empty plot
      if not args.noData: 
        if mode == "all": plot.histos[1][0].legendText = "Data"
        if mode == "SF":  plot.histos[1][0].legendText = "Data (SF)"
      extensions_ = ["pdf", "png", "root"] if mode == 'all' else ['png']

      plotting.draw(plot,
	    plot_directory = plot_directory_,
        extensions = extensions_,
	    ratio = {'yRange':(0.1,1.9)} if not args.noData else {},
	    logX = False, logY = log, sorting = True,
	    yRange = (0.03, "auto") if log else (0.001, "auto"),
	    scaling = scaling if args.normalize else {},
	    legend = [ (0.15,0.9-0.03*sum(map(len, plot.histos)),0.9,0.9), 2],
	    drawObjects = drawObjects( not args.noData, dataMCScale , lumi_scale ),
        copyIndexPHP = True,
      )

# define 3l selections
def getLeptonSelection( mode ):
    if   mode=="mumumu": return "nGoodMuons==3&&nGoodElectrons==0"
    elif mode=="mumue":  return "nGoodMuons==2&&nGoodElectrons==1"
    elif mode=="muee":   return "nGoodMuons==1&&nGoodElectrons==2"
    elif mode=="eee":    return "nGoodMuons==0&&nGoodElectrons==3"
    elif mode=='all':    return "nGoodMuons+nGoodElectrons==3"

# reweighting 
if args.reweightPtZToSM:
    sel_string = "&&".join([getFilterCut(isData=False), getLeptonSelection('all'), cutInterpreter.cutString(args.selection)])
    TTZ_ptZ = TTZtoLLNuNu.get1DHistoFromDraw("Z_pt", [20,0,1000], selectionString = sel_string, weightString="weight")
    TTZ_ptZ.Scale(1./TTZ_ptZ.Integral())

    def get_reweight( var, histo ):

        def reweight(event, sample):
            i_bin = histo.FindBin(getattr( event, var ) )
            return histo.GetBinContent(i_bin)

        return reweight

    for signal in signals:
        logger.info( "Computing PtZ reweighting for signal %s", signal.name )
        signal_ptZ = signal.get1DHistoFromDraw("Z_pt", [20,0,1000], selectionString = sel_string, weightString="weight")
        signal_ptZ.Scale(1./signal_ptZ.Integral())

        signal.reweight_ptZ_histo = TTZ_ptZ.Clone()
        signal.reweight_ptZ_histo.Divide(signal_ptZ)

        signal.weight = get_reweight( "Z_pt", signal.reweight_ptZ_histo )


#
# Read variables and sequences
#
read_variables =    ["weight/F",
                    "jet[pt/F,eta/F,phi/F,btagCSV/F,DFb/F,DFbb/F,id/I]", "njet/I","nJetSelected/I",
                    "lep[pt/F,eta/F,phi/F,pdgId/I]", "nlep/I",
                    "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I", 
                    "Z_l1_index/I", "Z_l2_index/I", "nonZ_l1_index/I", "nonZ_l2_index/I", 
                    "Z_phi/F","Z_pt/F", "Z_mass/F", "Z_eta/F","Z_lldPhi/F", "Z_lldR/F"
                    ]

sequence = []

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

sequence += [ getSelectedJets ]
#sequence += [ getAllJets, getForwardJets, getForwardJets_eta3, getForwardJetEta]

MW = 80.385
Mt = 172.5

sequence += [ getDPhiZLep, getDPhiZJet,getJets ]

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

#sequence += [ getCPVars ]

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

sequence.append( getL )

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
    
#sequence.append( reconstructLeptonicTop )

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

sequence.append( getCosThetaStar )

def getM3l( event, sample ):
    # get the invariant mass of the 3l system
    l = []
    for i in range(3):
        l.append(ROOT.TLorentzVector())
        l[i].SetPtEtaPhiM(event.lep_pt[i], event.lep_eta[i], event.lep_phi[i],0)
    event.threelmass = (l[0] + l[1] + l[2]).M()

sequence.append( getM3l )

def getLeptonSelection( mode ):
  if   mode=="mumumu": return "nGoodMuons==3&&nGoodElectrons==0"
  elif mode=="mumue":  return "nGoodMuons==2&&nGoodElectrons==1"
  elif mode=="muee":   return "nGoodMuons==1&&nGoodElectrons==2"
  elif mode=="eee":    return "nGoodMuons==0&&nGoodElectrons==3"

#
# Loop over channels
#
yields     = {}
allPlots   = {}
allModes   = ['mumumu','mumue','muee', 'eee']
for index, mode in enumerate(allModes):
    yields[mode] = {}
    if not args.noData:
        data_sample = Run2016
        data_sample.texName = "data"

        data_sample.setSelectionString([getFilterCut(isData=True), getLeptonSelection(mode)])
        data_sample.name           = "data"
        data_sample.read_variables = ["evt/I","run/I"]
        data_sample.style          = styles.errorStyle(ROOT.kBlack)
        lumi_scale                 = data_sample.lumi/1000

    if args.noData: lumi_scale = 35.9
    weight_ = lambda event, sample: event.weight

    if args.TTZ_LO:
        TTZ_mc = TTZ_LO
    else:
        TTZ_mc = TTZtoLLNuNu

    if args.onlyTTZ:
        mc = [ TTZ_mc ]
    else:
        if args.WZpowheg:
            mc             = [ TTZ_mc , TTW, TZQ, TTX, WZ_powheg, rare, TTLep_pow, DY_HT_LO, singleTop ]
        else:
            mc             = [ TTZ_mc , TTW, TZQ, TTX, WZ_amcatnlo, rare, TTLep_pow, DY_HT_LO, singleTop ]

    for sample in mc: sample.style = styles.fillStyle(sample.color)

    for sample in mc + signals:
      sample.scale          = lumi_scale
      #sample.read_variables = ['reweightTopPt/F','reweightDilepTriggerBackup/F','reweightLeptonSF/F','reweightBTag_SF/F','reweightPU36fb/F', 'nTrueInt/F', 'reweightLeptonTrackingSF/F']
      #sample.weight         = lambda event, sample: event.reweightTopPt*event.reweightBTag_SF*event.reweightLeptonSF*event.reweightDilepTriggerBackup*event.reweightPU36fb*event.reweightLeptonTrackingSF
      sample.read_variables = ['reweightBTagCSVv2_SF/F', 'reweightBTagDeepCSV_SF/F', 'reweightPU36fb/F']
      sample.weight         = lambda event, sample: event.reweightBTagDeepCSV_SF*event.reweightPU36fb
      tr = triggerSelector(2016)
      sample.setSelectionString([getFilterCut(isData=False), getLeptonSelection(mode), tr.getSelection("MC")])

    if not args.noData:
      stack = Stack(mc, data_sample)
    else:
      stack = Stack(mc)

    stack.extend( [ [s] for s in signals ] )

    if args.small:
        for sample in stack.samples:
            sample.reduceFiles( to = 1 )

    # Use some defaults
    Plot.setDefaults(stack = stack, weight = weight_, selectionString = cutInterpreter.cutString(args.selection), addOverFlowBin='upper')

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
    
    plotting.fill(plots, read_variables = read_variables, sequence = sequence)

    # Get normalization yields from yield histogram
    for plot in plots:
      if plot.name == "yield":
        for i, l in enumerate(plot.histos):
          for j, h in enumerate(l):
            yields[mode][plot.stack[i][j].name] = h.GetBinContent(h.FindBin(0.5+index))
            h.GetXaxis().SetBinLabel(1, "#mu#mu#mu")
            h.GetXaxis().SetBinLabel(2, "#mu#mue")
            h.GetXaxis().SetBinLabel(3, "#muee")
            h.GetXaxis().SetBinLabel(4, "eee")
    if args.noData: yields[mode]["data"] = 0

    yields[mode]["MC"] = sum(yields[mode][s.name] for s in mc)
    dataMCScale        = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')

    drawPlots(plots, mode, dataMCScale)
    allPlots[mode] = plots

# Add the different channels into SF and all
for mode in ["comb1","comb2","all"]:
    yields[mode] = {}
    for y in yields[allModes[0]]:
        try:    yields[mode][y] = sum(yields[c][y] for c in ['eee','muee','mumue', 'mumumu'])
        except: yields[mode][y] = 0
    dataMCScale = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')
    
    for plot in allPlots['mumumu']:
        if mode=="comb1":
            tmp = allPlots['mumue']
        elif mode=="comb2":
            tmp = allPlots['muee']
        else:
            tmp = allPlots['eee']
        for plot2 in (p for p in tmp if p.name == plot.name):
            for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
                for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
                    if i==k:
                        j.Add(l)
    
    if mode == "all": drawPlots(allPlots['mumumu'], mode, dataMCScale)

logger.info( "Done with prefix %s and selectionString %s", args.selection, cutInterpreter.cutString(args.selection) )

