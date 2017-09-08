#run in CMSSW_8_0_21
from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "tmp"
config.General.workArea = 'crab_ewkDM'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../cfg/step1_DIGI_L1_DIGI2RAW_HLT_PU.py'
config.JobType.disableAutomaticOutputCollection = False

config.section_("Data")
config.Data.splitting = 'EventAwareLumiBased'
#config.Data.splitting = 'Automatic'

config.Data.unitsPerJob = 1
#config.Data.totalUnits  = 50000 
config.Data.publication = True
config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'

config.Data.outputDatasetTag = 'ewkDM'
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
#config.Site.whitelist = ['T2_*']

config.section_("User")


if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand

    for input_dataset in [
'/ewkDM_ttZ_ll/schoef-ewkDM-e1a069162e896efecc10f859afdda0d0/USER',
'/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000/schoef-ewkDM-863d441c1e97429a518397b2b60fd1be/USER',
'/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000/schoef-ewkDM-ff3cbbd709193316b9c63feda6313fd2/USER',
'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700/schoef-ewkDM-bedd681b46b413b9e38bf1a1ea2e75b5/USER',
'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700/schoef-ewkDM-d670ddb18e88e55b6a43b4acd2505de3/USER',
'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000/schoef-ewkDM-fc88fc2758a774e57c48fe86b5da4bcc/USER',
'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700/schoef-ewkDM-28215b5f801d5ea3987bbdce381a4244/USER',
'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000/schoef-ewkDM-3a75ae4139536634dab39690896bcd56/USER',
'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000/schoef-ewkDM-83046cbf09b262686da67ff44f4901ef/USER',
'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000/schoef-ewkDM-f750c11322cf3df8d05711a6083e929b/USER',
'/ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000/schoef-ewkDM-d5ca1cdb139c8f92e34abf823fbeb652/USER',
'/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700/schoef-ewkDM-10e11608d2c97bb8d3584319b95ebd12/USER',
    ]:
        config.Data.inputDataset = input_dataset
        config.General.requestName = input_dataset.split('/')[1] 
        
        #crabCommand('submit', '--dryrun', config = config)
        crabCommand('submit', config = config)
