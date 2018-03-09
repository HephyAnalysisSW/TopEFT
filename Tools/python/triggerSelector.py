class triggerSelector:
    def __init__(self, year):
        if year == 2016:
            self.mmm    = ["HLT_TripleMu_12_10_5"]
            self.mm     = ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ","HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ"]
            self.m      = ["HLT_SingleMuTTZ"]
            self.eee    = ["HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL"]
            self.ee     = ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ"]
            self.e      = ["HLT_SingleEleTTZ"]
            self.em     = ["HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL", "HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ"]
            self.eem    = ["HLT_Mu8_DiEle12_CaloIdL_TrackIdL"]
            self.emm    = ["HLT_DiMu9_Ele9_CaloIdL_TrackIdL"]
        elif year == 2017:
            raise NotImplementedError
        else:
            raise NotImplementedError

        self.DoubleMuon     = "(%s)"%"||".join(self.mmm + self.mm)
        self.DoubleEG       = "(%s)"%"||".join(self.eee + self.ee)
        self.MuonEG         = "(%s)"%"||".join(self.em + self.eem + self.emm)
        self.SingleMuon     = "(%s)"%"||".join(self.m)
        self.SingleElectron = "(%s)"%"||".join(self.e)

        self.PDHierarchy = [ "DoubleMuon", "DoubleMuon", "DoubleEG", "MuonEG", "SingleMuon", "SingleElectron" ]



    def getVeto(self, cutString):
        return "!%s"%cutString

    def getSelection(self, PD):
        found = False
        cutString = ""
        for x in reversed(self.PDHierarchy):
            if found:
                cutString += "&&%s"%self.getVeto(getattr(self,x))
            if x in PD:# == getattr(self, PD):
                found = True
                cutString = getattr(self, x)

        return cutString

