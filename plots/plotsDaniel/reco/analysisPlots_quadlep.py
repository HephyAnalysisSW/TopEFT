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
from TopEFT.samples.color         import color

# for mt2ll
from TopEFT.Tools.mt2Calculator              import mt2Calculator
mt2Calc = mt2Calculator()

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
argParser.add_argument('--reweightPtZToSM',     action='store_true', help='Reweight Pt(Z) to the SM for all the signals?', )
argParser.add_argument('--plot_directory',      action='store',      default='80X_mva_v7')
argParser.add_argument('--selection',           action='store',      default='quadlep-lepSelQuad-njet0p-btag0-onZZ')  # quadlep-lepSelQuad-njet2p-btag0p-onZ1-offZ2 or quadlep-lepSelQuad-njet2p-btag1p-onZ1-offZ2 for signal regions
argParser.add_argument('--normalize',           action='store_true', default=False,             help="Normalize yields" )
argParser.add_argument('--WZpowheg',            action='store_true', default=False,             help="Use WZ powheg sample" )
argParser.add_argument('--WZmllmin01',          action='store_true', default=False,             help="Use WZ mllmin01 sample" )
argParser.add_argument('--DYincl',              action='store_true', default=False,             help="Use inclusive DY sample (for dilep)" )
argParser.add_argument('--year',                action='store',      default=2016,   type=int,  help="Which year?" )
args = argParser.parse_args()


# PU reweighting on the fly
from TopEFT.Tools.puProfileCache    import puProfile
from TopEFT.Tools.puReweighting     import getReweightingFunction
from TopEFT.samples.helpers         import fromHeppySample
WZTo3LNu_fxfx = fromHeppySample("WZTo3LNu_fxfx", data_path = "/a/b/c", maxN = None, MCgeneration="Fall17")

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
if args.WZmllmin01:                   args.plot_directory += "_WZmllmin01"
if args.normalize: args.plot_directory += "_normalize"
if args.reweightPtZToSM: args.plot_directory += "_reweightPtZToSM"
#
# Make samples, will be searched for in the postProcessing directory
#

if args.year == 2016:
    data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
    postProcessing_directory = "TopEFT_PP_2016_mva_v7/trilep/"
    from TopEFT.samples.cmgTuples_Data25ns_80X_03Feb_postProcessed import *
    data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
    postProcessing_directory = "TopEFT_PP_2016_mva_v7/trilep/"
    dirs = {}
    dirs['TTZ']     = ['TTZToLLNuNu_ext']
    dirs['ZZ']      = ['ZZTo4L']
    dirs['rare']    = ['WWW', 'WWZ', 'WZZ', 'ZZZ']


else:
    data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
    postProcessing_directory = "TopEFT_PP_2017_mva_v7/trilep/"
    from TopEFT.samples.cmgTuples_Data25ns_94X_Run2017_postProcessed import *
    # load MC from here for now
    data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
    postProcessing_directory = "TopEFT_PP_2017_mva_v7/trilep/"
    dirs = {}
    dirs['TTZ']     = ['TTZToLLNuNu_amc']
    dirs['ZZ']      = ['ZZTo4L_comb']
    dirs['rare']    = ['WWW_4F', 'WWZ_4F', 'WZZ', 'ZZZ']

directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}
ZZ = Sample.fromDirectory(name="ZZ", treeName="Events", isData=False, color=color.ZZ, texName="ZZ (4l)", directory=directories['ZZ'])
TTZ = Sample.fromDirectory(name="TTZ", treeName="Events", isData=False, color=color.TTZtoLLNuNu, texName="t#bar{t}Z", directory=directories['TTZ'])
rare = Sample.fromDirectory(name="rare", treeName="Events", isData=False, color=color.rare, texName="rare", directory=directories['rare'])


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
	    ratio = {'yRange':(0.1,1.9)} if not args.noData else None,
	    logX = False, logY = log, sorting = True,
	    yRange = (0.03, "auto") if log else (0.001, "auto"),
	    scaling = scaling if args.normalize else {},
	    legend = [ (0.15,0.9-0.03*sum(map(len, plot.histos)),0.9,0.9), 2],
	    drawObjects = drawObjects( not args.noData, dataMCScale , lumi_scale ),
        copyIndexPHP = True,
      )

