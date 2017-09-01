from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "privateMCProduction#REQUESTDATE##WHOAMI#"
config.General.workArea = 'crab_privateMCProduction'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'GEN-SIM-LHE_LO.py'
#config.JobType.inputFiles = ['GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh', 'gridpack.tgz']
config.JobType.disableAutomaticOutputCollection = False
config.jobType.pyCfgParams = ['gridpack=/afs/hephy.at/data/rschoefbeck01/TopEFT/results/gridpacks/ewkDM_ttZ_ll_DC1A_0.600000_DC1V_-0.240000_DC2A_0.250000.tar.xz']

config.section_("Data")
config.Data.outputPrimaryDataset = 'privateMCProductionLHEGEN'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1200
config.Data.totalUnits = #NUMBEREVENTS#
config.Data.publication = True
config.Data.outputDatasetTag = 'eventLHEGEN-#BASENAME#-#REQUESTDATE#'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
config.Site.whitelist = ['T2_*']

config.section_("User")
