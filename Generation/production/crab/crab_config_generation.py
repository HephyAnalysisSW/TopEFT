# run in CMSSW_7_1_25_patch2
from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "tmp"
config.General.workArea = 'crab_ewkDM_v2'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../cfg/GEN-SIM-LHE_LO.py'
config.JobType.disableAutomaticOutputCollection = False

config.section_("Data")
config.Data.splitting = 'EventBased'

config.Data.unitsPerJob = 800
config.Data.totalUnits  = 500000 
config.Data.publication = True
config.Data.publishDBS = 'phys03'

#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
#config.Site.whitelist = ['T2_*']

config.section_("User")


if __name__ == '__main__':
    gridpack_dir = "/afs/hephy.at/data/rschoefbeck01/gridpacks/"

    import os

    from CRABAPI.RawCommand import crabCommand

    for outputDatasetTag, nJetMax, gridpack in [
        ( 'dim6Top_19_08_25', 1, 'ttW01j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz')
        #'ewkDM_ttZ_ll_noH.tar.xz',
        #'ewkDM_ttZ_ll_noH_DC2V_-0.150000.tar.xz',
        #'ewkDM_ttZ_ll_noH_DC2V_-0.250000.tar.xz',
        #'ewkDM_ttZ_ll_noH_DC2V_0.050000.tar.xz',
        #'ewkDM_ttZ_ll_noH_DC2V_0.100000.tar.xz',
        #'ewkDM_ttZ_ll_noH_DC2V_0.200000.tar.xz',
        #'ewkDM_ttZ_ll_noH_DC2V_0.300000.tar.xz',
        #'ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
        #'ewkDM_TTZToLL_LO_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
        #'ewkDM_TTZToLL_LO_DC1A_0p60_DC1V_m0p24_DC2A0p25_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
        #'ewkDM_TTZToLL_LO_DC1A_0p50_DC1V_0p50_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
        #'ewkDM_TTZToLL_LO_DC1A_0p50_DC1V_m1p00_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
        #'ewkDM_TTZToLL_LO_DC1A_1p00_DC1V_0p00_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
        #'ewkDM_TTZToLL_LO_DC1A_0p60_DC1V_m0p24_DC2V0p25_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
        #'ewkDM_TTZToLL_01j_LO_DC2A0p2_DC2V0p2_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
        #'ewkDM_TTZToLL_01j_LO_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'

        #('ewkDM_09Nov17', 0, 'ewkDM_ttZ_ll_DC1A_0.500000_DC1V_0.500000.tar.xz'),
        #('ewkDM_09Nov17', 0, 'ewkDM_ttZ_ll_DC1A_0.500000_DC1V_-1.000000.tar.xz'),
        #('ewkDM_09Nov17', 0, 'ewkDM_ttZ_ll_DC1A_0.600000_DC1V_-0.240000_DC2A_-0.176700_DC2V_-0.176700.tar.xz'),
        #('ewkDM_09Nov17', 0, 'ewkDM_ttZ_ll_DC1A_0.600000_DC1V_-0.240000_DC2A_-0.176700_DC2V_0.176700.tar.xz'),
        #('ewkDM_09Nov17', 0, 'ewkDM_ttZ_ll_DC1A_0.600000_DC1V_-0.240000_DC2A_0.176700_DC2V_-0.176700.tar.xz'),
        #('ewkDM_09Nov17', 0, 'ewkDM_ttZ_ll_DC1A_0.600000_DC1V_-0.240000_DC2A_0.176700_DC2V_0.176700.tar.xz'),
        #('ewkDM_09Nov17', 0, 'ewkDM_ttZ_ll_DC1A_0.600000_DC1V_-0.240000_DC2A_-0.250000.tar.xz'),
        #('ewkDM_09Nov17', 0, 'ewkDM_ttZ_ll_DC1A_0.600000_DC1V_-0.240000_DC2A_0.250000.tar.xz'),
        #('ewkDM_09Nov17', 0, 'ewkDM_ttZ_ll_DC1A_0.600000_DC1V_-0.240000_DC2V_-0.250000.tar.xz'),
        #('ewkDM_09Nov17', 0, 'ewkDM_ttZ_ll_DC1A_0.600000_DC1V_-0.240000_DC2V_0.250000.tar.xz'),
        #('ewkDM_09Nov17', 0, 'ewkDM_ttZ_ll_DC1A_1.000000.tar.xz'),
        #('ewkDM_09Nov17', 0, 'ewkDM_ttZ_ll_DC2A_0.200000_DC2V_0.200000.tar.xz'),
        #('ewkDM_09Nov17', 0, 'ewkDM_ttZ_ll.tar.xz'),
        #('HEL_09Nov17', 0, 'HEL_UFO_ttZ_ll_cuW_-0.100000.tar.xz'),
        #('HEL_09Nov17', 0, 'HEL_UFO_ttZ_ll_cuW_0.100000.tar.xz'),
        #('HEL_09Nov17', 0, 'HEL_UFO_ttZ_ll_cuW_-0.200000.tar.xz'),
        #('HEL_09Nov17', 0, 'HEL_UFO_ttZ_ll_cuW_0.200000.tar.xz'),
        #('HEL_09Nov17', 0, 'HEL_UFO_ttZ_ll_cuW_-0.300000.tar.xz'),
        #('HEL_09Nov17', 0, 'HEL_UFO_ttZ_ll_cuW_0.300000.tar.xz'),

        #('ewkDMGZ_13Jan18',0,'ewkDMGZ_ttgamma_ll.tar.xz'),
        #('ewkDMGZ_13Jan18',0,'ewkDMGZ_ttgamma_ll_DAG_-0.176700_DVG_-0.176700.tar.xz'),
        #('ewkDMGZ_13Jan18',0,'ewkDMGZ_ttgamma_ll_DAG_-0.176700_DVG_0.176700.tar.xz'),
        #('ewkDMGZ_13Jan18',0,'ewkDMGZ_ttgamma_ll_DAG_0.176700_DVG_-0.176700.tar.xz'),
        #('ewkDMGZ_13Jan18',0,'ewkDMGZ_ttgamma_ll_DAG_0.176700_DVG_0.176700.tar.xz'),
        #('ewkDMGZ_13Jan18',0,'ewkDMGZ_ttgamma_ll_DAG_-0.250000.tar.xz'),
        #('ewkDMGZ_13Jan18',0,'ewkDMGZ_ttgamma_ll_DAG_0.250000.tar.xz'),
        #('ewkDMGZ_13Jan18',0,'ewkDMGZ_ttgamma_ll_DAG_-0.500000.tar.xz'),
        #('ewkDMGZ_13Jan18',0,'ewkDMGZ_ttgamma_ll_DAG_0.500000.tar.xz'),
        #('ewkDMGZ_13Jan18',0,'ewkDMGZ_ttgamma_ll_DVG_-0.250000.tar.xz'),
        #('ewkDMGZ_13Jan18',0,'ewkDMGZ_ttgamma_ll_DVG_0.250000.tar.xz'),
        #('ewkDMGZ_13Jan18',0,'ewkDMGZ_ttgamma_ll_DVG_-0.500000.tar.xz'),
        #('ewkDMGZ_13Jan18',0,'ewkDMGZ_ttgamma_ll_DVG_0.500000.tar.xz'),
    ]:
        config.Data.outputDatasetTag = outputDatasetTag
        config.JobType.inputFiles = [os.path.join(gridpack_dir, gridpack)]
        config.General.requestName = gridpack.rstrip('.tar.xz').replace('-','m').replace('.','p')
        config.Data.outputPrimaryDataset = config.General.requestName # dataset name
        
        config.JobType.pyCfgParams = ['gridpack=../'+gridpack, 'nJetMax=%i'%nJetMax]

        #crabCommand('submit', '--dryrun', config = config)
        crabCommand('submit', config = config)
