import os
from CRABClient.UserUtilities import getUsernameFromSiteDB
from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "topEFT_signal_ttZ_HEL_UFO_cuw_0p051_DIGI"
config.General.workArea = 'crab_topEFT_signal'
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'SUS-RunIISummer16DR80-00013_1_cfg.py'

config.section_("Data")
config.Data.inputDataset = '/topEFT_signal_LHEGEN/dspitzba-topEFT_signal_LHEGEN-ttZ_HEL_UFO_cuw_0p051-08082017_RAWSIMoutput-dfca6a65821676e7cd825fbf500930f3/USER'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = True
config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'
config.Data.outputDatasetTag = 'topEFT_signal_LHEGEN-ttZ_HEL_UFO_cuw_0p051_DIGI-08082017'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'