# define 4l selections
offZ2 = "&&abs(Z2_mass_4l-91.2)>20" if args.selection.count("offZ2") else ""
def getLeptonSelection( mode ):
    if   mode=="mumumumu":  return "nMuons_tight_4l==4&&nElectrons_tight_4l==0" + offZ2
    elif mode=="mumumue":   return "nMuons_tight_4l==3&&nElectrons_tight_4l==1"
    elif mode=="mumuee":    return "nMuons_tight_4l==2&&nElectrons_tight_4l==2" + offZ2
    elif mode=="mueee":     return "nMuons_tight_4l==1&&nElectrons_tight_4l==3"
    elif mode=="eeee":      return "nMuons_tight_4l==0&&nElectrons_tight_4l==4" + offZ2
    elif mode=='all':       return "nMuons_tight_4l+nElectrons_tight_4l==4"

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
                    "lep[mediumMuonId/I,pt/F,eta/F,phi/F,pdgId/I,miniRelIso/F,relIso03/F,relIso04/F,sip3d/F,lostHits/I,convVeto/I,dxy/F,dz/F,hadronicOverEm/F,dEtaScTrkIn/F,dPhiScTrkIn/F,eInvMinusPInv/F,full5x5_sigmaIetaIeta/F,mvaTTV/F]", "nlep/I",
                    "met_pt/F", "met_phi/F", "metSig/F", "ht/F", "nBTag/I", 
                    "Z1_l1_index_4l/I", "Z1_l2_index_4l/I", "nonZ1_l1_index_4l/I", "nonZ1_l2_index_4l/I", "Z2_l1_index_4l/I", "Z2_l2_index_4l/I", 
                    "Z1_phi_4l/F","Z1_pt_4l/F", "Z1_mass_4l/F", "Z1_eta_4l/F","Z1_lldPhi_4l/F", "Z1_lldR_4l/F", "Z1_cosThetaStar_4l/F","Higgs_mass/F",
                    "Z2_phi_4l/F","Z2_pt_4l/F", "Z2_mass_4l/F", "Z2_eta_4l/F", "Z2_cosThetaStar_4l/F",
                    ]

sequence = []

def getMT2ll( event, sample ):
    l1 = ROOT.TLorentzVector()
    l2 = ROOT.TLorentzVector()
    event.lep_pt[event.nonZ1_l1_index_4l]
    l1.SetPtEtaPhiM(event.lep_pt[event.nonZ1_l1_index_4l], event.lep_eta[event.nonZ1_l1_index_4l], event.lep_phi[event.nonZ1_l1_index_4l], 0 )
    l2.SetPtEtaPhiM(event.lep_pt[event.nonZ1_l2_index_4l], event.lep_eta[event.nonZ1_l2_index_4l], event.lep_phi[event.nonZ1_l2_index_4l], 0 )
    mt2Calc.setLeptons(l1.Pt(), l1.Eta(), l1.Phi(), l2.Pt(), l2.Eta(), l2.Phi())

    met         = ROOT.TLorentzVector()
    met.SetPtEtaPhiM( event.met_pt, 0, event.met_phi, 0)

    Z           = ROOT.TLorentzVector()
    Z.SetPtEtaPhiM( event.Z1_pt_4l, event.Z1_eta_4l, event.Z1_phi_4l, 0)

    newMet = met+Z

    mt2Calc.setMet(newMet.Pt(), newMet.Phi())
    event.dl_mt2ll_Z = mt2Calc.mt2ll()

sequence += [ getMT2ll ]

def getDPhiZLep( event, sample ):
    event.dPhiZLep = deltaPhi(event.lep_phi[event.nonZ1_l1_index_4l], event.Z2_phi_4l)

def getDPhiZJet( event, sample ):
    event.dPhiZJet = deltaPhi(event.jet_phi[0], event.Z2_phi_4l) if event.njet>0 and event.Z1_mass_4l>0 else float('nan') #nJetSelected

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

