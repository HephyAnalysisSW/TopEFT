from TopEFT.analysis.getEstimates import getEstimate
from TopEFT.samples.cmgTuples_signals_Summer16_mAODv2_postProcessed import *
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *


from TopEFT.analysis.regions import regionsA

for signal in allSignals:
    for r in regionsA:
        getEstimate(signal, r, "all", overwrite=False)

mc = [TTZtoLLNuNu, WZ, TTX, TTW, TZQ, rare, nonprompt, pseudoData, pseudoDataPriv]

for sample in mc:
    for r in regionsA:
        getEstimate(sample, r, "all", overwrite=False)
