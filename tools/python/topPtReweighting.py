''' Functions for top pt reweighting
'''
from math import exp, sqrt

#https://indico.cern.ch/event/463433/contribution/5/attachments/1193635/1733505/MSavitskyi_ToppTRew13TeV_TopModGen.pdf
#updated a and b parameters for 13 TeV: https://twiki.cern.ch/twiki/bin/view/CMS/TopSystematics#pt_top_Reweighting


def getUnscaledTopPairPtReweightungFunction(selection = "dilep"):
    if selection == "dilep":
        a = 0.0615
        b = -0.0005
    else:
        raise ValueError ("top pt reweighting implemented only for 'dilep' ")
    def f(topPts):
        assert len(topPts)<=2, "Found too many top pts: %i"%len(topPts)
        res=1.
        for pt in topPts:
            res*=exp(a+b*pt)
        return sqrt(res)
    return f

#https://twiki.cern.ch/twiki/bin/viewauth/CMS/TopPtReweighting
def getTopPtDrawString(selection = "dilep"):
    if selection == "dilep":
        a = 0.0615
        b = -0.0005
    else:
        raise ValueError ("top pt reweighting implemented only for 'dilep' ")

    return "sqrt(exp(Sum$(("+str(a)+"+("+str(b)+")*genPartAll_pt)*(abs(genPartAll_pdgId)==6&&genPartAll_nDaughters==2&&genPartAll_status==62&&genPartAll_pt<=400))))"

def getTopPtsForReweighting(r):
    res=[]
    for i in range(r.ngenPartAll):
        if abs(r.genPartAll_pdgId[i])==6 and r.genPartAll_nDaughters[i]==2 and r.genPartAll_status[i]==62 and r.genPartAll_pt[i]<400:
            res.append(r.genPartAll_pt[i])
    return res
