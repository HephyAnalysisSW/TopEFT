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

jetVars = ['eta','pt','phi','btagCSV', 'id', 'id16', 'area', 'btagDeepCSV']

def getJets(c, jetVars=jetVars, jetColl="Jet"):
    return [getObjDict(c, jetColl+'_', jetVars, i) for i in range(int(getVarValue(c, 'n'+jetColl)))]

def isAnalysisJet(j, ptCut=30, absEtaCut=2.4, ptVar='pt', idVar='id'):
  return j[ptVar]>ptCut and abs(j['eta'])<absEtaCut and ( j[idVar] if idVar is not None else True )

def getGoodJets(c, ptCut=30, absEtaCut=2.4, jetVars=jetVars, jetColl="Jet"):
    return filter(lambda j:isAnalysisJet(j, ptCut=ptCut, absEtaCut=absEtaCut), getJets(c, jetVars, jetColl=jetColl))

def getAllJets(c, leptons, ptCut=30, absEtaCut=2.4, jetVars=jetVars, jetCollections=[ "Jet", "DiscJet"], idVar='id'):

    jets = sum( [ filter(lambda j:isAnalysisJet(j, ptCut=ptCut, absEtaCut=absEtaCut, idVar=idVar), getJets(c, jetVars, jetColl=coll)) for coll in jetCollections], [] )
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
def getGenPartsAll(c, collection="genPartAll", genVars=genVars):
    return [getObjDict(c, '%s_'%collection, genVars, i) for i in range(getattr(c, 'n%s'%collection))]

#https://twiki.cern.ch/twiki/bin/viewauth/CMS/SUSLeptonSF

lepton_selections = ['loose', 'FO_SS', 'FO_1l', 'FO_2l', 'FO_3l', 'FO_4l', 'tight_SS', 'tight_2l', 'tight_1l', 'tight_3l', 'tight_4l']

# muons 
def muonSelector( lepton_selection, year):

    mva_threshold_4l = -0.4
    mva_threshold_3l = 0.4
    mva_threshold_2l = 0.4 # DUMMY VALUE, change ASAP
    mva_threshold_1l = 0.4 # DUMMY VALUE, change ASAP
    mva_threshold_SS = 0.6

    closestJetDCsvFO_3l = 0.5 if year == 2017 else 0.4
    closestJetDCsvFO_2l = 0.5 if year == 2017 else 0.4 # DUMMY VALUE, change ASAP
    closestJetDCsvFO_1l = 0.5 if year == 2017 else 0.4 # DUMMY VALUE, change ASAP
    closestJetDCsvFO    = 0.4 if year == 2017 else 0.3
    closestJetDCsv      = 0.8001 if year == 2017 else 0.8958

    ptRatioThreshold_3l = 0.4 if year == 2017 else 0.4 # keep in case of changes
    ptRatioThreshold_2l = 0.4 if year == 2017 else 0.4 # DUMMY VALUE, change ASAP
    ptRatioThreshold_1l = 0.4 if year == 2017 else 0.4 # DUMMY VALUE, change ASAP
    ptRatioThreshold    = 0.4 if year == 2017 else 0.5

    if lepton_selection not in lepton_selections:
        raise ValueError( "Don't know about muon selection %r. Allowed: %r" % (lepton_selection, lepton_selections) )

    '''
    All selections based on loose definition
    '''

    if lepton_selection == 'loose':
        def func(l):
            return \
                l["pt"]>=5\
                and abs(l["pdgId"])==13\
                and abs(l["eta"])<2.4\
                and l["miniRelIso"]<0.4 \
                and l["sip3d"]<8.0\
                and abs(l["dxy"])<0.05\
                and abs(l["dz"])<0.1\
                and l["pfMuonId"]

    elif lepton_selection == 'FO_4l':
        loose_ = muonSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["mediumMuonId"]>=1\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and ( ( l["mvaTTV"] < mva_threshold_4l and l["jetPtRatiov2"] > ptRatioThreshold and l["jetBTagDeepCSV"] <= closestJetDCsvFO ) or l["mvaTTV"] >= mva_threshold_4l )

    elif lepton_selection == 'FO_3l':
        loose_ = muonSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["mediumMuonId"]>=1\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and ( ( l["mvaTTV"] < mva_threshold_3l and l["jetPtRatiov2"] > ptRatioThreshold_3l and l["jetBTagDeepCSV"] <= closestJetDCsvFO_3l ) or l["mvaTTV"] >= mva_threshold_3l )

    elif lepton_selection == 'FO_2l':
        loose_ = muonSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["mediumMuonId"]>=1\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and ( ( l["mvaTTV"] < mva_threshold_2l and l["jetPtRatiov2"] > ptRatioThreshold_2l and l["jetBTagDeepCSV"] <= closestJetDCsvFO_2l ) or l["mvaTTV"] >= mva_threshold_2l )

    elif lepton_selection == 'FO_1l':
        loose_ = muonSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["mediumMuonId"]>=1\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and ( ( l["mvaTTV"] < mva_threshold_1l and l["jetPtRatiov2"] > ptRatioThreshold_1l and l["jetBTagDeepCSV"] <= closestJetDCsvFO_1l ) or l["mvaTTV"] >= mva_threshold_1l )

    elif lepton_selection == 'FO_SS':
        loose_ = muonSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["mediumMuonId"]>=1\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and ( ( l["mvaTTV"] < mva_threshold_SS and l["jetPtRatiov2"] > ptRatioThreshold and l["jetBTagDeepCSV"] <= closestJetDCsvFO ) or l["mvaTTV"] >= mva_threshold_SS )

    elif lepton_selection == 'tight_4l':
        loose_ = muonSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["mediumMuonId"]>=1\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and l["mvaTTV"] >= mva_threshold_4l

    elif lepton_selection == 'tight_3l':
        loose_ = muonSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["mediumMuonId"]>=1\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and l["mvaTTV"] >= mva_threshold_3l

    elif lepton_selection == 'tight_2l':
        loose_ = muonSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["mediumMuonId"]>=1\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and l["mvaTTV"] >= mva_threshold_2l

    elif lepton_selection == 'tight_1l':
        loose_ = muonSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["mediumMuonId"]>=1\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and l["mvaTTV"] >= mva_threshold_1l

    elif lepton_selection == 'tight_SS':
        loose_ = muonSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["mediumMuonId"]>=1\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and l["mvaTTV"] >= mva_threshold_SS\
                and l["muonInnerTrkRelErr"] <= 0.2             # assume this is the correct branch

    return func

