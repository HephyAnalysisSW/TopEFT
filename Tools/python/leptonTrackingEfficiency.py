import ROOT
from TopEFT.Tools.helpers import getObjFromFile
import os, math

# Logging
import logging
logger = logging.getLogger(__name__)

class leptonTrackingEfficiency:
    def __init__(self, year):

        self.year = year

        if self.year == 2016:
            ## Electrons
            e_file   = '$CMSSW_BASE/src/TopEFT/Tools/data/leptonSFData/EGamma_Run2016_passingRECO.root'
            e_key    = "EGamma_SF2D"
            m_file   = '$CMSSW_BASE/src/TopEFT/Tools/data/leptonSFData/Muon_Run2016_passingRECO.root'
            m_key    = "ratio_eff_eta3_dr030e030_corr"

            self.e_sf = getObjFromFile(os.path.expandvars(e_file),   e_key)
            assert self.e_sf, "Could not load ele SF histo %s from file %s."%( e_key, e_file )

            self.e_ptMax = self.e_sf.GetYaxis().GetXmax()
            self.e_ptMin = self.e_sf.GetYaxis().GetXmin()

            self.e_etaMax = self.e_sf.GetXaxis().GetXmax()
            self.e_etaMin = self.e_sf.GetXaxis().GetXmin()


            ## Muons
            self.m_sf = getObjFromFile(os.path.expandvars(m_file),   m_key)
            assert self.m_sf, "Could not load muon SF histo %s from file %s."%( m_key, m_file )

            self.m_etaMax = self.m_sf.GetXaxis().GetXmax()
            self.m_etaMin = self.m_sf.GetXaxis().GetXmin()
        
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
            # Nothing availbale yet


    def getSF(self, pdgId, pt, eta):

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
                if self.year == 2016:
                    # in 2016 SFs for pt < 20 are similar to pt > 20
                    pt_forVal = self.e_ptMin + 1
                elif self.year == 2017:
                    # in 2017 there's a seperate hist for low pt electrons
                    if pt < self.e_ptMin_lowEt:
                        pt_forVal = self.e_ptMin_lowEt + 1
                    else:
                        pt_forVal = pt
                    sf_hist = self.e_sf_lowEt
            else:
                pt_forVal = pt

            val     = sf_hist.GetBinContent( sf_hist.FindBin(eta, pt_forVal) )
            valErr  = sf_hist.GetBinError( sf_hist.FindBin(eta, pt_forVal) )
            
            if not (20 < pt < 80) and self.year == 2016: addUnc = 0.01 * val # Additional 1% on ele with pt > 80 or pt < 20 in 2016
            else: addUnc = 0.
                
            valErr = math.sqrt(valErr**2 + addUnc**2)

            return (val, valErr)

        elif abs(pdgId)==13:
            if self.year == 2017:
                return (1,0)
            else:
                if not eta<=self.m_etaMax:
                    logger.warning( "Muon eta out of bounds: %3.2f (need %3.2f <= eta <=% 3.2f)", eta, self.m_etaMin, self.m_etaMax )
                    eta = self.m_etaMax
                if not eta>=self.m_etaMin:
                    logger.warning( "Muon eta out of bounds: %3.2f (need %3.2f <= eta <=% 3.2f)", eta, self.m_etaMin, self.m_etaMax )
                    eta = self.m_etaMin

                val = self.m_sf.Eval( eta )
                valErr = 0. # Systematic uncertainty not there yet

                return (val, valErr)

        else:
            raise ValueError( "Lepton pdgId %i neither electron or muon"%pdgId )


