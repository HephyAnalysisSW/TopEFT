import ROOT

from TopEFT.samples.helpers import singleton as singleton

@singleton
class color():
  pass

color.data           = ROOT.kBlack
color.DY             = ROOT.kBlue-9
color.TTJets         = 7
color.nonprompt      = ROOT.kBlue-9
color.nonPromptDD    = ROOT.kBlue-9
color.singleTop      = 40
color.TTX            = ROOT.kRed-10
color.TTXNoZ         = ROOT.kRed-10
color.TTH            = ROOT.kRed-10
color.TTW            = ROOT.kRed
color.TTZ            = 91
color.TTZtoLLNuNu    = 91
color.signal         = ROOT.kOrange
color.TTZtoQQ        = 91
color.TTG            = ROOT.kRed
color.TTG_signal     = 91
color.TZQ            = 9
color.TWZ            = ROOT.kBlue-4
color.WJetsToLNu     = ROOT.kRed-10
color.diBoson        = ROOT.kOrange
color.multiBoson     = ROOT.kOrange
color.ZZ             = ROOT.kGreen+3
color.WZ             = 51
color.WZ_amc         = 51
color.WW             = ROOT.kOrange-7
color.VV             = 30
color.WG             = ROOT.kOrange-5
color.ZG             = ROOT.kGreen
color.triBoson       = ROOT.kYellow
color.rare           = 8
color.rare_noZZ      = 8
color.WZZ            = ROOT.kYellow
color.WWG            = ROOT.kYellow-5
color.QCD            = 46
color.QCD_HT         = 46
color.QCD_Mu5        = 46
color.QCD_EMbcToE    = 46
color.QCD_Mu5EMbcToE = 46

color.other          = 46

color.T2tt_450_0                       = ROOT.kBlack
color.TTbarDMJets_scalar_Mchi1_Mphi200 = ROOT.kBlack
color.TTbarDMJets_scalar_Mchi1_Mphi10  = ROOT.kBlack
color.TTbarDMJets_scalar_Mchi1_Mphi20  = ROOT.kBlack
color.TTbarDMJets_scalar_Mchi1_Mphi100 = ROOT.kBlack
color.TTbarDMJets_pseudoscalar_Mchi1_Mphi100 = ROOT.kRed
color.TTbarDMJets_scalar_Mchi10_Mphi100 = ROOT.kPink
