# Standard imports
import ROOT
import pickle
import array

# TopEFT
from TopEFT.Tools.WeightInfo import WeightInfo
# RootTools
from RootTools.core.standard import *
# rw_cpQM -10 ... 30
# rw_cpt -20 ... 20

sample = Sample.fromFiles("ttZ_current_scan", ["/afs/hephy.at/data/rschoefbeck02/TopEFT/skims/gen/v2/fwlite_ttZ_ll_LO_currentplane_highStat_scan/fwlite_ttZ_ll_LO_currentplane_highStat_scan_0.root"])

# Load weight info
weight_info = pickle.load(file('/afs/hephy.at/data/rschoefbeck02/TopEFT/results/gridpacks/ttZ0j_rwgt_patch_currentplane_highStat_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl'))
w = WeightInfo("/afs/hephy.at/data/rschoefbeck02/TopEFT/results/gridpacks/ttZ0j_rwgt_patch_currentplane_highStat_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.pkl")

weight_dict = { tuple( map(float, k.replace('p','.').replace('m','-').split('_')[1::2])): v for k,v in weight_info.iteritems()}
values = {}
for k in weight_info.keys():
    vars = k.split('_')[::2] 
    vals = map(float, k.replace('p','.').replace('m','-').split('_')[1::2] )
    assert len(vars)==len(vals)
    for i in range(len(vars)):
        if vars[i] not in values.keys(): values[vars[i]] = []
        if vals[i] not in values[vars[i]]: values[vars[i]].append(vals[i])

for var in vars: 
    values[var].sort()
        

variables = [ 
    "nrw/I", "p[C/F]", "np/I",
    "Z_pt/F", "Z_eta/F", "Z_phi/F", "Z_mass/F", "Z_cosThetaStar/F", "Z_daughterPdg/I"
]
weight_vector = VectorTreeVariable.fromString("rw[w/F,cpQM/F,cpt/F]", nMax = len(weight_info.keys()) )
r = sample.treeReader( variables = map( TreeVariable.fromString, variables ) + [weight_vector] )

maxEvents = 30
counter = 0
first = True

c1 = ROOT.TCanvas()

r.start()
tg = {}
while r.run():

    counter += 1
    tg[counter] = ROOT.TGraph(len(values['cpt']), array.array('d', values['cpt'] ), array.array('d', [ r.event.rw_w[weight_dict[(0, v)]] for v in values['cpt'] ] ) )
    tg[counter].Fit("pol2","","", min(values['cpt']), max(values['cpt']))
    tg[counter].Draw('AP*' if first else 'P*')
    tg[counter].GetYaxis().SetRangeUser(0,50*10**-6)
    tg[counter].SetLineWidth(1)
    first = False
    if counter == maxEvents: break

    f = ROOT.TTreeFormula( "f%i"%counter, w.weight_string(2), sample.chain)

c1.Print("/afs/hephy.at/user/r/rschoefbeck/www/etc/ew.png")
 
#[ weight_dict[(0, v)] for v in values['cpt'] ]
