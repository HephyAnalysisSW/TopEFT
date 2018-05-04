''' Class to construct & cache MC PU profiles
'''

# Standard imports
import ROOT
import os

# RootTools
from RootTools.core.standard import *

# TopEFT
from TopEFT.Tools.resultsDB import resultsDB

if __name__ == "__main__":

    #
    # Arguments
    # 
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser")
    argParser.add_argument('--logLevel',        action='store',      default='INFO',  nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
    argParser.add_argument('--makePlots',        action='store_true',       help="Make PU profile plots?")
    args = argParser.parse_args()

    # Logger
    import TopEFT.Tools.logger as logger
    import RootTools.core.logger as logger_rt
    logger    = logger.get_logger(   args.logLevel, logFile = None)
    logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)

else:
    # Logger
    import logging
    logger = logging.getLogger(__name__)


class puProfile:

    def __init__( self, source_sample, cacheDir = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/puProfiles/"):
        self.source_sample = source_sample
        self.initCache( cacheDir )
        self.binning        = [ 100, 0, 100 ]
        self.draw_string    = 'nTrueInt'

    def initCache(self, cacheDir):
        self.cache = resultsDB(os.path.join(cacheDir, 'puProfiles.sql'), "puProfile", ["selection", "weight", "source"])

    def uniqueKey( self, *arg ):
        '''No dressing required'''
        return arg

    def cachedTemplate( self, selection, weight = '(1)', save = True, overwrite = False):
        key = {"selection":selection, "weight":weight, "source":self.source_sample.name}
        if (self.cache and self.cache.contains(key)) and not overwrite:
            result = self.cache.get(key)
            logger.info( "Loaded MC PU profile from %s"%(self.cache.database_file) )
            logger.debug( "Key used: %s result: %r"%(key, result) )
        elif self.cache:
            logger.info( "Obtain PU profile for %s"%( key, ) )
            result = self.makeTemplate( selection = selection, weight = weight)
            if result:
                result = self.cache.addData( key, result, overwrite=save )
                logger.info( "Adding PU profile to cache for %s : %r" %( key, result) )
            else:
                logger.warning( "Couldn't create PU profile to cache for %s : %r" %( key, result) )
        else:
            result = self.makeTemplate( selection = selection, weight = weight)
        return result

    def makeTemplate( self, selection, weight = '(1)'):
        logger.info( "Make PU profile for sample %s and selection %s and weight %s", self.source_sample.name, selection, weight )

        h_source = self.source_sample.get1DHistoFromDraw(self.draw_string, self.binning, selectionString = selection, weightString = weight )
        logger.info( "PU histogram contains %s weighted events", h_source.Integral() )
        h_source.Scale(1./h_source.Integral())
        return h_source

if __name__ == "__main__":

    # Get all CMG tuples for caching
    from TopEFT.samples.helpers import fromHeppySample
    from TopEFT.samples.heppy_dpm_samples import *
    from TopEFT.Tools.user import results_directory, plot_directory
    
    allSamples = [ Fall17_heppy_mapper.from_heppy_samplename(a) for a in Fall17_heppy_mapper.heppy_sample_names ]

    for s in allSamples:
        logger.info("Working on samples %s", s.name)
        puProfiles = puProfile( source_sample = s )
        # reweighting selection
        selection = "( 1 )"
        profile = puProfiles.cachedTemplate( selection, weight='genWeight', overwrite=False )

        # plot the MC PU profile
        if args.makePlots:
            profilePlot = Plot.fromHisto( s.name, texX = "nTrueInt", histos = [[profile]])
            plotting.draw( profilePlot, plot_directory = os.path.join( plot_directory, 'puProfiles'), logY = True, copyIndexPHP = True, extensions = ["png"])
