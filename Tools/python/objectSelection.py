# Standard imports
import numbers
from math import *

# TopEFT
from TopEFT.Tools.helpers import mZ, getVarValue, getObjDict, deltaR

# helpers
def alwaysTrue(*args, **kwargs):
  return True
def alwaysFalse(*args, **kwargs):
  return False

# Jets & b-jets

jetVars = ['eta','pt','phi','btagCSV', 'id', 'area', 'btagDeepCSV']

def getJets(c, jetVars=jetVars, jetColl="Jet"):
    return [getObjDict(c, jetColl+'_', jetVars, i) for i in range(int(getVarValue(c, 'n'+jetColl)))]

def isAnalysisJet(j, ptCut=30, absEtaCut=2.4, ptVar='pt'):
  return j[ptVar]>ptCut and abs(j['eta'])<absEtaCut and j['id']

def getGoodJets(c, ptCut=30, absEtaCut=2.4, jetVars=jetVars, jetColl="Jet"):
    return filter(lambda j:isAnalysisJet(j, ptCut=ptCut, absEtaCut=absEtaCut), getJets(c, jetVars, jetColl=jetColl))

def getAllJets(c, leptons, ptCut=30, absEtaCut=2.4, jetVars=jetVars, jetCollections=[ "Jet", "DiscJet"]):

    jets = sum( [ filter(lambda j:isAnalysisJet(j, ptCut=ptCut, absEtaCut=absEtaCut), getJets(c, jetVars, jetColl=coll)) for coll in jetCollections], [] )
    res  = []

    for jet in jets:
        clean = True
        for lepton in leptons:
            if deltaR(lepton, jet) < 0.4:
                clean = False
                break
        if clean:
            res.append(jet)

    res.sort( key = lambda j:-j['pt'] )

    return res

def isBJet(j, tagger = 'DeepCSV', year = 2016):
    if tagger == 'CSVv2':
        if year == 2016:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
            return j['btagCSV'] > 0.8484 
        elif year == 2017:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
            return j['btagCSV'] > 0.8838 
        else:
            raise (NotImplementedError, "Don't know what cut to use for year %s"%year)
    elif tagger == 'DeepCSV':
        if year == 2016:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation80XReReco
            return j['btagDeepCSV'] > 0.6324
        elif year == 2017:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
            return j['btagDeepCSV'] > 0.4941
        else:
            raise (NotImplementedError, "Don't know what cut to use for year %s"%year)


def getGoodBJets(c, tagger = 'DeepCSV'):
    return filter(lambda j:isBJet(j, tagger = tagger), getGoodJets(c))

def getGenLeps(c):
    return [getObjDict(c, 'genLep_', ['eta','pt','phi','charge', 'pdgId', 'sourceId'], i) for i in range(int(getVarValue(c, 'ngenLep')))]

def getGenParts(c):
    return [getObjDict(c, 'GenPart_', ['eta','pt','phi','charge', 'pdgId', 'motherId', 'grandmotherId'], i) for i in range(int(getVarValue(c, 'nGenPart')))]

genVars = ['eta', 'pt', 'phi', 'mass', 'charge', 'status', 'pdgId', 'motherId', 'grandmotherId', 'nDaughters', 'daughterIndex1', 'daughterIndex2', 'nMothers', 'motherIndex1', 'motherIndex2', 'isPromptHard'] 
def getGenPartsAll(c):
    return [getObjDict(c, 'genPartAll_', genVars, i) for i in range(int(getVarValue(c, 'ngenPartAll')))]

#https://twiki.cern.ch/twiki/bin/viewauth/CMS/SUSLeptonSF

tight_mva_threshold = 0.85
lepton_selections = ['loose', 'tight', 'FO', 'tight_SS', 'FO_SS']

