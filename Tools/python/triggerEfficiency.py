import ROOT
import os

class triggerEfficiency:
    def __init__(self, year):
        ''' apply constant SF to leading lepton, if SF is larger than uncertainty inflate uncertainty accordingly
        '''

        self.unc = 0.01 # updated because 2% was considered too conservative.
        if year == 2016:
            self.maxPt   = 120.
            self.SF      = 0.985
            self.inflUnc = max( [ 1- self.SF, self.unc] )
        if year == 2017:
            self.maxPt   = 80.
            self.SF      = 0.966
            self.inflUnc = max( [1 - self.SF, self.unc] )

    def getSF(self, leptons):
        if len(leptons)==0 : return 1
        if leptons[0]['pt'] < self.maxPt:
            return (self.SF, self.inflUnc)
        else:
            return (1, self.unc)

