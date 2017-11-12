#run in CMSSW_8_0_21

tag = '09Nov17-GS-3'

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "tmp"
config.General.workArea = 'crab_step1_%s' % tag
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../cfg/step1_DIGI_L1_DIGI2RAW_HLT_PU.py'
config.JobType.disableAutomaticOutputCollection = False

config.section_("Data")
#config.Data.splitting = 'FileBased'
#config.Data.splitting = 'EventBased'
config.Data.splitting = 'EventAwareLumiBased'
#config.Data.totalUnits  = 500000 
config.Data.unitsPerJob = 200
#config.Data.totalUnits  = 50000 
config.Data.publication = True
config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'

#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
#config.Site.whitelist = ['T2_*']

config.section_("User")


if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand

    for input_dataset in [
        #'/ewkDM_ttZ_ll/schoef-ewkDM_09Nov17-e77c441d012ee598545c0020859d9ab0/USER',
        '/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000/schoef-ewkDM_09Nov17-f07f90363df434a06f0f034162e7cc3c/USER',
        '/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000/schoef-ewkDM_09Nov17-382ba64850d333b8758cfbda64e154ee/USER',
        '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000/schoef-ewkDM_09Nov17-bf639f7c0cf3b58622309ab38644e6ef/USER',
        '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000/schoef-ewkDM_09Nov17-854a538c08c9889843c402e7c057267b/USER',
        '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000/schoef-ewkDM_09Nov17-93af3031bce01ac1431c3dea90315387/USER',
        '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000/schoef-ewkDM_09Nov17-36a7133612c20cebff4a51e59aaf8364/USER',
        #'/ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000/schoef-ewkDM_09Nov17-c0cc438e2ba1a4b23d2945ab2f261d2c/USER',
        '/ewkDM_ttZ_ll_DC1A_1p000000/schoef-ewkDM_09Nov17-7f9958cc97b83149cf0fe0553bdfcaf2/USER',
        '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700/schoef-ewkDM_09Nov17-ba4fabcbf8a5908d45414efd57aa8119/USER',
        '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700/schoef-ewkDM_09Nov17-44a0b965bee64391722ee1ac626cec71/USER',
        '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700/schoef-ewkDM_09Nov17-9cfb58347b5f3ab2740df554d66647b8/USER',
        '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700/schoef-ewkDM_09Nov17-9e4d723e7412ffedf3b8c0606b6c5e6d/USER',
        '/HEL_UFO_ttZ_ll_cuW_0p100000/schoef-HEL_09Nov17-df62a4db47c06ad19258ed4ccbb31f31/USER',
        '/HEL_UFO_ttZ_ll_cuW_0p200000/schoef-HEL_09Nov17-6a3c68b4249a638b0436b57c064ddea6/USER',
        '/HEL_UFO_ttZ_ll_cuW_0p300000/schoef-HEL_09Nov17-a046fa0828dd90306ca134e402fb046d/USER',
        '/HEL_UFO_ttZ_ll_cuW_m0p100000/schoef-HEL_09Nov17-0fc0045464dd563d2392bedcaa76f810/USER',
        '/HEL_UFO_ttZ_ll_cuW_m0p200000/schoef-HEL_09Nov17-6333492b80f6cd9d334ac349cec18447/USER',
        '/HEL_UFO_ttZ_ll_cuW_m0p300000/schoef-HEL_09Nov17-10730607a8d7ab9f15cbeb533e6f3d6f/USER',
    ]:
        config.Data.inputDataset = input_dataset
        config.General.requestName = input_dataset.split('/')[1] 
        config.Data.outputDatasetTag = tag 
        
        #crabCommand('submit', '--dryrun', config = config)
        crabCommand('submit', config = config)
