import ROOT
from TopEFT.Tools.helpers import getObjFromFile
from TopEFT.Tools.u_float import u_float
import os
from math import sqrt

from TopEFT.Tools.leptonTrackingEfficiency import *

## maps for electrons ##
maps_ele = {\
    2016: {\
            'loose':    [("scaleFactors_ele_2016_eta.root",  "EleToTTVLoose")],
            'tight_3l': [("scaleFactors_ele_2016_eta.root",  "EleToTTVLoose"),
                         ("scaleFactors_ele_2016_eta.root",  "TTVLooseToTTVLeptonMvattZ3l")],
            'tight_4l': [("scaleFactors_ele_2016_eta.root",  "EleToTTVLoose"),
                         ("scaleFactors_ele_2016_eta.root",  "TTVLooseToTTVLeptonMvattZ4l")],
            'tight_SS': [("scaleFactors_ele_2016_eta.root",  "EleToTTVLoose"),
                         ("scaleFactors_ele_2016_eta.root",  "TTVLooseToTTVLeptonMvattW"),
                         ("scaleFactors_ele_2016_eta.root",  "TTVLeptonMvattWToTightCharge")],
            },
    2017: {\
            'loose':    [("scaleFactors_ele_2017.root",  "EleToTTVLoose")],
            'tight_3l': [("scaleFactors_ele_2017.root",  "EleToTTVLoose"),
                         ("scaleFactors_ele_2017.root",  "TTVLooseToTTVLeptonMvattZ3l")],
            'tight_4l': [("scaleFactors_ele_2017.root",  "EleToTTVLoose"),
                         ("scaleFactors_ele_2017.root",  "TTVLooseToTTVLeptonMvattZ4l")],
            'tight_SS': [("scaleFactors_ele_2017.root",  "EleToTTVLoose"),
                         ("scaleFactors_ele_2017.root",  "TTVLooseToTTVLeptonMvattW"),
                         ("scaleFactors_ele_2017.root",  "TTVLeptonMvattWToTightCharge")],
            },
    }

## maps for muons ##
maps_mu = {\
    2016: {\
            'loose':    [("scaleFactors_mu_2016.root",  "MuonToTTVLoose")],
            'tight_3l': [("scaleFactors_mu_2016.root",  "MuonToTTVLoose"),
                         ("scaleFactors_mu_2016.root",  "TTVLooseToTTVLeptonMvattZ3l")],
            'tight_4l': [("scaleFactors_mu_2016.root",  "MuonToTTVLoose"),
                         ("scaleFactors_mu_2016.root",  "TTVLooseToTTVLeptonMvattZ4l")],
            'tight_SS': [("scaleFactors_mu_2016.root",  "MuonToTTVLoose"),
                         ("scaleFactors_mu_2016.root",  "TTVLooseToTTVLeptonMvattW"),
                         ("scaleFactors_mu_2016.root",  "TTVLeptonMvattWTotkSigmaPtOverPtCut")],
            },
    2017: {\
            'loose':    [("scaleFactors_mu_2017.root",  "MuonToTTVLoose")],
            'tight_3l': [("scaleFactors_mu_2017.root",  "MuonToTTVLoose"),
                         ("scaleFactors_mu_2017.root",  "TTVLooseToTTVLeptonMvattZ3l")],
            'tight_4l': [("scaleFactors_mu_2017.root",  "MuonToTTVLoose"),
                         ("scaleFactors_mu_2017.root",  "TTVLooseToTTVLeptonMvattZ4l")],
            'tight_SS': [("scaleFactors_mu_2017.root",  "MuonToTTVLoose"),
                         ("scaleFactors_mu_2017.root",  "TTVLooseToTTVLeptonMvattW"),
                         ("scaleFactors_mu_2017.root",  "TTVLeptonMvattWTotkSigmaPtOverPtCut")],
            },
    }


class leptonSF:
    def __init__(self, year, ID = None):
        self.dataDir = "$CMSSW_BASE/src/TopEFT/Tools/data/leptonSFData"
        self.year = year
        self.LSF = leptonTrackingEfficiency(self.year)
        if not ID in maps_ele[year].keys():
            raise Exception("Don't know ID %s"%ID)
        self.mu  = [getObjFromFile(os.path.expandvars(os.path.join(self.dataDir, file)), key) for (file, key) in maps_mu[year][ID]]
        self.ele = [getObjFromFile(os.path.expandvars(os.path.join(self.dataDir, file)), key) for (file, key) in maps_ele[year][ID]]
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

    def getSF(self, pdgId, pt, eta, sigma=0):
        # electrons always use supercluster eta.
        # TrackingSF.
        trackingSF = self.LSF.getSF(pdgId, pt, eta)

        # LeptonSF. for electrons in 2016 use eta instead of abs(eta)
        eta = eta if ( self.year == 2016 and abs(pdgId) == 11 ) else abs(eta)
        if abs(pdgId)==13:
          if pt >= 120: pt = 119 # last bin is valid to infinity
          sf = self.mult([self.getPartialSF(effMap, pt, eta) for effMap in self.mu])
        elif abs(pdgId)==11:
          if pt >= 200: pt = 199 # last bin is valid to infinity
          sf = self.mult([self.getPartialSF(effMap, pt, eta) for effMap in self.ele])
        else: 
          raise Exception("Lepton SF for PdgId %i not known"%pdgId)

        # Get the final scale-factor
        sf = sf*trackingSF
        return sf.val+sf.sigma*sigma

