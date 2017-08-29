# Standard imports
import argparse

# TopEFT imports
from TopEFT.gencode.Configuration import Configuration
from TopEFT.gencode.Process       import Process
from TopEFT.tools.u_float         import u_float
# Logging
import TopEFT.tools.logger as logger

argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--process',     action='store',         default='ttZ',      choices=['ttZ','ttH','ttW'],     help="Which process?")
argParser.add_argument('--model',       action='store',         default='HEL_UFO',  choices=['ewkDM', 'HEL_UFO', 'TopEffTh'], help="Which madgraph model?")
#argParser.add_argument('--couplings',   action='store',         default=[],         nargs='*',  type = str, help="Give a list of the non-zero couplings with values, e.g. NAME1 VALUE1 NAME2 VALUE2")
argParser.add_argument('--couplings',   action='store',         default='coups.txt',         type = str, help="Give a file containing the modified couplings")
argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite exisiting x-sec calculation and gridpack")
argParser.add_argument('--logLevel',    action='store',         nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], default='INFO', help="Log level for logging" )

args = argParser.parse_args()

logger = logger.get_logger(args.logLevel, logFile = None)

# Create configuration class
config = Configuration( model_name = args.model, modified_couplings = {} )

with open(args.couplings, 'r') as f:
    lines = f.readlines()

for line in lines:
    couplings = line.replace('\n','').split(' ')
    
    # Interpret coupling argument list
    coupling_names  = couplings[::2]
    coupling_values = map(float,couplings[1::2])
    
    modified_couplings = {c:v for c,v in zip( coupling_names, coupling_values ) }
    
    # Let's not leave the user in the dark
    logger.info("Model:        %s", args.model)
    logger.info("Process:      %s", args.process)
    logger.info("Couplings:    %s", ", ".join( [ "%s=%5.4f" % c for c in modified_couplings.items()] ))
    
    p = Process(process = args.process, nEvents = 50000, config = config)
    xsec_val = p.xsec(overwrite = args.overwrite, modified_couplings = modified_couplings)

    logger.info("Done! Calculated xsec: %s ", repr(xsec_val) )
    
config.cleanup()
    
