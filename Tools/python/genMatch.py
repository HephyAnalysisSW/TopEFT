
def getGenMatch(lepton, genParticles):

    # Defaults
    match       = None
    minDeltaR   = 9999.
    isPrompt    = False

    # Filter
    genParticles = [ p for p in genParticles if (abs(p['pdgId'])==abs(lepton['pdgId']) or p['pdgId']==22)  ]

    # Loop
    for p in genParticles:
        dR = deltaR(l, p) 
        if dR < minDeltaR:
            match, minDeltaR = p, dR
            print match, dR
    

    if match:
        return genParticle, isPrompt
    else:
        return False


