def deepLeptonSignalSamples(year):

    if year==2016:
        SignalSamples = [
    
        'TTJets_SingleLeptonFromTbar',
        'TTJets_SingleLeptonFromTbar_ext',
        'TTJets_SingleLeptonFromT',
        'TTJets_SingleLeptonFromT_ext',
        
        'TTJets_DiLepton',
        'TTJets_DiLepton_ext',
        
        #'TTJets',
        #'TTJets_LO',
        #'TT_pow_ext3',
        #'TT_pow',
        #'TTLep_pow',
        #'TTSemiLep_pow',
        #'TTJets_LO_HT600to800_ext',
        #'TTJets_LO_HT800to1200_ext',
        #'TTJets_LO_HT1200to2500_ext',
        #'TTJets_LO_HT2500toInf_ext',
                    
                        ]
    
    if year==2017:
        SignalSamples = [

        'TTJets',
        'TTLep_pow',
        'TTHad_pow',
        'TTSemi_pow',
        'TTJets_SingleLeptonFromT',
        'TTLep_pow_TuneDown',
        'TTLep_pow_TuneUp',
        'TTLep_pow_hdampDown',
        'TTLep_pow_hdampUp',

                        ]

    return SignalSamples

def deepLeptonBackgroundSamples(year):

    if year==2016:
        BackgroundSamples = [
    
        'QCD_Pt20to30_EMEnriched',
        'QCD_Pt30to50_EMEnriched',
        'QCD_Pt30to50_EMEnriched_ext',
        'QCD_Pt50to80_EMEnriched_ext',
        'QCD_Pt80to120_EMEnriched_ext',
        'QCD_Pt120to170_EMEnriched',
        'QCD_Pt170to300_EMEnriched',
        'QCD_Pt300toInf_EMEnriched',

        'QCD_Pt_20to30_bcToE',
        'QCD_Pt_30to80_bcToE',
        'QCD_Pt_80to170_bcToE',
        'QCD_Pt_170to250_bcToE',
        'QCD_Pt_250toInf_bcToE',

        'QCD_Pt15to20_Mu5',
        'QCD_Pt20to30_Mu5',
        'QCD_Pt30to50_Mu5',
        'QCD_Pt50to80_Mu5',
        'QCD_Pt80to120_Mu5',
        'QCD_Pt80to120_Mu5_ext',
        'QCD_Pt120to170_Mu5',
        'QCD_Pt170to300_Mu5',
        'QCD_Pt170to300_Mu5_ext',
        'QCD_Pt300to470_Mu5',
        'QCD_Pt300to470_Mu5_ext',
        'QCD_Pt300to470_Mu5_ext2',
        'QCD_Pt470to600_Mu5',
        'QCD_Pt470to600_Mu5_ext',
        'QCD_Pt470to600_Mu5_ext2',
        'QCD_Pt600to800_Mu5',
        'QCD_Pt600to800_Mu5_ext',
        'QCD_Pt800to1000_Mu5',
        'QCD_Pt800to1000_Mu5_ext',
        'QCD_Pt800to1000_Mu5_ext2',
        'QCD_Pt1000toInf_Mu5',
        'QCD_Pt1000toInf_Mu5_ext',

                        ]
    
    if year==2017:
        BackgroundSamples = [

        'QCD_Pt15to20_EMEnriched',
        'QCD_Pt20to30_EMEnriched',
        'QCD_Pt30to50_EMEnriched',
        'QCD_Pt50to80_EMEnriched',
        'QCD_Pt80to120_EMEnriched',
        'QCD_Pt120to170_EMEnriched',
        'QCD_Pt170to300_EMEnriched',
        'QCD_Pt300toInf_EMEnriched',

        'QCD_Pt15to20_bcToE',
        'QCD_Pt20to30_bcToE',
        'QCD_Pt30to80_bcToE',
        'QCD_Pt80to170_bcToE',
        'QCD_Pt170to250_bcToE',
        'QCD_Pt250toInf_bcToE',

        'QCD_Pt15to20_Mu5',
        'QCD_Pt20to30_Mu5',
        'QCD_Pt30to50_Mu5',
        'QCD_Pt50to80_Mu5',
        'QCD_Pt80to120_Mu5',
        'QCD_Pt120to170_Mu5',
        'QCD_Pt170to300_Mu5',
        'QCD_Pt300to470_Mu5',
        'QCD_Pt470to600_Mu5',
        'QCD_Pt600to800_Mu5',
        'QCD_Pt800to1000_Mu5',
        'QCD_Pt1000toInf_Mu5',

                        ]

    return BackgroundSamples

################
# Leptons 2016 #
################

#ele Prompt    181435654
#ele NonPrompt  16010337
#ele Fake       19637052

#muo Prompt    191035981
#muo NonPrompt   6673285
#muo Fake         771745

################
# Leptons 2017 #
################

#ele Prompt    123763579
#ele NonPrompt  20983142
#ele Fake       23624542

#muo Prompt    125785124
#muo NonPrompt   6495135
#muo Fake         702582
