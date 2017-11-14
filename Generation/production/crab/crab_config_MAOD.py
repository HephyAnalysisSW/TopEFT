#run in CMSSW_8_0_21
from WMCore.Configuration import Configuration
config = Configuration()


tag = '09Nov17-GS-3-PREPROD'

config.section_("General")
config.General.requestName = "tmp"
config.General.workArea = 'crab_ewkDM_mAOD'
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
#config.Site.whitelist = ['T2_*']

config.section_("User")


if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for input_dataset in [
    '/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000/schoef-09Nov17-GS-3-19898e58c9c00509372f15bcc801ecbe/USER',
    '/ewkDM_ttZ_ll/schoef-09Nov17-GS-3-19898e58c9c00509372f15bcc801ecbe/USER',
    '/ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000/schoef-09Nov17-GS-3-19898e58c9c00509372f15bcc801ecbe/USER',

    #'/ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2_slc6_amd64_gcc481_CMSSW_7_1_30_tarball/dspitzba-ewkDM_GENSIMRAW-19898e58c9c00509372f15bcc801ecbe/USER',
    #'/ewkDM_TTZToLL_LO_slc6_amd64_gcc481_CMSSW_7_1_30_tarball/dspitzba-ewkDM_GENSIMRAW-19898e58c9c00509372f15bcc801ecbe/USER',
    ]:
        config.Data.inputDataset = input_dataset
        config.General.requestName = input_dataset.split('/')[1] 
        
        #crabCommand('submit', '--dryrun', config = config)
        crabCommand('submit', config = config)
