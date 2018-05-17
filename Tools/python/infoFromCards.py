from TopEFT.Tools.u_float import u_float
import math

def getPull(nuisanceFile, name):
    with open(nuisanceFile) as f:
      for line in f:
        if name != line.split()[0]: continue
        return float(line.split(',')[0].split()[-1])
    return 0 # Sometimes a bin is not found in the nuisance file because its yield is 0

def getConstrain(nuisanceFile, name):
    with open(nuisanceFile) as f:
      for line in f:
        if name != line.split()[0]: continue
        return float(line.split(',')[1].split()[0].replace('*','').replace('!',''))
    return 0 # Sometimes a bin is not found in the nuisance file because its yield is 0


    # Returns something of the form "Bin0" if bin name (as written in the comment lines of the cards) are given
def getBinNumber(cardFile, binName):
    with open(cardFile) as f:
      for line in f:
        if binName in line: return line.split(':')[0].split()[-1]

def getFittedUncertainty(nuisanceFile, name):
    with open(nuisanceFile) as f:
      for line in f:
        if name != line.split()[0]: continue
        return float(line.split(',')[1].split()[0].replace('!','').replace('*',''))
    return 0 # Sometimes a bin is not found in the nuisance file because its yield is 0


def getPostFitUncFromCard(cardFile, estimateName, uncName, binName):
    nuisanceFile = cardFile.replace('.txt','_nuisances_full.txt')
    return getFittedUncertainty(nuisanceFile, estimateName)*getPreFitUncFromCard(cardFile, estimateName, uncName, binName)

def getPreFitUncFromCard(cardFile, estimateName, uncName, binName):
    binNumber = getBinNumber(cardFile, binName)
    with open(cardFile) as f:
      binList = False
      estimateList = False
      for line in f:
        if len(line.split())==0: continue
        if line.split()[0] == "bin":
          if not binList: binList = True
          else:           binList = line.split()[1:]
        if line.split()[0] == "process":
          if not estimateList: estimateList = line.split()[1:]
        if line.split()[0] != uncName: continue
        for i in range(len(binList)):
          if binList[i] == binNumber and estimateList[i]==estimateName:
            try:    return float(line.split()[2:][i])-1
            except: 
              return 0. # muted bin has -, cannot be converted to float
      raise Warning('No uncertainty ' + uncName + ' for ' + estimateName + ' ' + binName)

def getTotalPostFitUncertainty(cardFile, binName):
    binNumber = getBinNumber(cardFile, binName)
    with open(cardFile) as f:
      binList = False
      estimateList = False
      ind = []
      uncertainties = False
      uncDict = {}
      totalUnc = {}
      for line in f:
        if len(line.split())==0: continue
        if line.split()[0] == "bin":
          if not binList: binList = True
          else:
            binList = line.split()[1:]
            for i,b in enumerate(binList):
                if b == binName:
                    ind.append(i) 
          print ind
        if line.split()[0] == "process":
          if not estimateList:
            estimateList = line.split()[1:]
            estimateList = estimateList[ind[1]:ind[-1]+1]
        if line.split()[0] == "rate":
          estimates = line.split()[1:]
          estimates = [float(a) for a in estimates[ind[1]:ind[-1]+1]]
        if line.split()[0] == 'PU': uncertainties = True
        if uncertainties:
            uncDict[line.split()[0]] = [ 0 if a =='-' else float(a)-1 for a in line.split()[2:][ind[1]:ind[-1]+1] ]
    print estimateList
    print estimates
    nuisanceFile = cardFile.replace('.txt','_nuisances_full.txt')
    for unc in uncDict.keys():
        totalUnc[unc] = 0
        for i in range(len(estimates)):
            #totalUnc[unc] += uncDict[unc][i] * estimates[i] * ( 1 + getPull(nuisanceFile,unc)*uncDict[unc][i] ) #* getConstrain(nuisanceFile, unc)
            totalUnc[unc] += uncDict[unc][i] * estimates[i] * math.exp( getPull(nuisanceFile,unc)*uncDict[unc][i] )
            #totalUnc[unc] += (uncDict[unc][i] * estimates[i] * math.exp( getPull(nuisanceFile,unc)*uncDict[unc][i] ))**2
        if totalUnc[unc] > 0: print unc, totalUnc[unc]
        #totalUnc[unc] = math.sqrt(totalUnc[unc])
    total = 0
    for unc in totalUnc.keys():
        total += totalUnc[unc]**2
    estimatesPostFit = []
    for e in estimateList:
        res = getEstimateFromCard(cardFile, e, binName)
        res = applyAllNuisances(cardFile, e, res, binName)
        estimatesPostFit.append(res.val)
    estimatePostFit = sum(estimatesPostFit)
    return u_float(estimatePostFit,math.sqrt(total))
    #return uncDict, totalUnc
          #else: 

