#!/usr/bin/env python
''' Somewhat obscure 
'''
import ROOT
import os
import argparse
from RootTools.core.Sample import Sample


from TopEFT.Tools.resultsDB     import resultsDB
from TopEFT.Tools.user          import combineReleaseLocation, analysis_results, results_directory, plot_directory

from TopEFT.Analysis.reducedSetup      import Setup

setup = Setup()

cacheFileName = os.path.join(plot_directory, setup.resultsFile)
columns = ['signal', 'exp', 'obs', 'exp1up', 'exp1down', 'exp2up', 'exp2down', 'NLL_prefit', 'dNLL_postfit_r1', 'dNLL_bestfit']

res = resultsDB(cacheFileName, "limits", columns)

def getResult(sample):
    ''' to be extended '''
    key = {"signal":sample.name}
    if res.contains(key):
        return res.getDicts(key)[0]

def addResult(sample, key, value, overwrite):
    print "Adding result for %s"%(sample.name)
    key.update({"signal":sample.name})
    res.add(key, value, overwrite=True)

