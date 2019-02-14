from TopEFT.Analysis.MCBasedEstimate              import MCBasedEstimate

class estimatorList:
    def __init__(self, setup, samples=['TTZ', 'WZ', 'TTX', 'TTW', 'ZG', 'rare', 'pseudoData', 'ZZ', 'XG','ZZZ','WZZ','WWZ','TZQ','TWZ','TTXrest','TTH','TTXX']): #rare_noZZ
        for s in samples:
            setattr(self, s, MCBasedEstimate(name="%s_%s"%(s, setup.year), sample=setup.samples[s]))
        
    def constructEstimatorList(self, samples):
        self.estimatorList = [ getattr(self, s) for s in samples ]
        return self.estimatorList

