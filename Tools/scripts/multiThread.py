#!/usr/bin/env python

import subprocess
import os
import time
import sys


from RootTools.core.Sample import Sample

import argparse
parser = argparse.ArgumentParser(description = "Argument parser")
parser.add_argument('--logLevel', dest="logLevel",       action='store', default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'],             help="Log level for logging")
parser.add_argument("--nThreads", dest="nThreads",       action='store', default='2',          nargs='?', help="How many threads?")
parser.add_argument("--inFile", action='store', default=None, help="Run on which file?")
options = parser.parse_args()

import TopEFT.Tools.logger as logger
logger = logger.get_logger(options.logLevel, logFile = None )


processes = set()
max_processes = int(options.nThreads)

#command = "echo"
command = ""

input_file = options.inFile

if os.path.exists(input_file):
    with open(input_file) as f:
        # Remove everything after #
        # jobs_ = [l.split('#')[0].rstrip() for l in f.readlines() ]
        jobs_ = [ l.rstrip() for l in f.readlines() ]
        # remove empty lines
        jobs_ = filter(lambda l:len(l)>0, jobs_) 
else:
    raise ValueError( "Could not find file %s", input_file )

jobs = []
for job in jobs_:
    # Implement '<job>#SPLITn'
    if job.count('#'):
        job, comment = job.split('#')[:2]
    else:
        comment = None

    # Remove blanks
    if not job.strip(): continue

    args  = job.split() #filter(lambda s:not s.startswith("SPLIT"), cmds)
    if comment is not None and "SPLIT" in comment:
        try:
            n = int(comment.replace("SPLIT", ""))
        except ValueError:
            n = -1
    else:
        n = -1

    if n>0:
        logger.info( "Splitting into %i jobs: %r", n, " ".join( args ) )
        for i in range(n):
            j_args = args+["--nJobs",str(n),"--job",str(i)]
            logger.info( "Queuing job %r", " ".join( j_args ) )
            jobs.append(j_args)
    else:
        logger.info( "No splitting. Queuing job %r", " ".join( args ) )
        jobs.append(args)

extra_args = []
#if len(sys.argv)>=2:
#    extra_args = sys.argv[2:]

for cmds in jobs:
    if command!="": cmds_ = [command] + cmds + extra_args
    else:           cmds_ = cmds + extra_args
    logger.info( "Processing: %s", " ".join(cmds_) )
    processes.add(subprocess.Popen( cmds_ ))
    if len(processes) >= max_processes:
        os.wait()
        processes.difference_update(
            [p for p in processes if p.poll() is not None])

#Check if all the child processes were closed
for p in processes:
    if p.poll() is None:
        p.wait()