# muons 
def muonSelector( lepton_selection, year):

    if lepton_selection not in lepton_selections:
        raise ValueError( "Don't know about muon selection %r. Allowed: %r" % (lepton_selection, lepton_selections) )

    if lepton_selection == 'loose':
        def func(l):
            return \
                l["pt"]>=5\
                and abs(l["pdgId"])==13\
                and abs(l["eta"])<2.4\
                and l["miniRelIso"]<0.4 \
                and l["sip3d"]<8.0\
                and abs(l["dxy"])<0.05\
                and abs(l["dz"])<0.1

    elif lepton_selection == 'tight':
        loose_ = muonSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["mediumMuonId"]>=1\
                and l["relIso03"]<0.15\
                and l["sip3d"]<4.0\
                and l['lostHits']<=1
                ## -> future
                # and l["mvaTTV"] > tight_mva_threshold

    elif lepton_selection == 'FO':
        loose_ = muonSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["mediumMuonId"]>=1 

    # No extra muon-SS cuts for FO and tight selections
    elif lepton_selection == 'FO_SS':
        func = muonSelector('FO', year)

    elif lepton_selection == 'tight_SS':
        func = muonSelector('tight', year)

    return func

# electrons 

def triggerEmulatorSelector(l):

    ECSc = abs(l["etaSc"])>1.479

    if l["full5x5_sigmaIetaIeta"]   >= (0.00998+0.01922*ECSc):   return False
    if abs(l["dPhiScTrkIn"])        >= (0.0816-0.0422*ECSc):     return False
    if abs(l["dEtaScTrkIn"])        >= (0.00308+0.00297*ECSc):    return False
    if l["eInvMinusPInv"]           <= -0.05:                return False
    if l["eInvMinusPInv"]           >= (0.0129-0.0*ECSc):    return False
    if l["hadronicOverEm"]          >= (0.0414+0.0227*ECSc):     return False
    return True


#ele_MVAID = {'M': {(0,0.8):0.837, (0.8, 1.479):0.715, (1.57, 999): 0.357}}
#ele_MVAID = {'M': {(0,0.8):0.913286 , (0.8, 1.479):0.805013, (1.57, 999): 0.358969},
#            'VL': {(0,0.8):-0.76, (0.8, 1.479):-0.52, (1.57, 999): -0.23}}
#def eleMVAIDSelector( eleId ):
#    ele_mva_WP = ele_MVAID[eleId]
#    def func(l):
#        abs_ele_eta = abs(l["eta"])
#        for abs_ele_bin, mva_threshold in ele_mva_WP.iteritems():
#            if abs_ele_eta>=abs_ele_bin[0] and abs_ele_eta<abs_ele_bin[1] and l["mvaIdSpring16"] > mva_threshold: return True
#        return False
#    return func

#def eleCutIDSelector( ele_cut_Id = 4):
#    def func(l):
#        return l["eleCutId_Spring2016_25ns_v1_ConvVetoDxyDz"]>=ele_cut_Id 
#    return func


