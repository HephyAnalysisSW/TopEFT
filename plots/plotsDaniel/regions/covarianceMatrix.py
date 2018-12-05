import shutil, os
import ROOT
from array import array
import math
import pickle
import numpy as np
import copy

from TopEFT.Tools.user import combineReleaseLocation as releaseLocation

import re
def natural_sort(list, key=lambda s:s):
    """
    Sort the list into natural alphanumeric order.
    http://stackoverflow.com/questions/4836710/does-python-have-a-built-in-function-for-string-natural-sort
    """
    def get_alphanum_key_func(key):
        convert = lambda text: int(text) if text.isdigit() else text 
        return lambda s: [convert(c) for c in re.split('([0-9]+)', key(s))]
    sort_key = get_alphanum_key_func(key)

    lc = sorted(list, key=sort_key)
    return lc

def getCovariance(fname):
    import uuid, os
    ustr          = str(uuid.uuid4())
    uniqueDirname = os.path.join(releaseLocation, ustr)
    print "Creating %s"%uniqueDirname
    os.makedirs(uniqueDirname)

    if fname is not None:  # Assume card is already written when fname is not none
      filename = os.path.abspath(fname)
    else:
      filename = fname if fname else os.path.join(uniqueDirname, ustr+".txt")
      self.writeToFile(filename)
    covFilename = filename.replace('.txt', '_mlfit.root')
    shapeFilename = filename.replace('.txt', '_shape.txt')
    
    assert os.path.exists(filename), "File not found: %s"%filename
    combineCommand = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;combineCards.py %s -S > myshapecard.txt "%fname

    #set workspace
    workspaceCommand = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;text2workspace.py myshapecard.txt"

    #Run fit
    fitCommand = "cd "+uniqueDirname+";eval `scramv1 runtime -sh`;combine -M FitDiagnostics --freezeParameters r --saveShapes --saveWithUnc --numToysForShape 100 --saveOverall myshapecard.root"
    print fitCommand

    os.system(combineCommand)
    os.system(workspaceCommand)
    os.system(fitCommand)

    f1 = ROOT.TFile(uniqueDirname+"/fitDiagnostics.root")

    postfit = f1.Get("shapes_fit_s")
    prefit  = f1.Get("shapes_prefit")

    # should also extract yields here to directly obtain chi2

    cov_postfit     = copy.deepcopy(postfit.Get("overall_total_covar"))
    cov_prefit      = copy.deepcopy(prefit.Get("overall_total_covar"))
    total_postfit   = copy.deepcopy(postfit.Get("total_overall"))
    total_prefit    = copy.deepcopy(prefit.Get("total_overall"))

    data            = copy.deepcopy(postfit.Get("total_data"))

    del postfit, prefit

    f1.Close()

    del f1

    shutil.rmtree(uniqueDirname)

    return {"postfit":cov_postfit, "prefit":cov_prefit, "yield_postfit":total_postfit, "yield_prefit":total_prefit, "data":data}

#f1 = ROOT.TFile("/afs/hephy.at/work/d/dspitzbart/top/devel/CMSSW_8_1_0/src/fitDiagnostics.root")

def getMatrix(h2, binNumbers):
    binNames = []
    matrix = {}
    nbins = len(binNumbers)

    for i in range(1, nbins+1):
        #binNames.append(h2.GetXaxis().GetBinLabel(i))
        matrix[h2.GetXaxis().GetBinLabel(i)] = {}
        for j in range(1, nbins+1):
            matrix[h2.GetXaxis().GetBinLabel(i)][h2.GetXaxis().GetBinLabel(j)] = h2.GetBinContent(i,j)

    sorted_cov = ROOT.TH2D('cov','',nbins,0,nbins,nbins,0,nbins)
    #binNames = natural_sort(binNames)
    
    cov = np.zeros((nbins,nbins))
    diag = np.zeros((nbins,nbins))
    diag_corr = np.zeros((nbins, nbins))
    
    for i,k in enumerate(binNumbers):
        diag_corr[i,i] = math.sqrt(h2.GetBinContent(k,k))
        for j,l in enumerate(binNumbers):
            cov[i][j] = h2.GetBinContent(k,l)#matrix[k][l]
            if i==j:
                diag[i][j] = h2.GetBinContent(k,l)

    return cov,diag, diag_corr

