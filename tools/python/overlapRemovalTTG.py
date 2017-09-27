from TopEFT.tools.objectSelection import getGenPartsAll
from TopEFT.tools.helpers import deltaR


def isIsolatedPhoton(g, genparts, coneSize):
    for other in genparts:
      if other['pdgId'] == 22:        continue                                                        # Avoid photon or generator copies of it
      if other['status'] < 0:         continue                                                        # Only final state particles
      if other['pt'] < 5:             continue                                                        # pt > 5
      if deltaR(g, other) > coneSize: continue                                                        # check deltaR
      return False
    return True

# Run through parents in genparticles, and return list of their pdgId
def getParentIds(genParticles, g):
  parents = []
  if g['motherIndex1'] > 0:
    mother1 = genParticles[g['motherIndex1']]
    parents += [mother1['pdgId']] + getParentIds(genParticles, mother1)
  if g['motherIndex2'] > 0:
    mother2 = genParticles[g['motherIndex2']]
    parents += [mother2['pdgId']] + getParentIds(genParticles, mother2)
  return parents

# Check if event qualifies as TTGJets events
# Note: returns False for a few events in the TTGJets sample, probably when the photon goes undetected (mostly at lower pt's)
# Recipe is based on AN2015-165
# Gen photon pt/eta cuts taken from Madgraph card
# https://github.com/cms-sw/genproductions/blob/b0427dd453eb682bba6a84d10b5e3b4ad752c380/bin/MadGraph5_aMCatNLO/cards/production/13TeV/TTGJets_5f_NLO_FXFX/TTGJets_5f_NLO_FXFX_run_card.dat
def getTTGJetsEventType(r):
  type = 0
  genparts = getGenPartsAll(r)
  for g in genparts:                                                                                  # Type 0: no photon
    if g['pdgId'] != 22:                        continue                                              # pdgId == 22 for photons
    type = max(type, 1)                                                                               # Type 1: photon found
    if g['pt'] < 10:                            continue                                              # pt > 10 GeV
    if abs(g['eta']) > 2.6:                     continue                                              # |eta| < 2.6
    type = max(type, 2)                                                                               # Type 2: photon within generator cuts
#   if not isIsolatedPhoton(g, genparts, 0.05): continue                                              # According to MG the photon isolation is 0.05, probably too small to really apply this cut
                                                                                                      # (TTGJets has a few events where other stuff is found within 0.05 of the photon)

    parents = getParentIds(genparts, g)                                                               # Get complete parentsList
    parents = filter(lambda x: abs(x) != 2212, parents)                                               # Remove the protons from the list

    if len(parents) == 0:                          type = max(type, 3)                                # Rare, not sure what's happening here, apparently sometimes the photon has no parents or the proton as parent
    elif max(parents) < 37 and min(parents) > -37: type = max(type, 4)                                # Only quarks, leptons, gluons and bosons allowed in the parent list (i.e. we avoid photons from pions) [those are the ones which should be removed]
  return type