def getEstimateFromCard(cardFile, estimateName, binName):
    res = u_float(0)
    binNumber = getBinNumber(cardFile, binName)
    uncName = 'Stat_' + binName + '_' + estimateName
    with open(cardFile) as f:
      binList = False
      estimateList = False
      for line in f:
        if len(line.split())==0: continue
        if line.split()[0] == "bin":
          if not binList: binList = True
          else:           binList = line.split()[1:]
        if line.split()[0] == "process":
          if not estimateList: estimateList = line.split()[1:]
        if line.split()[0] == "rate":
            for i in range(len(binList)):
              if binList[i] == binNumber and estimateList[i]==estimateName:
                try: res.val = float(line.split()[1:][i])
                except: res.val = 0
                #return float(line.split()[1:][i])
        if line.split()[0] != uncName: continue
        for i in range(len(binList)):
          if binList[i] == binNumber and estimateList[i]==estimateName:
            try:    res.sigma = (float(line.split()[2:][i])-1)*res.val
            except: res.sigma = 0.
    return res

def getObservationFromCard(cardFile, binName):
    res = u_float(0)
    binNumber = getBinNumber(cardFile, binName)
    with open(cardFile) as f:
      binList = False
      estimateList = False
      for line in f:
        if len(line.split())==0: continue
        if line.split()[0] == "bin":
            binList = line.split()[1:]
        if line.split()[0] == "observation":
            for i in range(len(binList)):
              if binList[i] == binNumber:# and estimateList[i]==estimateName:
                try: res.val = float(line.split()[1:][i])
                except: res.val = 0
    return res

def applyNuisance(cardFile, estimate, res, binName):
    if not estimate.name in ['DY','multiBoson','TTZ']: return res
    uncName      = estimate.name if estimate.name != "TTZ" else 'ttZ'
    nuisanceFile = cardFile.replace('.txt','_nuisances_full.txt')
    binNumber    = getBinNumber(cardFile, binName)
    scaledRes    = res*(1+getPreFitUncFromCard(cardFile, estimate.name, uncName, binName)*getPull(nuisanceFile, uncName))
    scaledRes2   = scaledRes*(1+res.sigma/res.val*getPull(nuisanceFile, 'Stat_' + binNumber + '_' + estimate.name)) if scaledRes.val > 0 else scaledRes
    return scaledRes2

def applyAllNuisances(cardFile, estimate, res, binName, nuisances):
    if not estimate in ['signal', 'WZ', 'TTX', 'TTW', 'TZQ', 'rare', 'nonprompt', 'ZZ']: return res
    if estimate == "WZ":
        uncName = estimate+'_xsec'
    elif estimate == "WZ":
        uncName = estimate+'_xsec'
    elif estimate == "TZQ":
        uncName = "tZq"
    elif estimate == "TTX":
        uncName = "ttX"
    else:
        uncName      = estimate
    # use r=1 fits for now
    nuisanceFile = cardFile.replace('.txt','_nuisances_r1_full.txt')
    binNumber    = getBinNumber(cardFile, binName)
    if estimate == "signal" or estimate == "TTW":
        scaledRes = res
    else:
        scaledRes    = res*(1+getPreFitUncFromCard(cardFile, estimate, uncName, binName)*getPull(nuisanceFile, uncName))
    scaledRes2   = scaledRes*(1+getPreFitUncFromCard(cardFile, estimate, 'Stat_' + binNumber + '_' + estimate, binName))**getPull(nuisanceFile, 'Stat_' + binNumber + '_' + estimate) if scaledRes.val > 0 else scaledRes
    allNuisances = nuisances#["unclEn","JER","leptonSF","PU","Lumi","PDF","SFb","topPt","JEC","trigger","SFl"]
    for n in allNuisances:
        scaledRes2 = scaledRes2*(1+getPreFitUncFromCard(cardFile, estimate, n, binName))**getPull(nuisanceFile, n) if scaledRes.val > 0 else scaledRes
    return scaledRes2