# electrons 

def triggerEmulatorSelector(l):

    ECSc = abs(l["etaSc"])>1.479

    if l["full5x5_sigmaIetaIeta"]   >= (0.011+0.019*ECSc):   return False
    if abs(l["dPhiScTrkIn"])        >= (0.04+0.03*ECSc):     return False
    if abs(l["dEtaScTrkIn"])        >= (0.01-0.002*ECSc):    return False
    if l["eInvMinusPInv"]           <= -0.05:                return False
    if l["eInvMinusPInv"]           >= (0.01-0.005*ECSc):    return False
    if l["hadronicOverEm"]          >= (0.10-0.03*ECSc):     return False
    return True

def eleSelector( lepton_selection, year ):

    mva_threshold_4l = -0.4
    mva_threshold_3l = 0.4
    mva_threshold_2l = 0.4 # DUMMY VALUE, change ASAP
    mva_threshold_1l = 0.4 # DUMMY VALUE, change ASAP
    mva_threshold_SS = 0.6

    closestJetDCsvFO_3l = 0.5 if year == 2017 else 0.4
    closestJetDCsvFO_2l = 0.5 if year == 2017 else 0.4 # DUMMY VALUE, change ASAP
    closestJetDCsvFO_1l = 0.5 if year == 2017 else 0.4 # DUMMY VALUE, change ASAP
    closestJetDCsvFO    = 0.4 if year == 2017 else 0.3
    closestJetDCsv      = 0.8001 if year == 2017 else 0.8958

    ptRatioThreshold_3l = 0.4 if year == 2017 else 0.4 # keep in case of changes
    ptRatioThreshold_2l = 0.4 if year == 2017 else 0.4 # DUMMY VALUE, change ASAP
    ptRatioThreshold_1l = 0.4 if year == 2017 else 0.4 # DUMMY VALUE, change ASAP
    ptRatioThreshold    = 0.4 if year == 2017 else 0.5

    eleMVA              = "mvaIdFall17noIso" if year == 2017 else "mvaIdSpring16"

    eleMVAval1_3l       = -0.3 if year == 2017 else -0.1
    eleMVAval1_2l       = -0.3 if year == 2017 else -0.1 # DUMMY VALUE, change ASAP
    eleMVAval1_1l       = -0.3 if year == 2017 else -0.1 # DUMMY VALUE, change ASAP
    eleMVAval1          =  0.4 if year == 2017 else  0.3

    eleMVAval2_3l       =  0.6 if year == 2017 else  0.8
    eleMVAval2_2l       =  0.6 if year == 2017 else  0.8 # DUMMY VALUE, change ASAP
    eleMVAval2_1l       =  0.6 if year == 2017 else  0.8 # DUMMY VALUE, change ASAP
    eleMVAval2          =  0.4 if year == 2017 else  0.3


    if lepton_selection not in lepton_selections:
        raise ValueError( "Don't know about ele selection %r. Allowed: %r" % (lepton_selection, lepton_selections) )

    ''' All selections based on loose definition
    '''

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
                and abs(l["lostHits"])<=1\
                and triggerEmulatorSelector(l) 

    elif lepton_selection == 'FO_4l':
        loose_ = eleSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and ( ( l["mvaTTV"] < mva_threshold_4l and l["jetPtRatiov2"] > ptRatioThreshold and l["jetBTagDeepCSV"] <= closestJetDCsvFO and l[eleMVA] >= (eleMVAval1 + (abs(l["eta"])>=1.479) * eleMVAval2 )) or l["mvaTTV"] >= mva_threshold_4l )

    elif lepton_selection == 'FO_3l':
        loose_ = eleSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and ( ( l["mvaTTV"] < mva_threshold_3l and l["jetPtRatiov2"] > ptRatioThreshold_3l and l["jetBTagDeepCSV"] <= closestJetDCsvFO_3l and l[eleMVA] >= (eleMVAval1_3l + (abs(l["eta"])>=1.479) * eleMVAval2_3l )) or l["mvaTTV"] >= mva_threshold_3l )

    elif lepton_selection == 'FO_2l':
        loose_ = eleSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and ( ( l["mvaTTV"] < mva_threshold_2l and l["jetPtRatiov2"] > ptRatioThreshold_2l and l["jetBTagDeepCSV"] <= closestJetDCsvFO_2l and l[eleMVA] >= (eleMVAval1_2l + (abs(l["eta"])>=1.479) * eleMVAval2_2l )) or l["mvaTTV"] >= mva_threshold_2l )

    elif lepton_selection == 'FO_1l':
        loose_ = eleSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and ( ( l["mvaTTV"] < mva_threshold_1l and l["jetPtRatiov2"] > ptRatioThreshold_1l and l["jetBTagDeepCSV"] <= closestJetDCsvFO_1l and l[eleMVA] >= (eleMVAval1_1l + (abs(l["eta"])>=1.479) * eleMVAval2_1l )) or l["mvaTTV"] >= mva_threshold_1l )

    elif lepton_selection == 'FO_SS':
        loose_ = eleSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and ( ( l["mvaTTV"] < mva_threshold_SS and l["jetPtRatiov2"] > ptRatioThreshold and l["jetBTagDeepCSV"] <= closestJetDCsvFO and l[eleMVA] >= (eleMVAval1 + (abs(l["eta"])>=1.479) * eleMVAval2 )) or l["mvaTTV"] >= mva_threshold_SS )

    elif lepton_selection == 'tight_4l':
        loose_ = eleSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and l["mvaTTV"] >= mva_threshold_4l

    elif lepton_selection == 'tight_3l':
        loose_ = eleSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and l["mvaTTV"] >= mva_threshold_3l

    elif lepton_selection == 'tight_2l':
        loose_ = eleSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and l["mvaTTV"] >= mva_threshold_2l

    elif lepton_selection == 'tight_1l':
        loose_ = eleSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and l["mvaTTV"] >= mva_threshold_1l

    elif lepton_selection == 'tight_SS':
        loose_ = eleSelector( 'loose', year )
        def func(l):
            return \
                loose_(l) \
                and l["pt"] >= 10\
                and l["jetBTagDeepCSV"] <= closestJetDCsv\
                and l["mvaTTV"] >= mva_threshold_SS\
                and l["chargeConsistency"]\
                and l["convVeto"]\
                and l["lostHits"] == 0


    return func

