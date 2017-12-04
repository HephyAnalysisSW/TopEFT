from TopEFT.Tools.objectSelection import getGenPartsAll

def getGenZ(genparts):
  for g in genparts:
    if g['pdgId'] != 23:        continue					# pdgId == 23 for Z
    if g['status'] != 62:	continue					# status 62 is last gencopy before it decays into ll/nunu
    return g
  return None

def getGenPhoton(genparts):
  for g in genparts:								# Type 0: no photon
    if g['pdgId'] != 22:        continue					# pdgId == 22 for photons
    if g['status'] != 23:	continue					# for photons, take status 23
    return g
  return None
