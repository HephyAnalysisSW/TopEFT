from TopEFT.analysis.Region import Region

def getRegionsFromThresholds(var, vals, gtLastThreshold = True):
    return [Region(var, (vals[i], vals[i+1])) for i in range(len(vals)-1)]

def getRegions2D(varOne, varOneThresholds, varTwo, varTwoThresholds):
    regions_varOne  = getRegionsFromThresholds(varOne,  varOneThresholds)
    regions_varTwo  = getRegionsFromThresholds(varTwo, varTwoThresholds)

    regions2D = []
    for r1 in regions_varOne:
        for r2 in regions_varTwo:
            regions2D.append(r1+r2)

    return regions2D



#Put all sets of regions that are used in the analysis, closure, tables, etc.
regionsA = [ Region("Z_pt", (0, 200)), Region("Z_pt", (200, 400)), Region("Z_pt", (400, -1)) ] # first sensitivity study
regionsB = getRegions2D("Z_pt", [0,100,200,-1], "cosThetaStar", [-1,-0.6, 0.6, 1])
regionsC = getRegions2D("Z_pt", [0,100,200,-1], "abs(cosThetaStar)", [0, 0.6, 1])
regionsD = [ Region("Z_pt", (0, 100)), Region("Z_pt", (100, 200)), Region("Z_pt", (200, -1)) ]
regionsE = getRegions2D("Z_pt", [0,100,200,400,-1], "cosThetaStar", [-1,-0.6, 0.6, 1]) # best results
regionsF = getRegions2D("Z_pt", [0,100,200,400], "cosThetaStar", [-1,-0.6, 0.6, 1]) + [Region("Z_pt", (400, -1))]
regionsG = getRegions2D("Z_pt", [0,100,200,400,-1], "lep_pt[2]", [0,30, 60, -1])
regionsH = getRegions2D("Z_pt", [0,100,200,400,-1], "lep_pt[Z_l2_index]", [0, 30, 60, -1])

