import ROOT, array
from math import pi, sqrt, cos, sin

#wrapper class for MT2 variables
class mt2Calculator:
    def __init__(self):
        ROOT.gROOT.ProcessLine(".L $CMSSW_BASE/src/TopEFT/Tools/scripts/mt2_bisect.cpp+")
        self.mt2 = ROOT.mt2()
        self.reset()
        self.leptonMass = 0.
        self.bjetMass = 0.
        self.mt2Mass_ll   = 0.   #probe mass for the daughter system
        self.mt2Mass_bb   = 80.4 #probe mass for the daughter system
        self.mt2Mass_blbl = 0.   #probe mass for the daughter system
    def reset(self):
        self.met=None
        self.lepton1=None
        self.lepton2=None
        self.bjet1=None
        self.bjet2=None

#Setters
    def setMet(self, pt, phi):
        self.met = ROOT.TVector2(pt*cos(phi), pt*sin(phi))
    def setLepton1(self, pt1, eta1, phi1):
        self.lepton1 = ROOT.TLorentzVector()
        self.lepton1.SetPtEtaPhiM(pt1, eta1, phi1, self.leptonMass)
    def setLepton2(self, pt2, eta2, phi2):
        self.lepton2 = ROOT.TLorentzVector()
        self.lepton2.SetPtEtaPhiM(pt2, eta2, phi2, self.leptonMass)
    def setLeptons(self, pt1, eta1, phi1, pt2, eta2, phi2):
        self.setLepton1(pt1,eta1,phi1)
        self.setLepton2(pt2,eta2,phi2)
    def setBJet1(self, pt1, eta1, phi1):
        self.bjet1 = ROOT.TLorentzVector()
        self.bjet1.SetPtEtaPhiM(pt1, eta1, phi1, self.bjetMass)
    def setBJet2(self, pt2, eta2, phi2):
        self.bjet2 = ROOT.TLorentzVector()
        self.bjet2.SetPtEtaPhiM(pt2, eta2, phi2, self.bjetMass)
    def setBJets(self, pt1, eta1, phi1, pt2, eta2, phi2):
        self.setBJet1(pt1,eta1,phi1)
        self.setBJet2(pt2,eta2,phi2)

#Traditional MT2
    def mt2ll(self):
        assert self.met and self.lepton1 and self.lepton2, "Incomplete specification, need met/lepton1/lepton2"
        pmiss  = array.array('d',[  0., self.met.Px(), self.met.Py()] )
        l1     = array.array('d',[  0., self.lepton1.Px(), self.lepton1.Py()] )
        l2     = array.array('d',[  0., self.lepton2.Px(), self.lepton2.Py()] )
        self.mt2.set_mn(self.mt2Mass_ll)
        self.mt2.set_momenta(l1, l2, pmiss)
        return self.mt2.get_mt2()
#MT2bb (treating leptons invisibly, endpoint at top mass)
    def mt2bb(self):
        assert self.met and self.lepton1 and self.lepton2 and self.bjet1 and self.bjet2, "Incomplete specification, need met/lepton1/lepton2/bjet1/bjet2"
        pmiss_vec = self.met+ROOT.TVector2(self.lepton1.Px()+self.lepton2.Px(), self.lepton1.Py()+self.lepton2.Py())
        pmiss  = array.array('d',[  0., pmiss_vec.Px(), pmiss_vec.Py()] )
        b1     = array.array('d',[  0., self.bjet1.Px(), self.bjet1.Py()] )
        b2     = array.array('d',[  0., self.bjet2.Px(), self.bjet2.Py()] )
        self.mt2.set_mn(self.mt2Mass_bb)
        self.mt2.set_momenta(b1, b2, pmiss)
        return self.mt2.get_mt2()
#MT2blbl (Brians variant)
    def mt2blbl(self, strategy="minMaxMass"):
        assert self.met and self.lepton1 and self.lepton2 and self.bjet1 and self.bjet2, "Incomplete specification, need met/lepton1/lepton2/bjet1/bjet2"

        #select lepton/bjet pairing by minimizing maximum mass
        if strategy=="minMaxMass":
            max1 = max([(self.lepton1 + self.bjet1).M(), (self.lepton2 + self.bjet2).M()])
            max2 = max([(self.lepton1 + self.bjet2).M(), (self.lepton2 + self.bjet1).M()])
            if max1<max2: #Choose pairing with smaller invariant mass
                bl1,bl2 = self.lepton1+self.bjet1, self.lepton2+self.bjet2
            else:
                bl1,bl2 = self.lepton1+self.bjet2, self.lepton2+self.bjet1
        else:
            assert False, "only minMaxMass implemented"

        pmiss  = array.array('d',[  0., self.met.Px(), self.met.Py()] )
        bl1     = array.array('d',[  0., bl1.Px(), bl1.Py()] )
        bl2     = array.array('d',[  0., bl2.Px(), bl2.Py()] )
        self.mt2.set_mn(self.mt2Mass_blbl)
        self.mt2.set_momenta(bl1, bl2, pmiss)
        return self.mt2.get_mt2()
