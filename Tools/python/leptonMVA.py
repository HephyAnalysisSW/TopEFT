''' Implementation of lepton MVA 2016/17 for TopEFT 
'''

# Standard imports
import ROOT
import array
import os
from math import log

# Logging
import logging
logger = logging.getLogger(__name__)

class MVAVar:
    def __init__(self, name, func):
        self.name = name
        self.func = func
        self.var  = array.array('f',[0.])

class leptonMVA:

    def __init__(self,  year):
        if year == 2016:
            self.el_file = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/leptonMVA/ttv/el_BDTG_TTV_2016.weights.xml"
            self.mu_file = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/leptonMVA/ttv/mu_BDTG_TTV_2016.weights.xml"

            self.commonVars = [ 
                MVAVar("pt",lambda lep: lep['pt']),
                MVAVar("eta",lambda lep: abs(lep['eta'])),
                MVAVar("trackMultClosestJet",lambda lep: lep['trackMult']),
                MVAVar("miniIsoCharged",lambda lep: lep['miniRelIsoCharged']),
                MVAVar("miniIsoNeutral",lambda lep: lep['miniRelIsoNeutral']),
                MVAVar("pTRel", lambda lep: lep['jetPtRelv2']),
                MVAVar("ptRatio", lambda lep: min(lep['jetPtRatiov2'], 1.5)),
                MVAVar("relIso", lambda lep: lep['relIso03']),
                MVAVar("deepCsvClosestJet", lambda lep: max( lep['jetBTagDeepCSV'] ,0.)),
                MVAVar("sip3d",lambda lep: lep['sip3d']),
                MVAVar("dxy",lambda lep: log(abs(lep['dxy']))),
                MVAVar("dz", lambda lep: log(abs(lep['dz']))),
            ]
            self.el_vars = self.commonVars + [
                MVAVar("electronMva",lambda lep: lep['mvaIdSpring16']),
            ]
            self.mu_vars = self.commonVars + [
                MVAVar("segmentCompatibility",lambda lep: lep['segmentCompatibility']),
            ]
 
            
        elif year == 2017:
            self.el_file = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/leptonMVA/ttv/el_BDTG_TTV_2017.weights.xml"
            self.mu_file = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/leptonMVA/ttv/mu_BDTG_TTV_2017.weights.xml"

            self.commonVars = [ 
                MVAVar("pt",lambda lep: lep['pt']),
                MVAVar("eta",lambda lep: abs(lep['eta'])),
                MVAVar("trackMultClosestJet",lambda lep: lep['trackMult']),
                MVAVar("miniIsoCharged",lambda lep: lep['miniRelIsoCharged']),
                MVAVar("miniIsoNeutral",lambda lep: lep['miniRelIsoNeutral']),
                MVAVar("pTRel", lambda lep: lep['jetPtRelv2']),
                MVAVar("ptRatio", lambda lep: min(lep['jetPtRatiov2'], 1.5)),
                MVAVar("relIso", lambda lep: lep['relIso03']),
                MVAVar("deepCsvClosestJet", lambda lep: max( lep['jetBTagDeepCSV'] ,0.)),
                MVAVar("sip3d",lambda lep: lep['sip3d']),
                MVAVar("dxy",lambda lep: log(abs(lep['dxy']))),
                MVAVar("dz", lambda lep: log(abs(lep['dz']))),
            ]
            self.el_vars = self.commonVars + [
                MVAVar("electronMvaFall17NoIso",lambda lep: lep["mvaIdFall17noIso"]),
            ]
            self.mu_vars = self.commonVars + [
                MVAVar("segmentCompatibility",lambda lep: lep['segmentCompatibility']),
            ]   
        else:
            raise NotImplementedError

        # Make readers & add variables
        self.el_reader = ROOT.TMVA.Reader("Silent")
        for mvavar in self.el_vars:
            self.el_reader.AddVariable(mvavar.name, mvavar.var)
        self.mu_reader = ROOT.TMVA.Reader("Silent")
        for mvavar in self.mu_vars:
            self.mu_reader.AddVariable(mvavar.name, mvavar.var)

        # Load XML files
        self.el_reader.BookMVA("mvaTTV", os.path.expandvars(self.el_file))
        self.mu_reader.BookMVA("mvaTTV", os.path.expandvars(self.mu_file))

    def __call__( self, lep ):
        if abs(lep['pdgId'])==11:
            for mvavar in self.el_vars:
                mvavar.var[0] = mvavar.func(lep)
#                print 'e', mvavar.name, mvavar.func(lep)
#            print 'e mva', self.el_reader.EvaluateMVA("mvaTTV")  
#            print
            return self.el_reader.EvaluateMVA("mvaTTV")
        elif abs(lep['pdgId'])==13:
            for mvavar in self.mu_vars:
                mvavar.var[0] = mvavar.func(lep)
#                print 'm', mvavar.name, mvavar.func(lep)
#            print 'mu mva', self.mu_reader.EvaluateMVA("mvaTTV")  
#            print
            return self.mu_reader.EvaluateMVA("mvaTTV")
        else:
            raise NotImplementedError
