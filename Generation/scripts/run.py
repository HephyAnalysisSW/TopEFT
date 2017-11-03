#!/usr/bin/env python

# Standard imports
import argparse
import os

# TopEFT imports
from TopEFT.Generation.Configuration import Configuration
from TopEFT.Generation.Process       import Process
from TopEFT.tools.u_float         import u_float

# Logging
import TopEFT.tools.logger as logger

#find all processes
process_path = os.path.expandvars("$CMSSW_BASE/src/TopEFT/Generation/data/processCards")
processes    = [os.path.splitext(f)[0] for f in os.listdir(process_path) if os.path.isfile(os.path.join(process_path, f)) and f.endswith('.dat')]


argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--process',     action='store',         default='ttZ',      choices=processes,     help="Which process?")
argParser.add_argument('--model',       action='store',         default='HEL_UFO',  choices=['ewkDM', 'ewkDM2', 'ewkDMGZ', 'HEL_UFO', 'TopEffTh', 'dim6top_LO'], help="Which madgraph model?")
argParser.add_argument('--couplings',   action='store',         default=[],         nargs='*',  type = str, help="Give a list of the non-zero couplings with values, e.g. NAME1 VALUE1 NAME2 VALUE2")
argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite exisiting x-sec calculation and gridpack")
argParser.add_argument('--keepWorkspace',   action='store_true',    help="keep the temporary workspace?")
argParser.add_argument('--nEvents',     action='store',         default = 50000,    type=int, help="Number of Events" )
argParser.add_argument('--logLevel',    action='store',         nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], default='INFO', help="Log level for logging" )
argParser.add_argument('--makeGridpack',action='store_true',    help="make gridPack?" )
argParser.add_argument('--calcXSec',    action='store_true',    help="calculate x-sec?" )

args = argParser.parse_args()

logger = logger.get_logger(args.logLevel, logFile = None)

logger.debug("Coupling arguments: %r", args.couplings )

# Single argument -> interpret as file
if len(args.couplings) == 1 and os.path.isfile(args.couplings[0]) :
    with open(args.couplings[0], 'r') as f:
        param_points = [ line.rstrip().split() for line in f.readlines() ]

# Interpret couplings 
#elif len(args.couplings)>=2:
elif len(args.couplings)==0 or len(args.couplings)>=2:
    # make a list of the form [ ['c1', v1, v2, ...], ['c2', ...] ] so we can recourse in the couplings c1,c2,... 
    coupling_list = []
    for a in args.couplings:
        try:
            val = float(a)
        except ValueError:
            coupling_list.append( [ a, [] ] )
            val = None

        if val: coupling_list[-1][1].append( float(a) )

    # recursively make a for loop over all couplings
    def recurse( c_list ):
        var, vals = c_list[-1]
        pairs     = [ (var, val) for val in vals ]
        if len(c_list)>1:
            rec       = recurse(c_list[:-1])
            return [ r + p for p in pairs for r in rec] 
        else:
            return pairs

    param_points = recurse( coupling_list ) if len(coupling_list)>0 else [[]]
    
else:
    logger.error("Need an even number of coupling arguments of the format coupling1, value1, value2, ... , coupling2, value3, ... . Got %r", args.couplings )
    raise ValueError

# Create configuration class
config = Configuration( model_name = args.model )

# Process all the coupling points
for i_param_point, param_point in enumerate(param_points):

    logger.info( "Processing parameter point %i/%i", i_param_point+1, len(param_points) )

    # Interpret coupling argument list
    names  = param_point[::2]
    values = map(float,param_point[1::2])

    modification_dict = {c:v for c,v in zip( names, values ) }

    # Let's not leave the user in the dark
    logger.info("Model:        %s", args.model)
    logger.info("Process:      %s", args.process)
    logger.info("Couplings:    %s", ", ".join( [ "%s=%5.4f" % c for c in modification_dict.items()] ))

    # make process
    p = Process(process = args.process, nEvents = args.nEvents, config = config) 

    # Make grid pack
    if args.makeGridpack: 
        gridpack = p.makeGridpack(modified_couplings = modification_dict, overwrite = args.overwrite)

    # calculate x-sec
    if args.calcXSec:
        xsec     = p.xsec(modified_couplings = modification_dict, overwrite = args.overwrite)
        logger.info("xsec: %s ", repr(xsec) )

if not args.keepWorkspace: config.cleanup()
