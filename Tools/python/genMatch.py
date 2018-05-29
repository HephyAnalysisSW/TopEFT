import copy
from TopEFT.Tools.helpers import deltaR, deltaR2
from TopEFT.Tools.mcTools import *

# comparing floats
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def getGenMatch(lepton, genParticles):

    # Defaults
    match       = None
    minDeltaR   = 9999.
    isPrompt    = False

    # make a copy of genParticles
    allGenParticles = copy.deepcopy(genParticles)

    # the full information of the gen match isn't stored in CMG by default. Use mcPt to find all potential matches
    nReferenceMatches = 0
    referenceMatches = []
    for p in allGenParticles:
        if isclose(p['pt'], lepton['mcPt']):
            referenceMatches.append(p)
            nReferenceMatches += 1
    
    # go through all possible reference matches. the right one should be the one on top of the hierarchy that has the right pdgId
    lastMatch = None
    if nReferenceMatches > 0:
        lastMatch = referenceMatches[-1]
        for refMatch in reversed(referenceMatches):
            if (refMatch['pdgId'] == lepton['pdgId']) and (lastMatch['pdgId'] == refMatch['pdgId']):
                lastMatch   = refMatch
                #match       = 
                #minDeltaR = 0
    
    if lastMatch:
        match       = lastMatch
        minDeltaR   = 0
    else:
        if nReferenceMatches > 0:
            print "OMG I lost the reference match!!"

    # if no match by reference is found, do geometrical matching
    if not match:
        genParticles = [ p for p in allGenParticles if abs(p['pdgId'])==abs(lepton['pdgId']) ]
        for p in genParticles:
            dR = deltaR(lepton, p) 
            if dR < minDeltaR:
                match, minDeltaR = p, dR
                #print match, dR
    
        if abs(match['motherId']) == 15:
            print "############## From tau #################"
            # get the right mother
            if abs(allGenParticles[match['motherIndex1']]['pdgId']) == 15: motherIndex = match['motherIndex1']
            elif abs(allGenParticles[match['motherIndex2']]['pdgId']) == 15: motherIndex = match['motherIndex2']
            if allGenParticles[motherIndex]['isPromptHard']:
                print "Tau also prompt"
                #print allGenParticles[motherIndex]
                isPrompt = True
        del genParticles
        print "## Geometric match"
    
    if minDeltaR > 0.2:
        genParticles = [ p for p in allGenParticles if p['pdgId']==22 ]
        for p in genParticles:
            dR = deltaR(lepton, p) 
            if dR < minDeltaR:
                match, minDeltaR = p, dR
                #print match, dR
        del genParticles

    if match is None:
        print "no match found"
    else:
        if match['isPromptHard']: isPrompt = True
        # prompt from taus missing
        
        #if match['pdgId'] == 22: print "####################### Matched a photon ####################"
    if minDeltaR > 0:
        print "geometric match"
        print lepton
        print match, isPrompt, minDeltaR
    if match:
        return match, isPrompt
    else:
        return False


