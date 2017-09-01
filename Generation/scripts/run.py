#!/usr/bin/env python

# Standard imports
import argparse

# TopEFT imports
from TopEFT.Generation.Configuration import Configuration
from TopEFT.Generation.Process       import Process
from TopEFT.tools.u_float         import u_float
# Logging
import TopEFT.tools.logger as logger

argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--process',     action='store',         default='ttZ',      choices=['ttZ','ttH','ttW'],     help="Which process?")
argParser.add_argument('--model',       action='store',         default='HEL_UFO',  choices=['ewkDM', 'HEL_UFO', 'TopEffTh'], help="Which madgraph model?")
argParser.add_argument('--couplings',   action='store',         default=[],         nargs='*',  type = str, help="Give a list of the non-zero couplings with values, e.g. NAME1 VALUE1 NAME2 VALUE2")
argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite exisiting x-sec calculation and gridpack")
argParser.add_argument('--keepWorkspace',   action='store_true',    help="keep the temporary workspace?")
argParser.add_argument('--nEvents',     action='store',         default = 50000,    type=int, help="Number of Events" )
argParser.add_argument('--logLevel',    action='store',         nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], default='INFO', help="Log level for logging" )
argParser.add_argument('--makeGridpack',action='store_true',    help="make gridPack?" )
argParser.add_argument('--calcXSec',    action='store_true',    help="calculate x-sec?" )

args = argParser.parse_args()

logger = logger.get_logger(args.logLevel, logFile = None)

# Single argument -> interpret as file
if len(args.couplings) == 1:
    with open(args.couplings[0], 'r') as f:
        param_points = [ line.rstrip().split() for line in f.readlines() ]
elif len(args.couplings)%2==0:
# Even number of arguments -> one line
    param_points = [args.couplings]
else:
    logger.error("Need an even number of coupling arguments of the format coupling1, value1, coupling2, value2, ... . Got %r", args.couplings )
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

    
config.cleanup()
    
