from TopEFT.analysis.getEstimates import getEstimate
#from TopEFT.samples.cmgTuples_signals_Summer16_mAODv2_postProcessed import *

data_directory = '/afs/hephy.at/data/rschoefbeck02/cmgTuples/'
postProcessing_directory = "TopEFT_PP_v12/trilep/"
from TopEFT.samples.cmgTuples_ttZ0j_Summer16_mAODv2_postProcessed import *

data_directory = '/afs/hephy.at/data/dspitzbart02/cmgTuples/'
postProcessing_directory = "TopEFT_PP_v12/dilep/"
from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import *


from TopEFT.analysis.regions import *

myRegions = regionsH

for signal in allSignals:
    for r in myRegions:
        getEstimate(signal, r, "all", overwrite=True)

mc = [TTZtoLLNuNu, WZ, TTX, TTW, TZQ, rare, nonprompt, pseudoData ]#, pseudoDataPriv]

for sample in mc:
    for r in myRegions:
        getEstimate(sample, r, "all", overwrite=False)
