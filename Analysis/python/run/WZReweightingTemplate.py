''' Class to construct & cache signal reweighting templates
'''

# Standard imports
import ROOT
import os

# RootTools
from RootTools.core.standard import *

# TopEFT
#from TopEFT.Tools.PickleCache import PickleCache
from TopEFT.Tools.resultsDB import resultsDB
#from TopEFT.Analysis.Cache import Cache

if __name__ == "__main__":

    #
    # Arguments
    # 
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser")
    argParser.add_argument('--logLevel',        action='store',      default='INFO',  nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
    argParser.add_argument('--makePlots',        action='store_true',       help="Make reweighting matrix plots?")
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


class WZReweighting:

    def __init__( self, source_sample, target_sample, cacheDir = None):

        self.source_sample = source_sample
        self.target_sample = target_sample 
        self.initCache( cacheDir )

        self.Z_pt_binning         = [ 0, 50, 100, 150, 200, 250, 300, 400, 500, 2000 ]
        self.template_draw_string = 'Z_pt'

    def initCache(self, cacheDir):
        self.cache = resultsDB(os.path.join(cacheDir, 'WZReweightingTemplate.sql'), "signalWeights", ["selection", "weight", "source", "target"])

    def uniqueKey( self, *arg ):
        '''No dressing required'''
        return arg


    def cachedReweightingFunc( self, selection, weight = '(1)', save = True, overwrite = False):

        t = self.cachedTemplate( selection=selection, weight=weight, save=save, overwrite=overwrite)
        
        def reweight_func( pt ):
            return t.GetBinContent( t.FindBin( pt ) )

        return reweight_func
            

    def cachedTemplate( self, selection, weight = '(1)', save = True, overwrite = False):
        
        key = {"selection":selection, "weight":weight, "source":self.source_sample.name, "target":self.target_sample.name}
        #key =  self.uniqueKey( selection, weight, self.source_sample.name, self.target_sample.name)
        if (self.cache and self.cache.contains(key)) and not overwrite:
            result = self.cache.get(key)
            logger.info( "Loaded reweighting template from %s for %s : %r"%(self.cache.database_file, key, result) )
            logger.debug( "With properties %s : %s"%( key, result) )
        elif self.cache:
            logger.info( "Obtain template for %s"%( key, ) )
            result = self.makeTemplate( selection = selection, weight = weight)
            if result:
                result = self.cache.addData( key, result, overwrite=save )
                #print "Adding template to cache for %s : %r" %( key, result)
                logger.info( "Adding template to cache for %s : %r" %( key, result) )
            else:
                logger.info( "Couldn't create template to cache for %s : %r" %( key, result) )
        else:
            result = self.makeTemplate( selection = selection, weight = weight)
        return result

    def makeTemplate( self, selection, weight = '(1)'):
        logger.info( "Make polarisation template for source_sample %s and target_sample %s and selection %s and weight %s", self.source_sample.name, self.target_sample.name, selection, weight )

        h_source = self.source_sample.get1DHistoFromDraw(self.template_draw_string , self.Z_pt_binning, selectionString = selection, weightString = weight, binningIsExplicit = True, addOverFlowBin='Upper' )
        logger.info( "Source histogram contains %s weighted events", h_source.Integral() )
        if h_source.Integral()>0:
            h_source.Scale(1./h_source.Integral())
        else:
            return False
            raise ValueError
        h_target = self.target_sample.get1DHistoFromDraw(self.template_draw_string , self.Z_pt_binning, selectionString = selection, weightString = weight, binningIsExplicit = True, addOverFlowBin='Upper' )
        logger.info( "Target histogram contains %s weighted events", h_target.Integral() )
        if h_target.Integral()>0:
            h_target.Scale(1./h_target.Integral())
        else:
            return False
            raise ValueError

        h_target.Divide( h_source ) 
        template = h_target 

        return template

if __name__ == "__main__":

    from TopEFT.samples.color import color
    from TopEFT.Tools.user import results_directory, plot_directory
    from TopEFT.Tools.cutInterpreter    import cutInterpreter

    # Samples
    data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
    postProcessing_directory = "TopEFT_PP_2016_mva_v16/trilep/"
    
    dirs = {}
    dirs['WZTo3LNu_amcatnlo']   = ["WZTo3LNu_amcatnlo"]
    dirs['WZTo3LNu']     = ['WZTo3LNu_comb']
    directories = { key : [ os.path.join( data_directory, postProcessing_directory, dir) for dir in dirs[key]] for key in dirs.keys()}

    source  = Sample.fromDirectory(name="WZTo3LNu_amcatnlo", treeName="Events", isData=False, color=color.WZ-2, texName="WZ MG (NLO)", directory=directories['WZTo3LNu_amcatnlo'])
    target  = Sample.fromDirectory(name="WZTo3LNu_powheg", treeName="Events", isData=False, color=color.WZ+2, texName="WZ powheg (NLO)", directory=directories['WZTo3LNu'])

    # reweighting class
    cacheDir = os.path.join( results_directory, 'WZReweightingTemplate' )
    if not os.path.isdir(cacheDir): os.makedirs(cacheDir)

    WZReweighting = WZReweighting( source_sample = source, target_sample = target, cacheDir = cacheDir)

    # reweighting selection
    selection = cutInterpreter.cutString('trilep-Zcand-onZ-lepSelTTZ-njet1p')
    
    # reweighting function
    f = WZReweighting.cachedReweightingFunc( selection, weight='weight' )
    
    # plot the reweighting matrix
    if args.makePlots:
        histo = WZReweighting.cachedTemplate( selection, weight='weight', overwrite=False )
        
        histo.style = styles.lineStyle( ROOT.kOrange+3, errors=True)
        histoPlot = Plot.fromHisto( target.name, texY = "a.u.", texX = "p_{T}(Z) (GeV)", histos = [[histo]])

        

        plotting.draw( histoPlot, plot_directory = os.path.join( plot_directory, 'WZreweighting', source.name), logX=True, logY = False, copyIndexPHP = True, extensions = ["png"])
