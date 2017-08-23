from TopEFT.gencode.EFT import *
import TopEFT.gencode.logger as logger

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--model',       action='store', default='HEL_UFO',          nargs='?',   choices=['HEL_UFO'], help="Which madgraph model?")
argParser.add_argument('--process',     action='store', default='ttZ',                  choices=['ttZ','ttH','ttW'], help="Which process?")
argParser.add_argument('--couplings',   action='store', default="cuW_0.01",   nargs='?', help="Give a underscore separated list of the non-zero couplings with their values, e.g. NAME1_VALUE1_NAME2_VALUE2")
argParser.add_argument('--noGridpack',  action='store_true', help="Don't keep the gridpack")
argParser.add_argument('--overwrite',   action='store_true', help="Overwrite exisiting x-sec calculation and gridpack")
argParser.add_argument('--logLevel',    action='store', nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], default='INFO', help="Log level for logging" )

args = argParser.parse_args()

logger = logger.get_logger(args.logLevel, logFile = None)


toList = args.couplings.split("_")
activeCouplings = zip(toList[::2], map(float,toList[1::2]))

logger.info("Setting following coefficients: %s",activeCouplings)

config = configuration(args.model)
config.setup()

if args.model == "HEL_UFO":
    coup = couplings()
    coup.addBlock("newcoup", HEL_couplings_newcoup)
    for c in activeCouplings:
        if not coup.setCoupling(c[0],c[1]):
            raise NotImplementedError("Coupling %s is not known"%c[0])

p = process(args.process, 50000, config)
p.addCoupling(coup)
p.run(keepGridpack = not args.noGridpack, overwrite = args.overwrite)

config.clean()

logger.info("Done!")

