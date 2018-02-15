import ROOT, pickle, os
from TopEFT.Tools.btagEfficiency import *
from TopEFT.Tools.user import *

import time, hashlib

from TopEFT.samples.heppy_dpm_samples import mc_heppy_mapper, Fall17_heppy_mapper

tt = mc_heppy_mapper.from_heppy_samplename("TTLep_pow")
WWW = mc_heppy_mapper.from_heppy_samplename("WWW")

tt_17 = Fall17_heppy_mapper.from_heppy_samplename("TTLep_pow")
WW_17 = Fall17_heppy_mapper.from_heppy_samplename("WW")

etaBorders = sorted(list(set(sum(etaBins,[]))))

def getBTagMCTruthEfficiencies(c, cut="(1)", overwrite=False, btagVar='Jet_btagCSV', btagWP='0.8484'):
  print c, cut
  mceff = {}
  commoncf=cut+"&&"
  for ptBin in ptBins:
    mceff[tuple(ptBin)] = {}
    for etaBin in etaBins:
      mceff[tuple(ptBin)][tuple(etaBin)] = {}
      etaCut = "abs(Jet_eta)>"+str(etaBin[0])+"&&abs(Jet_eta)<"+str(etaBin[1])
      ptCut = "Jet_pt>"+str(ptBin[0])
      if ptBin[1]>0:
        ptCut += "&&Jet_pt<"+str(ptBin[1])
      c.Draw(commoncf+"("+btagVar+">"+str(btagWP)+")>>hbQuark(100,-1,2)",commoncf+"abs(Jet_hadronFlavour)==5&&                     "+etaCut+"&&"+ptCut)
      c.Draw(commoncf+"("+btagVar+">"+str(btagWP)+")>>hcQuark(100,-1,2)",commoncf+"abs(Jet_hadronFlavour)==4&&                     "+etaCut+"&&"+ptCut)
      c.Draw(commoncf+"("+btagVar+">"+str(btagWP)+")>>hOther(100,-1,2)" ,commoncf+"(abs(Jet_hadronFlavour) < 4  || abs(Jet_hadronFlavour) > 5)&&  "+etaCut+"&&"+ptCut)
      hbQuark = ROOT.gDirectory.Get("hbQuark")
      hcQuark = ROOT.gDirectory.Get("hcQuark")
      hOther = ROOT.gDirectory.Get("hOther")
      mceff[tuple(ptBin)][tuple(etaBin)]["b"]     = hbQuark.GetMean()
      mceff[tuple(ptBin)][tuple(etaBin)]["c"]     = hcQuark.GetMean()
      mceff[tuple(ptBin)][tuple(etaBin)]["other"] = hOther.GetMean()
      print "Eta",etaBin,etaCut,"Pt",ptBin,ptCut,"Found b/c/other", mceff[tuple(ptBin)][tuple(etaBin)]["b"], mceff[tuple(ptBin)][tuple(etaBin)]["c"], mceff[tuple(ptBin)][tuple(etaBin)]["other"]
      del hbQuark, hcQuark, hOther
  if overwrite: pickle.dump(mceff, file(bTagEffFile, 'w'))
  return mceff

