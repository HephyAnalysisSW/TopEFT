from TopEFT.analysis.Region import Region

def getRegions2D(njetThresholds, nbtagThresholds):
    regions_njet    = getRegionsFromThresholds('njet',  njetThresholds)
    regions_nbtag   = getRegionsFromThresholds('nBTag', nbtagThresholds)

    regions2D = []
    for r1 in regions_nbtag:
        for r2 in regions_njet:
            regions2D.append(r1+r2)

    return regions2D

#Put all sets of regions that are used in the analysis, closure, tables, etc.
regionsA = [ Region("Z_pt", (0, 200)), Region("Z_pt", (200, 400)), Region("Z_pt", (400, -1)) ]

#regionsTTZ = 

