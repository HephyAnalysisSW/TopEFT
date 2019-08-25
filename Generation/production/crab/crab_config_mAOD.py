#run in CMSSW_8_0_21
from WMCore.Configuration import Configuration
config = Configuration()


tag = '15Jan17'

config.section_("General")
config.General.requestName = "tmp"
config.General.workArea = 'crab_mAOD_%s' % tag
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../cfg/RECOmAOD.py'
config.JobType.disableAutomaticOutputCollection = False

config.section_("Data")
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'Automatic'

config.Data.unitsPerJob = 5
#config.Data.totalUnits  = 50000 
config.Data.publication = True
config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'

config.Data.outputDatasetTag = '%s_mAOD' % tag
config.Data.ignoreLocality = True
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
#config.Site.whitelist = ['T2_AT_Vienna']
config.Site.whitelist = ['T2_IT_Legnaro', 'T2_AT_Vienna', 'T2_US_Florida', 'T2_PL_Swierk', 'T2_US_UCSD', 'T2_US_Caltech', 'T2_US_Wisconsin', 'T2_US_Nebraska', 'T2_RU_IHEP', 'T3_US_Baylor', 'T2_UK_SGrid_RALPP', 'T3_US_Colorado', 'T2_DE_RWTH', 'T2_US_MIT', 'T2_US_Vanderbilt', 'T2_UK_London_Brunel', 'T3_IT_Trieste', 'T3_UK_SGrid_Oxford', 'T3_US_UMD', 'T2_HU_Budapest', 'T2_UA_KIPT']

config.section_("User")


if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for input_dataset in [

        #'/ewkDM_ttZ_ll/schoef-09Nov17-GS-3-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000/schoef-09Nov17-GS-3-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000/schoef-09Nov17-GS-4-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700/schoef-09Nov17-GS-3-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000/schoef-09Nov17-GS-3-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700/schoef-09Nov17-GS-3-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700/schoef-09Nov17-GS-4-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000/schoef-09Nov17-GS-4-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700/schoef-09Nov17-GS-3-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000/schoef-09Nov17-GS-3-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000/schoef-09Nov17-GS-3-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDM_ttZ_ll_DC1A_1p000000/schoef-09Nov17-GS-3-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000/schoef-09Nov17-GS-3-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/HEL_UFO_ttZ_ll_cuW_0p100000/schoef-09Nov17-GS-3-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/HEL_UFO_ttZ_ll_cuW_m0p100000/schoef-09Nov17-GS-4-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/HEL_UFO_ttZ_ll_cuW_m0p200000/schoef-09Nov17-GS-4-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/HEL_UFO_ttZ_ll_cuW_0p200000/schoef-09Nov17-GS-3-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/HEL_UFO_ttZ_ll_cuW_0p300000/schoef-09Nov17-GS-4-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/HEL_UFO_ttZ_ll_cuW_m0p300000/schoef-09Nov17-GS-4-19898e58c9c00509372f15bcc801ecbe/USER',
        '/ewkDMGZ_ttgamma_ll/schoef-15Jan17-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDMGZ_ttgamma_ll_DAG_0p176700_DVG_m0p176700/schoef-15Jan17-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDMGZ_ttgamma_ll_DAG_0p176700_DVG_0p176700/schoef-15Jan17-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDMGZ_ttgamma_ll_DAG_0p500000/schoef-15Jan17-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDMGZ_ttgamma_ll_DAG_0p250000/schoef-15Jan17-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDMGZ_ttgamma_ll_DAG_m0p176700_DVG_m0p176700/schoef-15Jan17-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDMGZ_ttgamma_ll_DAG_m0p176700_DVG_0p176700/schoef-15Jan17-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDMGZ_ttgamma_ll_DAG_m0p500000/schoef-15Jan17-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDMGZ_ttgamma_ll_DAG_m0p250000/schoef-15Jan17-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDMGZ_ttgamma_ll_DVG_0p500000/schoef-15Jan17-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDMGZ_ttgamma_ll_DVG_0p250000/schoef-15Jan17-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDMGZ_ttgamma_ll_DVG_m0p500000/schoef-15Jan17-19898e58c9c00509372f15bcc801ecbe/USER',
        #'/ewkDMGZ_ttgamma_ll_DVG_m0p250000/schoef-15Jan17-19898e58c9c00509372f15bcc801ecbe/USER',

    #'/ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2_slc6_amd64_gcc481_CMSSW_7_1_30_tarball/dspitzba-ewkDM_GENSIMRAW-19898e58c9c00509372f15bcc801ecbe/USER',
    #'/ewkDM_TTZToLL_LO_slc6_amd64_gcc481_CMSSW_7_1_30_tarball/dspitzba-ewkDM_GENSIMRAW-19898e58c9c00509372f15bcc801ecbe/USER',
    ]:
        config.Data.inputDataset = input_dataset
        config.General.requestName = input_dataset.split('/')[1] 
        
        #crabCommand('submit', '--dryrun', config = config)
        crabCommand('submit', config = config)
