import copy
from TopEFT.Tools.helpers import deltaR, deltaR2
from TopEFT.Tools.mcTools import *

# comparing floats
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def getGenMatch(lepton, genParticles):

    # Defaults
    match       = None
    matchType   = None
    minDeltaR   = 9999.
    isPrompt    = False

    # the full information of the gen match isn't stored in CMG by default. Use mcPt to find all potential matches
    nReferenceMatches = 0
    referenceMatches = []
    for p in genParticles:
        if isclose(p['pt'], lepton['mcPt']):
            referenceMatches.append(p)
            nReferenceMatches += 1
    
    # go through all possible reference matches. the right one should be the one on top of the hierarchy that has the right pdgId
    lastMatch = None
    if nReferenceMatches > 0:
        for refMatch in reversed(referenceMatches):
            if (refMatch['pdgId'] == lepton['pdgId']):# and (lastMatch['pdgId'] == refMatch['pdgId']):
                lastMatch   = refMatch
    
    if lastMatch:
        match       = lastMatch
        isPrompt    = match["isPromptHard"]
        minDeltaR   = 0
        matchType   = "reference"
    
    # if no match by reference is found, do geometrical matching
    if not match:
        genParts = [ p for p in genParticles if abs(p['pdgId'])==abs(lepton['pdgId']) ]
        for p in genParts:
            dR = deltaR(lepton, p) 
            if dR < minDeltaR:
                match, minDeltaR = p, dR
                matchType = "geometric"
                #print match, dR
        if match:
            isPrompt = match["isPromptHard"]
            if abs(match['motherId']) == 15:
                # get the right mother
                if abs(genParticles[match['motherIndex1']]['pdgId']) == 15: motherIndex = match['motherIndex1']
                elif abs(genParticles[match['motherIndex2']]['pdgId']) == 15: motherIndex = match['motherIndex2']
                if genParticles[motherIndex]['isPromptHard']:
                    isPrompt = genParticles[motherIndex]['isPromptHard']
    
    if minDeltaR > 0.2:
        genParts = [ p for p in genParticles if p['pdgId']==22 ]
        for p in genParts:
            dR = deltaR(lepton, p) 
            if dR < minDeltaR:
                match, minDeltaR = p, dR
                matchType = "photon"
                isPrompt = match['isPromptHard']

    return match, isPrompt, matchType

