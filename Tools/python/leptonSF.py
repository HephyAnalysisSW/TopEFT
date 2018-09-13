import ROOT
from TopEFT.Tools.helpers import getObjFromFile
from TopEFT.Tools.u_float import u_float
import os
from math import sqrt

from TopEFT.Tools.leptonTrackingEfficiency import *

## maps for electrons ##
maps_ele = {\
    2016: {\
            'loose':    [("scaleFactors_ele_2016.root",  "EleToTTVLoose")],
            'tight_3l': [("scaleFactors_ele_2016.root",  "EleToTTVLeptonMvattZ3l")],
            'tight_4l': [("scaleFactors_ele_2016.root",  "EleToTTVLeptonMvattZ4l")],
            'tight_SS': [("scaleFactors_ele_2016.root",  "EleToTTVLeptonMvattW"),
                         ("scaleFactors_ele_2016.root",  "EleToTTVLeptonMvattWTightCharge")],
            },
    2017: {\
            'loose':    [("scaleFactors_ele_2017.root",  "EleToTTVLoose")],
            'tight_3l': [("scaleFactors_ele_2017.root",  "EleToTTVLeptonMvattZ3l")],
            'tight_4l': [("scaleFactors_ele_2017.root",  "EleToTTVLeptonMvattZ4l")],
            'tight_SS': [("scaleFactors_ele_2017.root",  "EleToTTVLeptonMvattW"),
                         ("scaleFactors_ele_2017.root",  "EleToTTVLeptonMvattWTightCharge")],
            },
    }

## maps for muons ##
maps_mu = {\
    2016: {\
            'loose':    [("scaleFactors_mu_2016.root",  "MuonToTTVLoose")],
            'tight_3l': [("scaleFactors_mu_2016.root",  "MuonToTTVLeptonMvattZ3l")],
            'tight_4l': [("scaleFactors_mu_2016.root",  "MuonToTTVLeptonMvattZ4l")],
            'tight_SS': [("scaleFactors_mu_2016.root",  "MuonToTTVLeptonMvattW"),
                         ("scaleFactors_mu_2016.root",  "MuonTotkSigmaPtOverPtCut")],
            },
    2017: {\

            'loose':    [("scaleFactors_mu_2017.root",  "MuonToTTVLoose")],
            'tight_3l': [("scaleFactors_mu_2017.root",  "MuonToTTVLeptonMvattZ3l")],
            'tight_4l': [("scaleFactors_mu_2017.root",  "MuonToTTVLeptonMvattZ4l")],
            'tight_SS': [("scaleFactors_mu_2017.root",  "MuonToTTVLeptonMvattW"),
                         ("scaleFactors_mu_2017.root",  "MuonTotkSigmaPtOverPtCut")],
            },
    }


class leptonSF:
    def __init__(self, year, ID = None):
        self.dataDir = "$CMSSW_BASE/src/TopEFT/Tools/data/leptonSFData"
        self.year = year
        self.LSF = leptonTrackingEfficiency(self.year)
        if not ID in maps_ele[year].keys():
            raise Exception("Don't know ID %s"%ID)
        self.mu         = [getObjFromFile(os.path.expandvars(os.path.join(self.dataDir, file)), key) for (file, key) in maps_mu[year][ID]]
        #self.mu_stat    = [getObjFromFile(os.path.expandvars(os.path.join(self.dataDir, file)), key+'_stat') for (file, key) in maps_mu[year][ID]]
        #self.mu_sys     = [getObjFromFile(os.path.expandvars(os.path.join(self.dataDir, file)), key+'_sys') for (file, key) in maps_mu[year][ID]]
        self.ele        = [getObjFromFile(os.path.expandvars(os.path.join(self.dataDir, file)), key) for (file, key) in maps_ele[year][ID]]
        self.ele_stat   = [getObjFromFile(os.path.expandvars(os.path.join(self.dataDir, file)), key+'_stat') for (file, key) in maps_ele[year][ID]]
        self.ele_sys    = [getObjFromFile(os.path.expandvars(os.path.join(self.dataDir, file)), key+'_sys') for (file, key) in maps_ele[year][ID]]
        for effMap in self.mu + self.ele: assert effMap

    def getPartialSF(self, effMap, pt, eta):
        sf  = effMap.GetBinContent(effMap.GetXaxis().FindBin(pt), effMap.GetYaxis().FindBin(eta))
        err = effMap.GetBinError(  effMap.GetXaxis().FindBin(pt), effMap.GetYaxis().FindBin(eta))
        return u_float(sf, err)

    def mult(self, l):
        if len(l) > 0:
            res = l[0]
            for i in l[1:]: res = res*i
        else: res = u_float(1)
        return res

    def getSF(self, pdgId, pt, eta, unc='sys', sigma=0):
        # electrons always use supercluster eta.
        # TrackingSF.
        trackingSF = self.LSF.getSF(pdgId, pt, eta)

        # LeptonSF. for electrons in 2016 use eta instead of abs(eta)
        eta = eta if ( self.year == 2016 and abs(pdgId) == 11 ) else abs(eta)
        if abs(pdgId)==13:
          if pt >= 120: pt = 119 # last bin is valid to infinity
          effMaps = self.mu # self.mu_sys if unc == 'sys' else self.mu_stat
          sf = self.mult([self.getPartialSF(effMap, pt, eta) for effMap in effMaps])
        elif abs(pdgId)==11:
          if pt >= 200: pt = 199 # last bin is valid to infinity
          effMaps = self.ele_sys if unc == 'sys' else self.ele_stat
          sf = self.mult([self.getPartialSF(effMap, pt, eta) for effMap in effMaps])
        else: 
          raise Exception("Lepton SF for PdgId %i not known"%pdgId)

        # Get the final scale-factor
        sf = sf*trackingSF
        return sf.val+sf.sigma*sigma

