from TopEFT.analysis.MCBasedEstimate              import MCBasedEstimate

from SetupHelpers import channels 
from Setup import Setup, otherEWKComponents
from TopEFT.analysis.Region import Region
setup = Setup()

estimators = {}

## Data-driven estimators
# non so far

## main MC based estimators
for mc in ['TTZtoLLNuNu', 'WZ', 'TTX', 'TTW', 'TZQ', 'rare', 'nonprompt']:
    estimators[mc] = [MCBasedEstimate(name=mc, sample=setup.sample[mc])]

# check if all estimators have unique name
estimatorNames = [e.name for eList in estimators.values() for e in eList]
assert len(set(estimatorNames)) == len(estimatorNames), "Names of bkgEstimators are not unique: %s"%",".join(estimatorNames)

# constuct estimator lists
def constructEstimatorList(eList):
    estimatorList = []
    for e in eList:
        estimatorList += estimators[e]
    return estimatorList

allEstimators = constructEstimatorList(estimators.keys())
