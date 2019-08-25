''' Functions for top pt reweighting
'''
from math import exp, sqrt

#https://indico.cern.ch/event/463433/contribution/5/attachments/1193635/1733505/MSavitskyi_ToppTRew13TeV_TopModGen.pdf
#updated a and b parameters for 13 TeV: https://twiki.cern.ch/twiki/bin/view/CMS/TopSystematics#pt_top_Reweighting


def getCRWeight(njets):
    if njets < 3:
        return 1.
    elif njets == 3:
        return (1-0.0122834751382)
    elif njets == 4:
        return 1+0.00650110282004
    elif njets >= 5:
        return 1+0.0272257402539
    
def getCRDrawString():
    nJetString = "Sum$(Jet_pt>30&&abs(Jet_eta)<2.4&&Jet_id16>0)"
    return "(1*(%s<3) + (1-0.0122834751382)*(%s==3) + (1+0.00650110282004)*(%s==4) + (1+0.0272257402539)*(%s>=5))"%(nJetString, nJetString, nJetString, nJetString)

