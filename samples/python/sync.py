from RootTools.core.standard import *
base_dir = '/afs/hephy.at/data/rschoefbeck01/cmgTuples/sync/'
mc_2016  = Sample.fromCMGOutput('mc_2016',  base_dir, chunkString='TTJets_SingleLeptonFromTbar', isData = True)
mc_2017  = Sample.fromCMGOutput('mc_2017',  base_dir, chunkString='TTSemi_pow', isData = True)
data_2016= Sample.fromCMGOutput('data_2016',base_dir, chunkString='MuonEG_Run2016F_03Feb2017', isData = True)
data_2017= Sample.fromCMGOutput('data_2017',base_dir, chunkString='MuonEG_Run2017F_17Nov2017', isData = True)

#base_dir = '/afs/hephy.at/data/dspitzbart02/cmgTuples/sync/'
#ttz_2017 = Sample.fromCMGOutput('ttz_2017',base_dir, chunkString='TTZToLLNuNu_amc', isData = True) # fake data
#ttbar_2017 = Sample.fromCMGOutput('ttbar_2017',base_dir, chunkString='TTLep_pow', isData = True) # fake data
#DoubleMuon_Run2016G_07Aug17 = Sample.fromFiles('DoubleMuon_Run2016G', [base_dir+'DoubleMuon_Run2016G/tree_108.root'], treeName='tree', isData = True)

moertel_sync = Sample.fromFiles('moertel_sync', ['/afs/hephy.at/data/rschoefbeck01/DeepLepton/data/full_events/WZTo3LNu_amcatnlo_2/treeProducerSusySingleLepton/tree.root'], treeName='tree', isData = True)
