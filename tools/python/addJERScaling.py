def addJERScaling(j):
    # from https://twiki.cern.ch/twiki/bin/view/CMS/JetResolution
    available = 1 if j['mcPt']>0 else 0

    for var, pf in [[0,''],[-1,'Down'],[+1,'Up']]:
        delta = j['pt']-j['mcPt']
        if   abs(j['eta']) > 3.2: j['pt_JER'+pf] = j['pt'] + available*(-1+1.320 + var * 0.286)*delta
        elif abs(j['eta']) > 3.0: j['pt_JER'+pf] = j['pt'] + available*(-1+1.303 + var * 0.111)*delta
        elif abs(j['eta']) > 2.5: j['pt_JER'+pf] = j['pt'] + available*(-1+1.343 + var * 0.123)*delta
        elif abs(j['eta']) > 1.9: j['pt_JER'+pf] = j['pt'] + available*(-1+1.126 + var * 0.094)*delta
        elif abs(j['eta']) > 1.3: j['pt_JER'+pf] = j['pt'] + available*(-1+1.106 + var * 0.030)*delta
        elif abs(j['eta']) > 0.8: j['pt_JER'+pf] = j['pt'] + available*(-1+1.088 + var * 0.029)*delta
        else:                     j['pt_JER'+pf] = j['pt'] + available*(-1+1.061 + var * 0.023)*delta

#  ptscale = max(0.0, (jetpt + (factor-1)*(jetpt-genpt))/jetpt)
#  #print "get with pt %.1f (gen pt %.1f, ptscale = %.3f)" % (jetpt,genpt,ptscale)
#  jet.deltaMetFromJetSmearing = [ -(ptscale-1)*jet.rawFactor()*jet.px(), -(ptscale-1)*jet.rawFactor()*jet.py() ]