def getSortedBinNumber(h1):
    binNames = []
    indices = []
    nbins = h1.GetNbinsX()
    for i in range(1, nbins+1):
        binNames.append(h1.GetXaxis().GetBinLabel(i))

    sortedBinNames = natural_sort(binNames)

    #sortedBinNames = sortedBinNames[0:15]# + sortedBinNames[30:45]


    for x in sortedBinNames:
        binNumber = binNames.index(x)+1
        if h1.GetBinContent(binNumber)>0:
            indices.append(binNames.index(x)+1)

    return indices, sortedBinNames


def getVectorFromHist(h1, binNumbers):
    vector = []

    for b in binNumbers:
        vector.append(h1.GetBinContent(b))

    return np.array(vector)

def getVectorFromGraph(graph, binNumbers):
    vector = []

    for b in binNumbers:
        vector.append(graph.Eval(b-0.5))

    return np.array(vector)


cov = getCovariance("/afs/hephy.at/data/dspitzbart01/TopEFT/results/cardFiles/regionsE_COMBINED_xsec_shape_lowUnc_SRandCR/dim6top_LO_currents/dim6top_LO_ttZ_ll.txt")

binNumbers,sortedBinNames = getSortedBinNumber(cov["yield_postfit"])

cov_prefit, cov_prefit_diag, cov_prefit_diag_corr     = getMatrix(cov["prefit"], binNumbers)
cov_postfit, cov_postfit_diag, cov_postfit_diag_corr   = getMatrix(cov["postfit"], binNumbers)

obs = getVectorFromGraph(cov["data"], binNumbers)
exp_postfit = getVectorFromHist(cov["yield_postfit"], binNumbers)
exp_prefit  = getVectorFromHist(cov["yield_prefit"], binNumbers)

# Chi2 for postfit

R_postfit = obs - exp_postfit

cov_postfit_inv = np.linalg.inv(cov_postfit)

chi2_postfit = np.dot(cov_postfit_inv, R_postfit)
chi2_postfit = np.dot(R_postfit,chi2_postfit)

cov_postfit_diag_inv = np.linalg.inv(cov_postfit_diag)
cov_postfit_diag_corr_inv = np.linalg.inv(cov_postfit_diag_corr)
chi2_postfit_uncor = np.dot(cov_postfit_diag_inv, R_postfit)
chi2_postfit_uncor = np.dot(R_postfit, chi2_postfit_uncor)


## get the correlation matrix
corr = np.dot(cov_postfit_diag_corr_inv, cov_postfit)
corr = np.dot(corr, cov_postfit_diag_corr_inv)

nbins = len(binNumbers)
sorted_corr = ROOT.TH2D('corr','',nbins,0,nbins,nbins,0,nbins)
for i,k in enumerate(sortedBinNames[:nbins]):
    #if i < nSR:
    sorted_corr.GetXaxis().SetBinLabel(i+1, str(i+1))#SRnames[i])
    sorted_corr.GetYaxis().SetBinLabel(i+1, str(i+1))#SRnames[i])
    for j,l in enumerate(sortedBinNames[:nbins]):
        sorted_corr.SetBinContent(i+1, j+1, corr[i][j])

sorted_corr.GetXaxis().LabelsOption("v")
sorted_corr.GetZaxis().SetRangeUser(-1.0, 1.0)
c3 = ROOT.TCanvas('c3','c3',700,700)

pad2=ROOT.TPad("pad2","Main",0.,0.,1.,1.)
pad2.SetRightMargin(0.15)
pad2.SetTopMargin(0.06)
pad2.SetBottomMargin(0.12)
pad2.Draw()
pad2.cd()

sorted_corr.Draw("colz")

latex1 = ROOT.TLatex()
latex1.SetNDC()
latex1.SetTextSize(0.04)
latex1.SetTextAlign(11) # align right

latex1.DrawLatex(0.10,0.95,'CMS #bf{#it{Private Work}}')

outname = 'correlation'
filetypes = ['.png','.pdf','.root']
plot_dir = '/afs/hephy.at/user/d/dspitzbart/www/TopEFT/correlation/'
for f in filetypes:
    c3.Print(plot_dir+outname+f)


chi2_primitive = 0
for i,r in enumerate(R_postfit):
    #if i >= 30 and i<45:
    chi2_primitive += (r**2 / cov_postfit[i][i])

print "Results"
print chi2_postfit
print chi2_primitive

# Chi2 for prefit

R_prefit = obs - exp_prefit

cov_prefit_inv = np.linalg.inv(cov_prefit)

chi2_prefit = np.dot(cov_prefit_inv, R_prefit)
chi2_prefit = np.dot(R_prefit,chi2_prefit)

#cov_inv = np.linalg.inv(cov)

#pickle.dump(cov_inv, file('cov_inv.pkl','w'))

