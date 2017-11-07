# run in CMSSW_7_1_25_patch2
from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "tmp"
config.General.workArea = 'crab_ewkDM_2'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../cfg/GEN-SIM-LHE_LO.py'
config.JobType.disableAutomaticOutputCollection = False

config.section_("Data")
config.Data.splitting = 'EventBased'

config.Data.unitsPerJob = 200
config.Data.totalUnits  = 500000 
config.Data.publication = True
config.Data.publishDBS = 'phys03'

config.Data.outputDatasetTag = 'ewkDM'
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
#config.Site.whitelist = ['T2_*']

config.section_("User")


if __name__ == '__main__':
    #gridpack_dir = "/afs/hephy.at/data/rschoefbeck02/TopEFT/results/gridpacks/"
    gridpack_dir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/gridpacks/"

    import os

    from CRABAPI.RawCommand import crabCommand

    for gridpack in [
        #'ewkDM_ttZ_ll_noH.tar.xz',
        #'ewkDM_ttZ_ll_noH_DC2V_-0.150000.tar.xz',
        #'ewkDM_ttZ_ll_noH_DC2V_-0.250000.tar.xz',
        #'ewkDM_ttZ_ll_noH_DC2V_0.050000.tar.xz',
        #'ewkDM_ttZ_ll_noH_DC2V_0.100000.tar.xz',
        #'ewkDM_ttZ_ll_noH_DC2V_0.200000.tar.xz',
        #'ewkDM_ttZ_ll_noH_DC2V_0.300000.tar.xz',
        'ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
        'ewkDM_TTZToLL_LO_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'
    ]:
        config.JobType.inputFiles = [os.path.join(gridpack_dir, gridpack)]
        config.General.requestName = gridpack.rstrip('.tar.xz').replace('-','m').replace('.','p')
        config.Data.outputPrimaryDataset = config.General.requestName # dataset name
        
        config.JobType.pyCfgParams = ['gridpack=../'+gridpack]

        #crabCommand('submit', '--dryrun', config = config)
        crabCommand('submit', config = config)
