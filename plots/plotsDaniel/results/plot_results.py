import ROOT
import os
import ctypes
import copy
import shutil
from functools                      import partial
from array                          import array

from RootTools.core.standard        import *

from TopEFT.Tools.user              import combineReleaseLocation, analysis_results, plot_directory


# Plot style
ROOT.gROOT.LoadMacro('$CMSSW_BASE/src/TopEFT/Tools/scripts/tdrstyle.C')
ROOT.setTDRStyle()

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument("--testGrayscale",   action='store_true',            help="Because of  reasons...")
argParser.add_argument("--preliminary",     action='store_true',            help="Because of  reasons...")
argParser.add_argument("--model",           action='store', default='EFT',  help="Use sigma levels?")
args = argParser.parse_args()

## define all the results. EFT
results_EFT = [\
    {   'name': 'ctZ',
        'tex': 'C_{tZ}/#Lambda^{2}',
        'limits': {'new': [(-1.1, 1.1)], 'CMS': [(-2.6,2.6)], 'ATLAS': [(-2.4, 2.4)], 'indirect': [(-4.7, 0.2)], 'direct': [(-2.2, 3.3)], 'maltoni':[(-7.2, 7.7)]}
    },
    {   'name': 'ctZI',
        'tex': 'C_{tZ}^{[I]}/#Lambda^{2}',
        'limits': {'new': [(-1.2, 1.2)], 'CMS': [], 'ATLAS': [], 'indirect': [], 'direct': [], 'maltoni':[]} #nothing else?!
    },
    {   'name': 'cpt',
        'tex': 'C_{#varphit}/#Lambda^{2}',
        'limits': {'new': [(0.3, 5.4)], 'CMS': [(-22.2, -13.0), (-3.2, 6.0)], 'ATLAS': [(-25.0, 5.5)], 'indirect': [(-0.1, 3.7)], 'direct': [(-9.7, 8.3)], 'maltoni':[(-6.4, 7.3)]}
    },
    {   'name': 'cpQM',
        'tex': 'C_{#varphiQ}^{#font[122]{\55}}/#Lambda^{2}',
        'limits': {'new': [(-4.0, 0.05)], 'CMS': [], 'ATLAS': [(-3.3, 4.2)], 'indirect': [(-4.7, 0.7)], 'direct': [(-6.1, 6.2)], 'maltoni':[(-4.2, 3.9)]}
    },
]

ordering_EFT = ['new', 'CMS', 'ATLAS', 'maltoni', 'direct', 'indirect']

## define all the results. BSM
results_BSM = [\
    {   'name': 'DC2A',
        'tex': 'C_{2,A}',
        'limits': {'new': [(-0.128,0.129)], 'CMS': []}
    },
    {   'name': 'DC2V',
        'tex': 'C_{2,V}',
        'limits': {'new': [(-0.122, 0.116)], 'CMS': []}
    },
    {   'name': 'DC1A',
        'tex': '#DeltaC_{1,A}',
        'limits': {'new': [(-0.816+0.601, -0.646+0.601)], 'CMS': [(-0.9+0.601, -0.45+0.601), (0.45+0.601, 0.90+0.601)], 'expected': [(-0.18, 0.14)]}
    },
    {   'name': 'DC1V',
        'tex': '#DeltaC_{1,V}',
        'limits': {'new': [(-0.730-0.245, -0.385-0.245), (0.347-0.245, 0.771-0.245)], 'CMS': [(-0.7-0.245, 0.7-0.245)], 'expected': [(-0.85,0.39)]}
    },
]

ordering_BSM = ['new', 'CMS']

if args.model == 'EFT':
    res = results_EFT
    ordering = ordering_EFT
else:
    res = results_BSM
    ordering = ordering_BSM

styles = {
    'new': {'color':ROOT.kBlack, 'style':1, 'width':4},
    'CMS': {'color': ROOT.kRed+1,   'style':1, 'width':3},
    'ATLAS': {'color': ROOT.kBlue-6, 'style':1, 'width':3},
    'maltoni': {'color': ROOT.kOrange-2, 'style':1, 'width':3},
    'direct': {'color': ROOT.kSpring+1, 'style':1, 'width':3},
    'indirect': {'color': ROOT.kBlack, 'style':2, 'width':2}
    }

cans = ROOT.TCanvas("cans","",10,10,700,700)
cans.Range(-10,-1,10,1)

if args.testGrayscale:
    cans.SetGrayscale()

# draw the axis
if args.model == 'EFT':
    upper = 12
    lower = -26
else:
    upper = 0.8
    lower = -1.2

