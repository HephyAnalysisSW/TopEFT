''' Class to construct & cache signal reweighting templates
'''

# Standard imports
import ROOT
import os

# RootTools
from RootTools.core.standard import *

# TopEFT
from TopEFT.Tools.PickleCache import PickleCache

class SignalReweighting:

    def __init__( self, source_sample, target_sample, cacheDir = None):

        self.source_sample = source_sample
        self.target_sample = target_sample 
        self.initCache( cacheDir )

        self.cosThetaStar_binning = [ i/10. for i in range(-10,11) ] 
        self.Z_pt_binning         = [ 0, 50, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 1000 ] 
        self.template_draw_string = 'Z_cosThetaStar:Z_pt'

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

    def cachedTemplate( self, selection, weight = 'weight', save = True, overwrite = False):

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

    def makeTemplate( self, selection, weight = 'weight'):
        logger.info( "Make polarisation template for sample %s and selection %s and weight %s", self.sample.name, selection, weight )

        h_source = self.source_sample.get2DHistoFromDraw(self.template_draw_string , ( self.cosThetaStar_binning, self.Z_pt_binning), selectionString = selection, weightString = weight )
        if h_source.Integral()>0:
            h_source.Scale(1./h_source.Integral())
        else:
            raise ValueError
        h_target = self.source_sample.get2DHistoFromDraw(self.template_draw_string , ( self.cosThetaStar_binning, self.Z_pt_binning), selectionString = selection, weightString = weight )
        if h_target.Integral()>0:
            h_target.Scale(1./h_target.Integral())
        else:
            raise ValueError

        h_target.Divide( h_source ) 
        template = h_target 

        return template

if __name__ == "__main__":

    from TopEFT.samples.gen_fwlite_benchmarks import *
    signalReweighting = SignalReweighting( source_sample = ewkDM_ttZ_ll_gen, target_sample = ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700 )

