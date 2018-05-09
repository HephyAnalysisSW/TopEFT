channels          = ['3mu', '2mu1e', '2e1mu', '3e']
allChannels       = ['all'] + channels

class channel:
    def __init__(nElectrons=-1, nMuons=-1):
        self.nE = nElectrons
        self.nM = nMuons
        if nElectrons >= 0 and nMuons >= 0:
            self.name = "Mu"*self.nM + "E"*self.nM
        else:
            self.name = "all"

trilepChannels      = [channel(3,0), channel(2,1), channel(1,2), channel(0,3)]
allTrilepChannels   = [channel(-1,-1)] + trilep

quadlepChannels     = [channel(4,0), channel(3,1), channel(2,2), channel(1,3), channel(0,4)]
allQuadlepChannels  = [channel(-1,-1)] + trilep

from TopEFT.Tools.helpers import mZ
def getZCut(mode, var, zMassRange=15):
    zstr = "abs(%s - %s)"%(var, mZ)
    if mode.lower()=="onz": return zstr+"<="+str(zMassRange)
    if mode.lower()=="offz": return zstr+">"+str(zMassRange)
    return "(1)"