sequence += [ getSelectedJets ]

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
    leptonCharge = -event.lep_pdgId[event.nonZ1_l1_index_4l]/abs(event.lep_pdgId[event.nonZ1_l1_index_4l])
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
    lepton.SetPtEtaPhiM( event.lep_pt[event.nonZ1_l1_index_4l], event.lep_eta[event.nonZ1_l1_index_4l], event.lep_phi[event.nonZ1_l1_index_4l], 0)
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
    lepton.SetPtEtaPhiM(event.lep_pt[event.nonZ1_l1_index_4l], event.lep_eta[event.nonZ1_l1_index_4l], event.lep_phi[event.nonZ1_l1_index_4l], 0)
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
    
    lepton.SetPtEtaPhiM(event.lep_pt[event.nonZ1_l1_index_4l], event.lep_eta[event.nonZ1_l1_index_4l], event.lep_phi[event.nonZ1_l1_index_4l], 0)
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
    lm_index = event.Z1_l1_index_4l if event.lep_pdgId[event.Z1_l1_index_4l] > 0 else event.Z1_l2_index_4l
    
    # get the Z and lepton vectors
    Z   = ROOT.TVector3()
    l   = ROOT.TVector3()

    # set the values
    Z.SetPtEtaPhi(event.Z1_pt_4l,               event.Z1_eta_4l,                event.Z1_phi_4l)
    l.SetPtEtaPhi(event.lep_pt[lm_index],   event.lep_eta[lm_index],    event.lep_phi[lm_index])

    # get cos(theta)
    cosTheta = Z*l / (sqrt(Z*Z) * sqrt(l*l))
    
    # get beta and gamma
    gamma   = sqrt(1+event.Z1_pt_4l**2/event.Z1_mass_4l**2 * cosh(event.Z1_eta_4l)**2 )
    beta    = sqrt( 1 - 1/gamma**2 )
    
    cosThetaStar = (-beta + cosTheta) / (1 - beta*cosTheta)
    event.cosThetaStar = cosThetaStar

def getZ2CosThetaStar( event, sample ):
    # get the negative-charge lepton from Z
    lm_index = event.Z2_l1_index_4l if event.lep_pdgId[event.Z2_l1_index_4l] > 0 else event.Z2_l2_index_4l

    # get the Z and lepton vectors
    Z   = ROOT.TVector3()
    l   = ROOT.TVector3()

    # set the values
    Z.SetPtEtaPhi(event.Z2_pt_4l,               event.Z2_eta_4l,                event.Z2_phi_4l)
    l.SetPtEtaPhi(event.lep_pt[lm_index],   event.lep_eta[lm_index],    event.lep_phi[lm_index])

    # get cos(theta)
    cosTheta = Z*l / (sqrt(Z*Z) * sqrt(l*l))

    # get beta and gamma
    gamma   = sqrt(1+event.Z2_pt_4l**2/event.Z2_mass_4l**2 * cosh(event.Z2_eta_4l)**2 )
    beta    = sqrt( 1 - 1/gamma**2 )

    cosThetaStar = (-beta + cosTheta) / (1 - beta*cosTheta)
    event.Z2_cosThetaStar = cosThetaStar


#sequence += [ getCosThetaStar, getZ2CosThetaStar ]

def getM3l( event, sample ):
    # get the invariant mass of the 3l system
    l = []
    for i in range(3):
        l.append(ROOT.TLorentzVector())
        l[i].SetPtEtaPhiM(event.lep_pt[i], event.lep_eta[i], event.lep_phi[i],0)
    event.threelmass = (l[0] + l[1] + l[2]).M()

sequence.append( getM3l )


def getLooseLeptonMult( event, sample ):
    leptons = [getObjDict(event, 'lep_', ['eta','pt','phi','charge', 'pdgId', 'sourceId','mediumMuonId'], i) for i in range(len(event.lep_pt))]
    lepLoose = [ l for l in leptons if l['pt'] > 10 and ((l['mediumMuonId'] and abs(l['pdgId'])==13) or abs(l['pdgId'])==11)  ]
    event.nLepLoose = len(lepLoose)

