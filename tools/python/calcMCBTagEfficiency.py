import ROOT, pickle, os
from StopsDilepton.tools.btagEfficiency import *
from StopsDilepton.tools.user import *

from StopsDilepton.samples.heppy_dpm_samples import mc_heppy_mapper
from StopsDilepton.samples.heppy_dpm_samples import T2tt_heppy_mapper


tt = mc_heppy_mapper.from_heppy_samplename("TTLep_pow")
tWnunu = mc_heppy_mapper.from_heppy_samplename("tWnunu")

T2tt_all = ROOT.TChain("tree")
for s in T2tt_heppy_mapper.heppy_sample_names[:1]:
    t2tt = T2tt_heppy_mapper.from_heppy_samplename(s)
    T2tt_all.Add(t2tt.chain)

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


presel = "(Sum$(Jet_pt>30&&abs(Jet_eta)<2.4&&Jet_id))>=2&&Sum$(LepGood_pt>20&&abs(LepGood_eta)<2.4)>=2"

#res = getBTagMCTruthEfficiencies(tt.chain, cut=presel, overwrite=False, btagVar='Jet_btagCSV', btagWP='0.8484')
res = getBTagMCTruthEfficiencies(T2tt_all, cut=presel, overwrite=False, btagVar='Jet_btagCSV', btagWP='0.8484')
#res = getBTagMCTruthEfficiencies(tWnunu.chain, cut=presel, overwrite=False, btagVar='Jet_btagCSV', btagWP='0.8484') #to test

print "Efficiencies:"
print res
pickle.dump(res, \
    file(os.path.expandvars('$CMSSW_BASE/src/StopsDilepton/tools/data/btagEfficiencyData/T2tt_Moriond17_2j_2l.pkl'), 'w')
)
