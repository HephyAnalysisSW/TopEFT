import ROOT
ROOT.gROOT.LoadMacro("$CMSSW_BASE/src/TopEFT/Tools/scripts/niceColorPalette.C")

def niceColorPalette(n=255):
    ROOT.niceColorPalette(n)

def redColorPalette(n=255):
    ROOT.redColorPalette(n)

def newColorPalette(n=255):
    ROOT.newColorPalette(n)