sequence.append( getLooseLeptonMult )


#
# Loop over channels
#
yields     = {}
allPlots   = {}
allModes   = ['mumumumu','mumumue','mumuee', 'mueee', 'eeee']
for index, mode in enumerate(allModes):
    yields[mode] = {}
    logger.info("Working on mode %s", mode)
    if not args.noData:
        data_sample = Run2016 if args.year == 2016 else Run2017
        data_sample.texName = "data"

        data_sample.setSelectionString([getFilterCut(isData=True, year=args.year), getLeptonSelection(mode)])
        data_sample.name           = "data"
        data_sample.read_variables = ["evt/I","run/I"]
        data_sample.style          = styles.errorStyle(ROOT.kBlack)
        lumi_scale                 = data_sample.lumi/1000

    if args.noData: lumi_scale = 35.9 if args.year == 2016 else 41.0
    weight_ = lambda event, sample: event.weight

    mc             = [ ZZ, TTZ, rare ]

    for sample in mc: sample.style = styles.fillStyle(sample.color)

    for sample in mc + signals:
      sample.scale          = lumi_scale
      sample.read_variables = ['reweightBTagCSVv2_SF/F', 'reweightBTagDeepCSV_SF/F', 'reweightPU36fb/F', 'reweightTrigger_tight_4l/F', 'reweightLeptonTrackingSF_tight_4l/F', 'nTrueInt/F', 'reweightPU36fb/F']
      
      if args.year == 2016:
          sample.weight         = lambda event, sample: event.reweightBTagDeepCSV_SF*event.reweightTrigger_tight_4l*event.reweightLeptonTrackingSF_tight_4l*event.reweightPU36fb #*nTrueInt36fb_puRW(event.nTrueInt)
      else:
          sample.weight         = lambda event, sample: event.reweightBTagDeepCSV_SF*event.reweightTrigger_tight_4l*event.reweightPU36fb #*nTrueInt36fb_puRW(event.nTrueInt)
      tr = triggerSelector(args.year)
      sample.setSelectionString([getFilterCut(isData=False, year=args.year), getLeptonSelection(mode), tr.getSelection("MC")])

    if not args.noData:
      stack = Stack(mc, data_sample)
    else:
      stack = Stack(mc)

    stack.extend( [ [s] for s in signals ] )

    if args.small:
        for sample in stack.samples:
            sample.reduceFiles( to = 1 )

    # Use some defaults
    Plot.setDefaults(stack = stack, weight = weight_, selectionString = cutInterpreter.cutString(args.selection), addOverFlowBin='both')

    plots = []
    
    plots.append(Plot(
      name = 'yield', texX = 'yield', texY = 'Number of Events',
      attribute = lambda event, sample: 0.5 + index,
      binning=[5, 0, 5],
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
        texX = 'H_{T} (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "ht/F" ),
        binning=[800/20,0,800],
    ))
    
    plots.append(Plot(
        texX = '#phi(E_{T}^{miss})', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "met_phi/F" ),
        binning=[10,-pi,pi],
    ))
    
    plots.append(Plot(
        texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 20 GeV',
        attribute = TreeVariable.fromString( "Z1_pt_4l/F" ),
        binning=[20,0,400],
    ))
    
    plots.append(Plot(
        name = 'Z1_pt_coarse', texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 50 GeV',
        attribute = TreeVariable.fromString( "Z1_pt_4l/F" ),
        binning=[16,0,800],
    ))
    
    plots.append(Plot(
        name = 'Z1_pt_superCoarse', texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events',
        attribute = TreeVariable.fromString( "Z1_pt_4l/F" ),
        binning=[3,0,600],
    ))
    
    plots.append(Plot(
        name = 'Z1_pt_analysis', texX = 'p_{T}(ll) (GeV)', texY = 'Number of Events / 100 GeV',
        attribute = TreeVariable.fromString( "Z1_pt_4l/F" ),
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
        attribute = TreeVariable.fromString( "Z1_lldPhi_4l/F" ),
        binning=[10,0,pi],
    ))

    # plots of lepton variables

    plots.append(Plot(
        name = "lZ1_pt",
        texX = 'p_{T}(l_{1,Z}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z1_l1_index_4l],
        binning=[30,0,300],
    ))

    plots.append(Plot(
        name = "lZ1_eta",
        texX = 'eta(l_{1,Z})', texY = 'Number of Events',
        attribute = lambda event, sample:event.lep_eta[event.Z1_l1_index_4l],
        binning=[40,-4.,4.],
    ))

    plots.append(Plot(
        name = "lZ1_phi",
        texX = '#phi(l_{1,Z})', texY = 'Number of Events',
        attribute = lambda event, sample:event.lep_phi[event.Z1_l1_index_4l],
        binning=[40,-3.2,3.2],
    ))

    plots.append(Plot(
        name = "lZ1_pdgId",
        texX = 'PDG ID (l_{1,Z})', texY = 'Number of Events',
        attribute = lambda event, sample:event.lep_pdgId[event.Z1_l1_index_4l],
        binning=[30,-15,15],
    ))

    # lepton 2    
    plots.append(Plot(
        name = "lZ2_pt",
        texX = 'p_{T}(l_{2,Z}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.Z1_l2_index_4l],
        binning=[20,0,200],
    ))


    plots.append(Plot(
        name = "lZ2_eta",
        texX = 'eta(l_{2,Z})', texY = 'Number of Events',
        attribute = lambda event, sample:event.lep_eta[event.Z1_l2_index_4l],
        binning=[40,-4.,4.],
    ))

    plots.append(Plot(
        name = "lZ2_phi",
        texX = '#phi(l_{2,Z})', texY = 'Number of Events',
        attribute = lambda event, sample:event.lep_phi[event.Z1_l2_index_4l],
        binning=[40,-3.2,3.2],
    ))

    plots.append(Plot(
        name = "lZ2_pdgId",
        texX = 'PDG ID (l_{2,Z})', texY = 'Number of Events',
        attribute = lambda event, sample:event.lep_pdgId[event.Z1_l2_index_4l],
        binning=[30,-15,15],
    ))
    
    # lepton 3
    plots.append(Plot(
        name = 'lnonZ1_pt',
        texX = 'p_{T}(l_{1,extra}) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = lambda event, sample:event.lep_pt[event.nonZ1_l1_index_4l],
        binning=[30,0,300],
    ))

    plots.append(Plot(
        name = "lnonZ1_eta",
        texX = 'eta(l_{1,extra})', texY = 'Number of Events',
        attribute = lambda event, sample:event.lep_eta[event.nonZ1_l1_index_4l],
        binning=[40,-4.,4.],
    ))

    plots.append(Plot(
        name = "lnonZ1_phi",
        texX = '#phi(l_{1,extra})', texY = 'Number of Events',
        attribute = lambda event, sample:event.lep_phi[event.nonZ1_l1_index_4l],
        binning=[40,-3.2,3.2],
    ))

    plots.append(Plot(
        name = "lnonZ1_pdgId",
        texX = 'PDG ID (l_{1,extra})', texY = 'Number of Events',
        attribute = lambda event, sample:event.lep_pdgId[event.nonZ1_l1_index_4l],
        binning=[30,-15,15],
    ))

    # other plots


    plots.append(Plot(
        texX = 'M(ll) (GeV)', texY = 'Number of Events / 2 GeV',
        attribute = TreeVariable.fromString( "Z1_mass_4l/F" ),
        binning=[20,70,110],
    ))

    plots.append(Plot(
        texX = 'M(ll) 2nd OS pair (GeV)', texY = 'Number of Events / 8 GeV',
        attribute = TreeVariable.fromString( "Z2_mass_4l/F" ),
        binning=[20,40,200],
    ))
    
    plots.append(Plot(
        texX = 'M(ZZ) (GeV)', texY = 'Number of Events / 10 GeV',
        attribute = TreeVariable.fromString( "Higgs_mass/F" ),
        binning=[22,80,300],
    ))
    
    plots.append(Plot(
        texX = 'M_{T2}(ll) Z estimated (GeV)', texY = 'Number of Events',
        name = "mt2ll_Z_estimated",
        attribute = lambda event, sample: event.dl_mt2ll_Z,
        binning=[4,0,320],
    ))
    
    plots.append(Plot(
      texX = 'N_{jets}', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nJetSelected/I" ), #nJetSelected
      binning=[8,-0.5,7.5],
    ))
    
    plots.append(Plot(
      texX = 'N_{b-tag}', texY = 'Number of Events',
      attribute = TreeVariable.fromString( "nBTag/I" ),
      binning=[4,-0.5,3.5],
    ))
    
    plots.append(Plot(
      texX = 'N_{l, loose}', texY = 'Number of Events',
      name = 'nLepLoose', attribute = lambda event, sample: event.nlep,
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

    plots.append(Plot(
        name = "LP", texX = 'L_{P}', texY = 'Number of Events / 0.1',
        attribute = lambda event, sample:event.Lp,
        binning=[20,-1,1],
    ))
    
    plots.append(Plot(
        name = "Z1_cosThetaStar", texX = 'cos#theta(Z1,l-)', texY = 'Number of Events / 0.2',
        attribute = lambda event, sample:event.Z1_cosThetaStar_4l,
        binning=[10,-1,1],
    ))
    
    plots.append(Plot(
        name = "Z1_cosThetaStar_coarse", texX = 'cos#theta(Z1,l-)', texY = 'Number of Events / 0.2',
        attribute = lambda event, sample:event.Z1_cosThetaStar_4l,
        binning=[5,-1,1],
    ))
    
    plots.append(Plot(
        name = "Z2_cosThetaStar", texX = 'cos#theta(Z2,l-)', texY = 'Number of Events / 0.2',
        attribute = lambda event, sample:event.Z2_cosThetaStar_4l,
        binning=[10,-1,1],
    ))
    
    plotting.fill(plots, read_variables = read_variables, sequence = sequence)

    # Get normalization yields from yield histogram
    for plot in plots:
      if plot.name == "yield":
        for i, l in enumerate(plot.histos):
          for j, h in enumerate(l):
            yields[mode][plot.stack[i][j].name] = h.GetBinContent(h.FindBin(0.5+index))
            h.GetXaxis().SetBinLabel(1, "#mu#mu#mu#mu")
            h.GetXaxis().SetBinLabel(2, "#mu#mu#mue")
            h.GetXaxis().SetBinLabel(3, "#mu#muee")
            h.GetXaxis().SetBinLabel(4, "#mueee")
            h.GetXaxis().SetBinLabel(5, "eeee")
    if args.noData: yields[mode]["data"] = 0

    yields[mode]["MC"] = sum(yields[mode][s.name] for s in mc)
    dataMCScale        = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')

    drawPlots(plots, mode, dataMCScale)
    allPlots[mode] = plots

# Add the different channels into SF and all
for mode in ["comb1","comb2","comb3","all"]:
    yields[mode] = {}
    for y in yields[allModes[0]]:
        try:    yields[mode][y] = sum(yields[c][y] for c in ['eeee','mueee','mumuee', 'mumumue', 'mumumumu'])
        except: yields[mode][y] = 0
    dataMCScale = yields[mode]["data"]/yields[mode]["MC"] if yields[mode]["MC"] != 0 else float('nan')
    
    for plot in allPlots['mumumumu']:
        if mode=="comb1":
            tmp = allPlots['mumumue']
        elif mode=="comb2":
            tmp = allPlots['mumuee']
        elif mode=="comb3":
            tmp = allPlots['mueee']
        else:
            tmp = allPlots['eeee']
        for plot2 in (p for p in tmp if p.name == plot.name):
            for i, j in enumerate(list(itertools.chain.from_iterable(plot.histos))):
                for k, l in enumerate(list(itertools.chain.from_iterable(plot2.histos))):
                    if i==k:
                        j.Add(l)
    
    if mode == "all": drawPlots(allPlots['mumumumu'], mode, dataMCScale)

logger.info( "Done with prefix %s and selectionString %s", args.selection, cutInterpreter.cutString(args.selection) )

