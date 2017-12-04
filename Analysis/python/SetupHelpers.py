channels          = ['3mu', '2mu1e', '2e1mu', '3e']
allChannels       = ['all'] + channels

from TopEFT.Tools.helpers import mZ
def getZCut(mode, zMassRange=15):
    zstr = "abs(Z_mass - "+str(mZ)+")"
    if mode.lower()=="onz": return zstr+"<="+str(zMassRange)
    if mode.lower()=="offz": return zstr+">"+str(zMassRange)
    return "(1)"