axis = ROOT.TGaxis(-9.5,-0.85,9.5,-0.85,lower,upper,505,"")
axisUpper = ROOT.TGaxis(-9.5,0.85,9.5,0.85,lower,upper,505,"-")
axisUpper.SetLabelOffset(10)
axis.SetName("axis")
axis.Draw()
axisUpper.Draw()

zero_point = 3.5 if args.model == 'EFT' else 1.9
zero = ROOT.TLine(zero_point,-0.85,zero_point,0.85)
zero.SetLineStyle(2)

box1 = ROOT.TLine(-9.5, -0.85, -9.5, 0.85)
box2 = ROOT.TLine(9.5, -0.85, 9.5, 0.85)
box3 = ROOT.TLine(-9.5, 0.85, 9.5, 0.85)

pads = []

### Get all the pads ###
for p in range(len(res)):
    y_lo = 0.9-0.8*((p+1.)/len(res))
    y_hi = 0.9-0.8*(float(p)/len(res))

    pads.append(ROOT.TPad("pad_%s"%p,"pad_%s"%p, 0.5/20, y_lo, 19.5/20, y_hi ))
    pads[-1].Range(lower,0,upper,5)
    pads[-1].SetFillColor(0)
    pads[-1].Draw()
    pads[-1].cd()
    
    # put the stuff
    graphs  = []
    res[p]['lines'] = []
    for i, o in enumerate(ordering):
        limits = res[p]['limits'][o]
        x = []
        y = []
        y_err = []
        x_plus = []
        x_minus = []
        for j,l in enumerate(limits):
            start = 4.4 if args.model == 'EFT' else 3.4
            newLines = []
            newLines += [   ROOT.TLine(l[0], start-0.5*i,       l[1], start-0.5*i),
                            ROOT.TLine(l[0], start-0.5*i+0.15,  l[0], start-0.5*i-0.15),
                            ROOT.TLine(l[1], start-0.5*i+0.15,  l[1], start-0.5*i-0.15)]
            for k,line in enumerate(newLines):
                line.SetLineColor(styles[o]['color'])
                line.SetLineWidth(styles[o]['width'])
                if k == 0:
                    line.SetLineStyle(styles[o]['style'])
            
            res[p]['lines'] += copy.deepcopy(newLines)
    
    for l in res[p]['lines']:
        l.Draw()
    cans.cd()

cans.cd()

zero.Draw()
box1.Draw()
box2.Draw()
box3.Draw()


## need a legend
leg = ROOT.TLegend(0.05,0.85-0.04*len(ordering),0.40,0.85)
leg.SetFillColor(ROOT.kWhite)
leg.SetShadowColor(ROOT.kWhite)
leg.SetBorderSize(0)
leg.SetTextSize(0.035)
leg.AddEntry(res[0]['lines'][0],  "#bf{CMS 77.5 fb^{-1} (95% CL)}", 'l')
if args.model == 'EFT':
    leg.AddEntry(res[0]['lines'][3],  "#bf{CMS 35.9 fb^{-1} (95% CL)}", 'l')
    leg.AddEntry(res[0]['lines'][6],  "#bf{ATLAS 36.1 fb^{-1} (95% CL)}", 'l')
    leg.AddEntry(res[0]['lines'][9],  "#bf{SMEFiT (95% CL)}", 'l')
    leg.AddEntry(res[0]['lines'][12], "#bf{TopFitter (95% CL)}", 'l')
    leg.AddEntry(res[0]['lines'][15], "#bf{Indirect (68% CL)}", 'l')
else:
    leg.AddEntry(res[2]['lines'][3],  "#bf{~prev. CMS (68% CL)}", 'l')

leg.Draw()


## finish it off

latex1 = ROOT.TLatex()
latex1.SetNDC()
latex1.SetTextSize(0.06)
latex1.SetTextAlign(11)

if args.preliminary:
    latex1.DrawLatex(0.03,0.94,'CMS #bf{#it{Preliminary}}')
else:
    latex1.DrawLatex(0.03,0.94,'CMS')

latex2 = ROOT.TLatex()
latex2.SetNDC()
latex2.SetTextSize(0.045)
latex2.SetTextAlign(11)
for i,r in enumerate(res):
    latex2.DrawLatex(0.84, 0.84-0.4*(i/2.), '#bf{%s}'%r['tex'])

plotDir = plot_directory + "summary/"

if not os.path.isdir(plotDir):
    os.makedirs(plotDir)

postFix = '_BSM' if args.model == 'BSM' else '_EFT'
if args.preliminary: postFix += '_preliminary'

if args.testGrayscale:
    postFix += '_gray'

for e in [".png",".pdf",".root"]:
    cans.Print(plotDir+"summaryResult"+postFix+e)

