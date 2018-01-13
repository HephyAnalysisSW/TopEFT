#!/usr/bin/env python

'''
Generate events from gridpacks stored locally, using the hephy batch system.
This script creates the txt file to be used with submitBatch.py
Gridpacks can be selected using a qualifier string.
A sandbox is created in the tmp_directory.
'''

import os

# TopEFT
from TopEFT.Tools.user import results_directory
from TopEFT.Tools.user import tmp_directory
import uuid

CMSSW_BASE = os.path.expandvars("$CMSSW_BASE")
cfg_path = os.path.join(CMSSW_BASE, 'src/TopEFT/Generation/production/cfg/')

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--gridpackDir',           action='store',      default='/afs/hephy.at/data/dspitzbart01/TopEFT/results/gridpacks/',          nargs='?', help="Where are the gridpacks?")
argParser.add_argument('--qualifier',             action='store',      default='dim6top_LO_ttZ_ll',          nargs='?', help="Any criteria on the name of the gridpack?")
argParser.add_argument('--maxEvents',           action='store',      default=100000,          nargs='?', help="How many events?")
argParser.add_argument('--nJetMax',           action='store',      default=0,          nargs='?', help="How many jets to match?")
argParser.add_argument('--outDir',           action='store',      default='/afs/hephy.at/data/dspitzbart01/TopEFT/genSamples/',          nargs='?', help="Where are the gridpacks?")
argParser.add_argument('--outFile',           action='store',      default='submit.txt',          nargs='?', help="Outputfile?")
argParser.add_argument('--cfg',                     action='store', default='GEN.py',               help="Which cfg from Generation/production/cfg to use?")

args = argParser.parse_args()

gridpacks = [ gp for gp in os.listdir(args.gridpackDir) if args.qualifier in gp ]

baseDir = os.path.abspath('.')
cfg     = os.path.join(cfg_path, args.cfg)

with open(args.outFile, 'w') as f:
    for gp in gridpacks:
        gpName      = gp.replace(".tar.xz","").replace(".","p").replace("-","m")
        uniqueDir   = uuid.uuid4().hex
        uPath       = os.path.join(tmp_directory, uniqueDir)
        line        = "mkdir %s; cp %s %s; cd %s; cmsRun %s gridpack=%s/%s maxEvents=%s nJetMax=%s outputDir=%s/%s/; cd %s; rm -rf %s\n"%(uPath, cfg, uPath, uPath, args.cfg, args.gridpackDir, gp, args.maxEvents, args.nJetMax, args.outDir, gpName, baseDir, uPath)
        #print line
        f.write(line)

print "Created submit file: %s"%args.outFile
print "You can copy the content of 'forSamplesPY.txt' to your sample python file."
print "Samples contained:"

with open('forSamplesPY.txt', 'w') as f:
    for gp in gridpacks:
        gpName      = gp.replace(".tar.xz","").replace(".","p").replace("-","m")
        niceName    = gpName.replace("0000", "")
        line = '{:40}= FWLiteSample.fromFiles({:40} , texName="", files = ["{}/{}/events.root"])\n'.format(niceName, '"%s"'%niceName, args.outDir, gpName)
        print niceName
        f.write(line)

with open('forPPSamplesPY.txt', 'w') as f:
    for gp in gridpacks:
        gpName      = gp.replace(".tar.xz","").replace(".","p").replace("-","m")
        niceName    = gpName.replace("0000", "")
        line = '{:40}= Sample.fromDirectory({:40}, directory = [os.path.join( gen_dir, "{}/")])\n'.format(niceName, '"%s"'%niceName, niceName)
        #print niceName
        f.write(line)


