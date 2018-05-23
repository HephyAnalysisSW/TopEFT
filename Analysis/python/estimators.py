from TopEFT.Analysis.MCBasedEstimate              import MCBasedEstimate

class estimatorList:
    def __init__(self, setup, samples=['TTZ', 'WZ', 'TTX', 'TTW', 'TZQ', 'rare', 'nonprompt', 'pseudoData', 'ZZ']): #rare_noZZ
        for s in samples:
            setattr(self, s, MCBasedEstimate(name=s, sample=setup.samples[s]))
        
    def constructEstimatorList(self, samples):
        self.estimatorList = [ getattr(self, s) for s in samples ]
        return self.estimatorList

