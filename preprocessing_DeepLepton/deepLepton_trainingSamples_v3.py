#dpm v3 samples (Robert)

DY = [
'DY1JetsToLL_M-50',
'DY2JetsToLL_M-50',
'DY3JetsToLL_M-50',
'DY4JetsToLL_M-50',
'DYJetsToLL_M-10to50',
]

TTJETS = [
'TTJets_DiLept',
'TTTo2L2Nu',
]

TTtoSEMILEP = [
'TTToSemilepton',
]

QCD = [
'QCD_Pt-1000toInf_MuEnrichedPt5',
'QCD_Pt-120to170_MuEnrichedPt5',
'QCD_Pt-15to20_MuEnrichedPt5',
'QCD_Pt-170to300_MuEnrichedPt5',
'QCD_Pt-20to30_MuEnrichedPt5',
'QCD_Pt-300to470_MuEnrichedPt5',
'QCD_Pt-30to50_MuEnrichedPt5',
'QCD_Pt-470to600_MuEnrichedPt5',
'QCD_Pt-50to80_MuEnrichedPt5',
'QCD_Pt-600to800_MuEnrichedPt5',
'QCD_Pt-800to1000_MuEnrichedPt5',
'QCD_Pt-80to120_MuEnrichedPt5',
]

NOTUSED = [
'TTJets_HT-1200to2500',
'TTJets_HT-1200to2500',
'TTJets_HT-1200to2500',
'TTJets_HT-2500toInf',
'TTJets_HT-600to800',
'TTJets_HT-800to1200',
'TTJets_SingleLeptFromT',
'TTJets_SingleLeptFromTbar',
'TTJets',
'TTJets',
'TT',
'DYJetsToLL_M-10to50',
'DYJetsToLL_M-50_HT-100to200',
'DYJetsToLL_M-50_HT-1200to2500',
'DYJetsToLL_M-50_HT-200to400',
'DYJetsToLL_M-50_HT-2500toInf',
'DYJetsToLL_M-50_HT-400to600',
'DYJetsToLL_M-50_HT-600to800',
'DYJetsToLL_M-50_HT-600toInf',
'DYJetsToLL_M-50_HT-70to100',
'DYJetsToLL_M-50_HT-800to1200',
'DYJetsToLL_M-50',
'DYJetsToLL_M-50',
'DYJetsToLL_M-5to50_HT-100to200',
'DYJetsToLL_M-5to50_HT-200to400',
'DYJetsToLL_M-5to50_HT-400to600',
'DYJetsToLL_M-5to50_HT-600toInf',
'DYJetsToLL_M-5to50_HT-70to100',
]

DYvsQCDvsQCD = { 'Prompt': DY, 'NonPrompt': QCD, 'Fake': QCD }
TTJETSvsTTtoSEMILEPvsQCD = { 'Prompt': TTJETS, 'NonPrompt': TTtoSEMILEP, 'Fake': QCD }