lepton_branches_data = 'pt/F,eta/F,etaSc/F,phi/F,pdgId/I,tightId/I,tightCharge/I,miniRelIso/F,relIso03/F,relIso04/F,sip3d/F,mediumMuonId/I,pfMuonId/I,lostHits/I,convVeto/I,dxy/F,dz/F,hadronicOverEm/F,dEtaScTrkIn/F,dPhiScTrkIn/F,eInvMinusPInv/F,full5x5_sigmaIetaIeta/F,etaSc/F,mvaTTH/F,matchedTrgObj1Mu/F,matchedTrgObj1El/F,muonInnerTrkRelErr/F,chargeConsistency/I'
lepton_branches_mc   = lepton_branches_data + ',mcMatchId/I,mcMatchAny/I,mcPt/F'

leptonVars = [s.split('/')[0] for s in lepton_branches_mc.split(',')] 

def getAllLeptons(c, collVars=leptonVars, collection = "LepGood"):
    n = int(getVarValue(c, 'n%s'%collection))
    res = [getObjDict(c, '%s_'%collection, collVars, i) for i in range(n)]
    # recall intial index
    for i in range(n):
        res[i]['i%s'%collection] = i
    return res

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
            if isData:
                filterCut += "&&Flag_eeBadScFilter"
        else:
            filterCut            = "Flag_goodVertices&&Flag_HBHENoiseIsoFilter&&Flag_HBHENoiseFilter&&Flag_globalTightHalo2016Filter&&Flag_EcalDeadCellTriggerPrimitiveFilter"
            filterCut            += "&&Flag_badChargedHadronSummer2016&&Flag_badMuonSummer2016"

    if isData: filterCut += "&&weight>0"
    return filterCut

def isGoodDelphesJet( j, ptCut=30, absEtaCut=2.4, ptVar='pt'):
  return j[ptVar]>ptCut and abs(j['eta'])<absEtaCut  

def isGoodDelphesLepton( j, ptCut=10, absEtaCut=3, ptVar='pt'):
  return j[ptVar]>ptCut and abs(j['eta'])<absEtaCut  