def eleSelector( lepton_selection, year ):

    if lepton_selection not in lepton_selections:
        raise ValueError( "Don't know about ele selection %r. Allowed: %r" % (lepton_selection, lepton_selections) )

    if lepton_selection == 'loose':
        def func(l):
            return \
                l["pt"]>=7\
                and abs(l["pdgId"])==11\
                and abs(l["eta"])<2.5\
                and l["miniRelIso"]<0.4\
                and l["sip3d"]<8.0\
                and abs(l["dxy"])<0.05\
                and abs(l["dz"])<0.1\
                and abs(l["lostHits"])<2\
                and triggerEmulatorSelector(l) 

    elif lepton_selection == 'tight':
        loose_ = eleSelector( 'loose', year)
        if year == 2016:
            def func(l):
                return \
                    loose_(l) \
                    and l["eleCutId_Spring2016_25ns_v1_ConvVetoDxyDz"]>=4
                    #and l["relIso03"]<0.15
                    #and l["relIso03"] < 0.15\
                    #and l["sip3d"]<4.0\
                    #and l['convVeto']\
                    #and l['lostHits']<=1\
                    #and ( ( l["full5x5_sigmaIetaIeta"]<0.0105     and (abs(l["eta"])<1.479) ) or (l["full5x5_sigmaIetaIeta"]<0.309 and (abs(l["eta"])>=1.479)) )\
                    #and ( ( abs(l["dEtaScTrkIn"])<0.00365 and (abs(l["eta"])<1.479) ) or (abs(l["dEtaScTrkIn"])<0.00625 and (abs(l["eta"])>=1.479)) )\
                    #and ( ( abs(l["dPhiScTrkIn"])<0.103   and (abs(l["eta"])<1.479) ) or (abs(l["dPhiScTrkIn"])<0.045  and (abs(l["eta"])>=1.479)) )\
                    #and ( ( abs(l["eInvMinusPInv"])<0.134 and (abs(l["eta"])<1.479) ) or (abs(l["eInvMinusPInv"])<0.13  and (abs(l["eta"])>=1.479)) )\
                    #and ( ( abs(l["hadronicOverEm"])<0.253 and (abs(l["eta"])<1.479)) or (abs(l["hadronicOverEm"])<0.0878 and (abs(l["eta"])>=1.479)) ) 
        elif year == 2017:
            def func(l):
                loose_ = eleSelector( 'loose', year)
                return \
                    loose_(l) \
                    and l["relIso03"] < 0.15\
                    and l["sip3d"]<4.0\
                    and l['convVeto']\
                    and l['lostHits']<=1\
                    and ( ( l["full5x5_sigmaIetaIeta"]<0.0105     and (abs(l["eta"])<1.479) ) or (l["full5x5_sigmaIetaIeta"]<0.309 and (abs(l["eta"])>=1.479)) )\
                    and ( ( abs(l["dEtaScTrkIn"])<0.00365 and (abs(l["eta"])<1.479) ) or (abs(l["dEtaScTrkIn"])<0.00625 and (abs(l["eta"])>=1.479)) )\
                    and ( ( abs(l["dPhiScTrkIn"])<0.0588  and (abs(l["eta"])<1.479) ) or (abs(l["dPhiScTrkIn"])<0.0355  and (abs(l["eta"])>=1.479)) )\
                    and ( ( abs(l["eInvMinusPInv"])<0.0327 and (abs(l["eta"])<1.479)) or (abs(l["eInvMinusPInv"])<0.0335  and (abs(l["eta"])>=1.479)) )\
                    and ( ( abs(l["hadronicOverEm"])<0.253 and (abs(l["eta"])<1.479)) or (abs(l["hadronicOverEm"])<0.0878 and (abs(l["eta"])>=1.479)) ) 
                # future -->
                #and l["mvaTTV"] > tight_mva_threshold

    elif lepton_selection == 'FO':
        loose_ = eleSelector( 'loose', year)
        def func(l):
            loose_ = eleSelector( 'loose', year)
            return \
                loose_(l)

    # extra ele-SS cuts for FO and tight selections
    elif lepton_selection == 'FO_SS':
        fo_ = eleSelector('FO', year)
        def func(l):
            return fo_(l)\
                and l['convVeto']\
                and l['lostHits']==0\
                and l['tightCharge']==2

    elif lepton_selection == 'tight_SS':
        tight_ = eleSelector('tight', year)
        def func(l):
            return tight_(l)\
                and l['convVeto']\
                and l['lostHits']==0\
                and l['tightCharge']==2

    return func

lepton_branches_data = 'pt/F,eta/F,etaSc/F,phi/F,pdgId/I,tightId/I,tightCharge/I,miniRelIso/F,relIso03/F,relIso04/F,sip3d/F,mediumMuonId/I,lostHits/I,convVeto/I,dxy/F,dz/F,hadronicOverEm/F,dEtaScTrkIn/F,dPhiScTrkIn/F,eInvMinusPInv/F,full5x5_sigmaIetaIeta/F,etaSc/F,mvaTTH/F,matchedTrgObj1Mu/F,matchedTrgObj1El/F'
lepton_branches_mc   = lepton_branches_data + ',mcMatchId/I,mcMatchAny/I'

leptonVars = [s.split('/')[0] for s in lepton_branches_mc.split(',')] 

def getAllLeptons(c, collVars=leptonVars, collection = "LepGood"):
    return [getObjDict(c, '%s_'%collection, collVars, i) for i in range(int(getVarValue(c, 'n%s'%collection)))]

