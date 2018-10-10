import ROOT
from TopEFT.Tools.helpers import getObjFromFile
import os, math
from TopEFT.Tools.u_float import *

# Logging
import logging
logger = logging.getLogger(__name__)

class leptonTrackingEfficiency:
    def __init__(self, year):

        self.year = year

        if self.year == 2016:
            ## Electrons
            e_file          = '$CMSSW_BASE/src/TopEFT/Tools/data/leptonSFData/EGamma_Run2016BtoH_passingRECO_Legacy2016.root'
            e_file_lowEt    = '$CMSSW_BASE/src/TopEFT/Tools/data/leptonSFData/EGamma_Run2016BtoH_passingRECO_lowEt_Legacy2016.root'
            e_key           = "EGamma_SF2D"
            m_file   = '$CMSSW_BASE/src/TopEFT/Tools/data/leptonSFData/Muon_Run2016_passingRECO.root'
            m_key    = "ratio_eff_eta3_dr030e030_corr"

            self.e_sf = getObjFromFile(os.path.expandvars(e_file),   e_key)
            self.e_sf_lowEt = getObjFromFile(os.path.expandvars(e_file_lowEt),   e_key)
            assert self.e_sf, "Could not load ele SF histo %s from file %s."%( e_key, e_file )
            assert self.e_sf_lowEt, "Could not load ele SF histo %s from file %s."%( e_key, e_file_lowEt )


            self.e_ptMax = self.e_sf.GetYaxis().GetXmax()
            self.e_ptMin = self.e_sf.GetYaxis().GetXmin()
            self.e_ptMin_lowEt = self.e_sf_lowEt.GetYaxis().GetXmin()

            self.e_etaMax = self.e_sf.GetXaxis().GetXmax()
            self.e_etaMin = self.e_sf.GetXaxis().GetXmin()


            ## Muons
            # SFs are 1. https://hypernews.cern.ch/HyperNews/CMS/get/muon/1425/1.html
        
        elif self.year == 2017:
            ## Electrons
            e_file          = '$CMSSW_BASE/src/TopEFT/Tools/data/leptonSFData/EGamma_Run2017BCDEF_passingRECO.root'
            e_file_lowEt    = '$CMSSW_BASE/src/TopEFT/Tools/data/leptonSFData/EGamma_Run2017BCDEF_passingRECO_lowEt.root'
            e_key           = "EGamma_SF2D"
            
            self.e_sf       = getObjFromFile(os.path.expandvars(e_file),   e_key)
            self.e_sf_lowEt = getObjFromFile(os.path.expandvars(e_file_lowEt),   e_key)
            assert self.e_sf, "Could not load ele SF histo %s from file %s."%( e_key, e_file )
            assert self.e_sf_lowEt, "Could not load ele SF histo %s from file %s."%( e_key, e_file_lowEt )

            self.e_ptMax = self.e_sf.GetYaxis().GetXmax()
            self.e_ptMin = self.e_sf.GetYaxis().GetXmin()
            self.e_ptMin_lowEt = self.e_sf_lowEt.GetYaxis().GetXmin()

            self.e_etaMax = self.e_sf.GetXaxis().GetXmax()
            self.e_etaMin = self.e_sf.GetXaxis().GetXmin()
            
            
            ## Muons
            # SFs are 1. https://hypernews.cern.ch/HyperNews/CMS/get/muon/1425/1.html


    def getSF(self, pdgId, pt, eta, sigma=0):

        if abs(pdgId)==11:
            if not (eta<=self.e_etaMax):
                logger.warning( "Supercluster eta out of bounds: %3.2f (need %3.2f <= eta <=% 3.2f)", eta, self.e_etaMin, self.e_etaMax )
                eta = self.e_etaMax
            if not (eta>=self.e_etaMin):
                logger.warning( "Supercluster eta out of bounds: %3.2f (need %3.2f <= eta <=% 3.2f)", eta, self.e_etaMin, self.e_etaMax )
                eta = self.e_etaMin

            # this is a bit awkward because of the seperate SFs for low pt electrons
            sf_hist = self.e_sf
            if pt >= self.e_ptMax:
                pt_forVal = self.e_ptMax - 1 
            elif pt <= self.e_ptMin:
                if pt < self.e_ptMin_lowEt:
                    pt_forVal = self.e_ptMin_lowEt + 1
                else:
                    pt_forVal = pt
                sf_hist = self.e_sf_lowEt
            else:
                pt_forVal = pt

            val     = sf_hist.GetBinContent( sf_hist.FindBin(eta, pt_forVal) )
            valErr  = sf_hist.GetBinError( sf_hist.FindBin(eta, pt_forVal) )
            
            return val + sigma*valErr

        elif abs(pdgId)==13:
            return 1

        else:
            raise ValueError( "Lepton pdgId %i neither electron or muon"%pdgId )