def getBTagMCTruthEfficiencies2D(c, cut="(1)", overwrite=False, btagVar='Jet_btagCSV', btagWP='0.8484'):
    from array import array
    mceff = {}
    c.SetEventList(0)
    if cut and cut.replace(" ","")!= "(1)":
        print "Setting Event List with cut: %s"%cut
        eListName = "eList_%s"%hashlib.md5("%s"%time.time()).hexdigest()
        print eListName
        print cut
        c.Draw(">>%s"%eListName,cut)
        c.SetEventList( getattr(ROOT,eListName))

    passed_hists = {}
    total_hists = {}
    ratios = {}

    btag_var = btagVar
    btag_wp  = btagWP

    jet_quality_cut = "Jet_id>0"
    
    flavor_cuts = {
                        'b':'abs(Jet_hadronFlavour)==5', 
                        'c':'abs(Jet_hadronFlavour)==4',      
                        'other':'(abs(Jet_hadronFlavour) < 4  || abs(Jet_hadronFlavour) > 5)', 
                   }
   
    flavors = flavor_cuts.keys()
 
    for flavor in flavors:
        passed_name = 'passed_%s'%flavor
        passed_hists[flavor] = ROOT.TH2D( passed_name, passed_name , len(ptBorders)-1, array('d',ptBorders), len(etaBorders)-1, array('d', etaBorders) )
        total_name = 'total_%s'%flavor
        total_hists[flavor] = ROOT.TH2D( total_name, total_name , len(ptBorders)-1, array('d',ptBorders), len(etaBorders)-1, array('d', etaBorders) )
        c.Draw("abs(Jet_eta):Jet_pt>>%s"%passed_name, ' && '.join("(%s)"%x for x in [cut,jet_quality_cut, flavor_cuts[flavor], '%s>%s'%(btag_var, btag_wp)]))
        c.Draw("abs(Jet_eta):Jet_pt>>%s"%total_name, ' && '.join("(%s)"%x for x in [cut,jet_quality_cut, flavor_cuts[flavor] ]))
        ratios[flavor] = passed_hists[flavor].Clone("ratio_%s"%flavor)
        ratios[flavor].Divide( total_hists[flavor]) 

    for ipt, ptBin in enumerate( ptBins ,1):
        mceff[tuple(ptBin)]={}
        for jeta, etaBin in enumerate( etaBins ,1):
            mceff[tuple(ptBin)][tuple(etaBin)] = {}
            for flavor in flavors:
                mceff[tuple(ptBin)][tuple(etaBin)][flavor] = ratios[flavor].GetBinContent(ipt, jeta)

            print "Eta",etaBin,"Pt",ptBin,"Found b/c/other", mceff[tuple(ptBin)][tuple(etaBin)]["b"], mceff[tuple(ptBin)][tuple(etaBin)]["c"], mceff[tuple(ptBin)][tuple(etaBin)]["other"]

    return mceff

presel = "(Sum$(Jet_pt>30&&abs(Jet_eta)<2.4&&Jet_id))>=2&&Sum$(LepGood_pt>20&&abs(LepGood_eta)<2.4)>=2"

# old method
#res = getBTagMCTruthEfficiencies(tt.chain, cut=presel, overwrite=False, btagVar='Jet_btagCSV', btagWP='0.8484')
#res = getBTagMCTruthEfficiencies(WWW.chain, cut=presel, overwrite=False, btagVar='Jet_btagCSV', btagWP='0.8484') #to test

# new method
#res = getBTagMCTruthEfficiencies2D(tt.chain, cut=presel, overwrite=False, btagVar='Jet_btagCSV', btagWP='0.8484') #to test
# btag WP for deepCSV 0.6324 in 80X, 0.4941 in 94X

## Fall17
#res = getBTagMCTruthEfficiencies2D(tt_17.chain, cut=presel, overwrite=False, btagVar='(Jet_DFbb+Jet_DFb)', btagWP='0.4941') #to test
#print "Efficiencies:"
#print res
#pickle.dump(res, \
#    file(os.path.expandvars('$CMSSW_BASE/src/TopEFT/Tools/data/btagEfficiencyData/TTLep_pow_Fall17_2j_2l_deepCSV_eta.pkl'), 'w')
#)

res = getBTagMCTruthEfficiencies2D(tt_17.chain, cut=presel, overwrite=False, btagVar='Jet_btagCSV', btagWP='0.8838')
print "Efficiencies:"
print res
pickle.dump(res, \
    file(os.path.expandvars('$CMSSW_BASE/src/TopEFT/Tools/data/btagEfficiencyData/TTLep_pow_Fall17_2j_2l_CSVv2_eta.pkl'), 'w')
)


## Moriond17
#res = getBTagMCTruthEfficiencies2D(tt.chain, cut=presel, overwrite=False, btagVar='(Jet_DFbb+Jet_DFb)', btagWP='0.6324') #to test
#print "Efficiencies:"
#print res
#pickle.dump(res, \
#    file(os.path.expandvars('$CMSSW_BASE/src/TopEFT/Tools/data/btagEfficiencyData/TTLep_pow_Moriond17_2j_2l_deepCSV_eta.pkl'), 'w')
#)
#
#res = getBTagMCTruthEfficiencies2D(tt.chain, cut=presel, overwrite=False, btagVar='Jet_btagCSV', btagWP='0.8484') #to test
#print "Efficiencies:"
#print res
#pickle.dump(res, \
#    file(os.path.expandvars('$CMSSW_BASE/src/TopEFT/Tools/data/btagEfficiencyData/TTLep_pow_Moriond17_2j_2l_CSVv2_eta.pkl'), 'w')
#)


