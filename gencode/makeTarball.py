from TopEFT.gencode.EFT import *


import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--model',       action='store', default='HEL_UFO',          nargs='?',   choices=['HEL_UFO'], help="Which madgraph model?")
argParser.add_argument('--process',     action='store', default='ttZ',                  choices=['ttZ','ttH','ttW'], help="Which process?")
argParser.add_argument('--couplings',   action='store', default="cuW 0.01",   nargs='?', help="Give a list of the non-zero couplings with their values, e.g. NAME1 VALUE1 NAME2 VALUE2")
argParser.add_argument('--noGridpack',  action='store_true', help="Don't keep the gridpack")
argParser.add_argument('--overwrite',   action='store_true', help="Overwrite exisiting x-sec calculation and gridpack")

args = argParser.parse_args()

print args.couplings

toList = args.couplings.split(" ")
activeCouplings = zip(toList[::2], map(float,toList[1::2]))


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


