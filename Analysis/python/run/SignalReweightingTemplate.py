''' Class to construct & cache signal reweighting templates
'''

# Standard imports
import ROOT
import os

# RootTools
from RootTools.core.standard import *

# TopEFT
from TopEFT.Tools.PickleCache import PickleCache

if __name__ == "__main__":

    #
    # Arguments
    # 
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser")
    argParser.add_argument('--logLevel',        action='store',      default='INFO',  nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
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


class SignalReweighting:

    def __init__( self, source_sample, target_sample, cacheDir = None):

        self.source_sample = source_sample
        self.target_sample = target_sample 
        self.initCache( cacheDir )

        self.cosThetaStar_binning = [ i/5. for i in range(-5,6) ] 
        self.Z_pt_binning         = [ 0, 50, 100, 150, 200, 250, 300, 400, 500, 2000 ]
        self.template_draw_string = 'Z_pt:Z_cosThetaStar'

    def initCache(self, cacheDir):
        if cacheDir:
            self.cacheDir = cacheDir
            try:    os.makedirs(cacheDir)
            except: pass
            cacheFileName = os.path.join(cacheDir, 'signalReweightingTemplates.pkl')
            self.cache    = PickleCache(cacheFileName)
        else:
            self.cache=None

    def uniqueKey( self, *arg ):
        '''No dressing required'''
        return arg


    def cachedReweightingFunc( self, selection, weight = '(1)', save = True, overwrite = False):

        t = self.cachedTemplate( selection=selection, weight=weight, save=save, overwrite=overwrite)

        def reweight_func( pt, cosThetaStar):
            return t.GetBinContent( t.FindBin( cosThetaStar, pt ) )

        return reweight_func
            

    def cachedTemplate( self, selection, weight = '(1)', save = True, overwrite = False):

        key =  self.uniqueKey( selection, weight, self.source_sample.name, self.target_sample.name)
        if (self.cache and self.cache.contains(key)) and not overwrite:
            result = self.cache.get(key)
            logger.debug( "Loading cached template for %s : %s"%( key, result) )
        elif self.cache:
            logger.info( "Obtain template for %s"%( key, ) )
            result = self.makeTemplate( selection = selection, weight = weight)
            result = self.cache.add( key, result, save=save)
            #print "Adding template to cache for %s : %r" %( key, result)
            logger.debug( "Adding template to cache for %s : %r" %( key, result) )
        else:
            result = self.makeTemplate( selection = selection, weight = weight)
        return result

    def makeTemplate( self, selection, weight = '(1)'):
        logger.info( "Make polarisation template for source_sample %s and target_sample %s and selection %s and weight %s", self.source_sample.name, self.target_sample.name, selection, weight )

        h_source = self.source_sample.get2DHistoFromDraw(self.template_draw_string , ( self.cosThetaStar_binning, self.Z_pt_binning), selectionString = selection, weightString = weight, binningIsExplicit = True )
        logger.info( "Source histogram contains %s weighted events", h_source.Integral() )
        if h_source.Integral()>0:
            h_source.Scale(1./h_source.Integral())
        else:
            raise ValueError
        h_target = self.target_sample.get2DHistoFromDraw(self.template_draw_string , ( self.cosThetaStar_binning, self.Z_pt_binning), selectionString = selection, weightString = weight, binningIsExplicit = True )
        logger.info( "Target histogram contains %s weighted events", h_target.Integral() )
        if h_target.Integral()>0:
            h_target.Scale(1./h_target.Integral())
        else:
            raise ValueError

        h_target.Divide( h_source ) 
        template = h_target 

        return template

if __name__ == "__main__":

    # Benchmarks for testing
    from TopEFT.samples.gen_fwlite_benchmarks import *
    from TopEFT.Tools.user import results_directory, plot_directory

    # reweighting class
    cacheDir = os.path.join( results_directory, 'SignalReweightingTemplate' )
    
    source_gen = dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_0p00

    for target in allSamples_dim6top:
        target_gen = target

        signalReweighting = SignalReweighting( source_sample = source_gen, target_sample = target_gen, cacheDir = cacheDir)

        # reweighting selection
        selection = "Sum$(GenJet_pt>30)>=3&& abs(Z_mass-91.2)<10&&(abs(Z_daughterPdg)==11 || abs(Z_daughterPdg)==13 || abs(Z_daughterPdg)==15 )"
        
        # reweighting function
        f = signalReweighting.cachedReweightingFunc( selection )
        
        # plot the reweighting matrix
        matrix = signalReweighting.cachedTemplate( selection )
        
        matrixPlot = Plot2D.fromHisto( target_gen.name, texY = "p_{T}(Z)", texX = "cos(#Theta*)", histos = [[matrix]])
        matrixPlot.drawOption = "colz text"

        def optimizeLogZ(histo):
            histo.GetZaxis().SetMoreLogLabels()
            histo.GetZaxis().SetNoExponent()

        ROOT.gStyle.SetPaintTextFormat("2.2f")        
         
        plotting.draw2D( matrixPlot, plot_directory = os.path.join( plot_directory, 'reweightingMatrices', source_gen.name), logY = True, copyIndexPHP = True, zRange = [0.5, 5.], extensions = ["png"], histModifications = [optimizeLogZ])
    
