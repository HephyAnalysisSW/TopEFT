#!/usr/bin/env python

# Standard imports
import argparse
import os

# TopEFT imports
from TopEFT.Generation.Configuration import Configuration
from TopEFT.Generation.Process       import Process
from TopEFT.Tools.u_float         import u_float

# Logging
import TopEFT.Tools.logger as logger

#find all processes
process_path = os.path.expandvars("$CMSSW_BASE/src/TopEFT/Generation/data/processCards")
processes    = [os.path.splitext(f)[0] for f in os.listdir(process_path) if os.path.isfile(os.path.join(process_path, f)) and f.endswith('.dat')]


argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--process',     action='store',         default='ttZ',      choices=processes,     help="Which process?")
argParser.add_argument('--model',       action='store',         default='HEL_UFO',  choices=['ewkDM', 'HEL_UFO', 'TopEffTh', 'ewkDMGZ'], help="Which madgraph model?")
argParser.add_argument('--couplings',   action='store',         default=[],         nargs='*',  type = str, help="Give a list of the non-zero couplings with values, e.g. NAME1 VALUE1 NAME2 VALUE2")
argParser.add_argument('--nEvents',     action='store',         default = 50000,    type=int, help="Number of Events" )
argParser.add_argument('--logLevel',    action='store',         nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], default='INFO', help="Log level for logging" )

args = argParser.parse_args()

logger = logger.get_logger(args.logLevel, logFile = None)

if len(args.couplings)%2==0:
    param_points = args.couplings
else:
    logger.error("Need an even number of coupling arguments of the format coupling1, value1, coupling2, value2, ... . Got %r", args.couplings )
    raise ValueError

# Create configuration class
config = Configuration( model_name = args.model )

p = Process(process = args.process, nEvents = args.nEvents, config = config)

names  = param_points[::2]
values = map(float,param_points[1::2])

modification_dict = {c:v for c,v in zip( names, values ) }
modification_dict["process"] = args.process
modification_dict["nEvents"] = args.nEvents

p.xsecDB.getTable(modification_dict)