def getLeptons(c, mu_selector, ele_selector, collVars=leptonVars):
    good_lep = [l for l in getAllLeptons(c, collVars, 'LepGood') if (abs(l["pdgId"])==11 and ele_selector(l)) or (abs(l["pdgId"])==13 and mu_selector(l))]
    other_lep = [l for l in getAllLeptons(c, collVars, 'LepOther') if (abs(l["pdgId"])==11 and ele_selector(l)) or (abs(l["pdgId"])==13 and mu_selector(l))]
    lep = good_lep + other_lep
    lep.sort( key = lambda l:-l['pt'] )
    return lep

def getElectrons(c, selector, collVars=leptonVars):
    good_lep = [l for l in getAllLeptons(c, collVars, 'LepGood') if (abs(l["pdgId"])==11 and selector(l))]
    other_lep = [l for l in getAllLeptons(c, collVars, 'LepOther') if (abs(l["pdgId"])==11 and selector(l))]
    lep = good_lep + other_lep
    lep.sort( key = lambda l:-l['pt'] )
    return lep

def getMuons(c, selector, collVars=leptonVars):
    good_lep = [l for l in getAllLeptons(c, collVars, 'LepGood') if (abs(l["pdgId"])==13 and selector(l))]
    other_lep = [l for l in getAllLeptons(c, collVars, 'LepOther') if (abs(l["pdgId"])==13 and selector(l))]
    lep = good_lep + other_lep
    lep.sort( key = lambda l:-l['pt'] )
    return lep

tauVars=['eta','pt','phi','pdgId','charge', 'dxy', 'dz', 'idDecayModeNewDMs', 'idCI3hit', 'idAntiMu','idAntiE','mcMatchId']

def getTaus(c, collVars=tauVars):
    return [getObjDict(c, 'TauGood_', collVars, i) for i in range(int(getVarValue(c, 'nTauGood')))]

def looseTauID(l, ptCut=20, absEtaCut=2.4):
    return \
        l["pt"]>=ptCut\
        and abs(l["eta"])<absEtaCut\
        and l["idDecayModeNewDMs"]>=1\
        and l["idCI3hit"]>=1\
        and l["idAntiMu"]>=1\
        and l["idAntiE"]>=1\

def getGoodTaus(c, collVars=tauVars):
    return [l for l in getTaus(c,collVars=collVars) if looseTauID(l)]

idCutBased={'loose':1 ,'medium':2, 'tight':3}
photonVars=['eta','pt','phi','mass','idCutBased','pdgId']
photonVarsMC = photonVars + ['mcPt']
def getPhotons(c, collVars=photonVars, idLevel='loose'):
    return [getObjDict(c, 'gamma_', collVars, i) for i in range(int(getVarValue(c, 'ngamma')))]
def getGoodPhotons(c, ptCut=50, idLevel="loose", isData=True, collVars=None):
    if collVars is None: collVars = photonVars if isData else photonVarsMC
    return [p for p in getPhotons(c, collVars) if p['idCutBased'] >= idCutBased[idLevel] and p['pt'] > ptCut and p['pdgId']==22]


def getFilterCut(isData=False, isFastSim = False, year = 2016):
    if isFastSim:
        filterCut            = "Flag_goodVertices"
    else:
        if year == 2017:
            filters = ["Flag_goodVertices", "Flag_globalTightHalo2016Filter", "Flag_HBHENoiseFilter", "Flag_HBHENoiseIsoFilter", "Flag_EcalDeadCellTriggerPrimitiveFilter", "Flag_BadPFMuonFilter", "Flag_BadChargedCandidateFilter", "Flag_ecalBadCalibFilter"]
            filterCut = "&&".join(filters)
        else:
            filterCut            = "Flag_goodVertices&&Flag_HBHENoiseIsoFilter&&Flag_HBHENoiseFilter&&Flag_globalTightHalo2016Filter&&Flag_EcalDeadCellTriggerPrimitiveFilter"
            filterCut            += "&&Flag_badChargedHadronSummer2016&&Flag_badMuonSummer2016"

    if isData: filterCut += "&&weight>0"
    return filterCut
