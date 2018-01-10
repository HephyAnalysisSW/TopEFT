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
    argParser.add_argument('--logLevel',           action='store',      default='INFO',  nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
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

        self.cosThetaStar_binning = [ i/10. for i in range(-10,11) ] 
        self.Z_pt_binning         = [ 0, 50, 100, 150, 200, 250, 300, 400, 1000 ] 
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
            self.cache.add( key, result, save=save)
            #print "Adding template to cache for %s : %r" %( key, result)
            logger.debug( "Adding template to cache for %s : %r" %( key, result) )
        else:
            result = self.makeTemplate( selection = selection, weight = weight)
        return result

    def makeTemplate( self, selection, weight = '(1)'):
        logger.info( "Make polarisation template for source_sample %s and target_sample %s and selection %s and weight %s", self.source_sample.name, self.target_sample.name, selection, weight )

        h_source = self.source_sample.get2DHistoFromDraw(self.template_draw_string , ( self.cosThetaStar_binning, self.Z_pt_binning), selectionString = selection, weightString = weight, binningIsExplicit = True )
        if h_source.Integral()>0:
            h_source.Scale(1./h_source.Integral())
        else:
            raise ValueError
        h_target = self.target_sample.get2DHistoFromDraw(self.template_draw_string , ( self.cosThetaStar_binning, self.Z_pt_binning), selectionString = selection, weightString = weight, binningIsExplicit = True )
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
    #cacheDir = os.path.join( results_directory, 'SignalReweightingTemplate' )
    cacheDir = None 
    signalReweighting = SignalReweighting( source_sample = ewkDM_ttZ_ll_gen, target_sample = ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700, cacheDir = cacheDir)

    # reweighting selection
    #selection = "Sum$(GenJet_pt>40)>=3&& abs(Z_mass-91.2)<10&&(abs(Z_daughterPdg)==11 || abs(Z_daughterPdg)==13 || abs(Z_daughterPdg)==15 )&&Sum$(GenLep_pt>0&&{l_match})>=3".format(l_match="(abs(GenLep_motherPdgId)==23||abs(GenLep_motherPdgId)==24)")
    selection = "(1)"#Sum$(GenJet_pt>40)>=3&& abs(Z_mass-91.2)<10&&(abs(Z_daughterPdg)==11 || abs(Z_daughterPdg)==13 )"

    # reweighting function
    f = signalReweighting.cachedReweightingFunc( selection )

    # A real world test
    # reco signals
    postProcessing_directory = "TopEFT_PP_v12/trilep/"
    data_directory           = "/afs/hephy.at/data/rschoefbeck02/cmgTuples/"
    from TopEFT.samples.cmgTuples_ttZ0j_Summer16_mAODv2_postProcessed import *

    source_reco = ttZ0j_ll
    target_reco = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700

    # cutInterpreter & selectionString
    from TopEFT.Tools.cutInterpreter import cutInterpreter
    reco_selection = cutInterpreter.cutString( 'lepSelTTZ-njet3p-btag1p-onZ')
    source_reco.setSelectionString( reco_selection )
    target_reco.setSelectionString( reco_selection )

    # Histos
    pt_bins = [(0,100), (100,200), (200,-1), (-1,-1)]
    h_pt = {s:ROOT.TH1F('h_pt', 'h_pt', 10, 0, 500) for s in ['source', 'target', 'source_reweighted']} 

    h_pt['source']              .legendText = source_reco.texName
    h_pt['source']              .style = styles.lineStyle( ROOT.kBlue, errors = True) 
    h_pt['target']              .legendText = target_reco.texName
    h_pt['target']              .style = styles.lineStyle( ROOT.kGreen, errors = True) 
    h_pt['source_reweighted']   .legendText = source_reco.texName+'(reweighted)'
    h_pt['source_reweighted']   .style = styles.lineStyle( ROOT.kRed, errors = True) 

    h_cosThetaStar_pt = {s:{p:ROOT.TH1F('h_pt_%i_%i'%p, 'h_pt_%i_%i'%p, 10, -1,1) for p in pt_bins} for s in ['source', 'target', 'source_reweighted']} 
    for pt_bin in pt_bins:
        h_cosThetaStar_pt['source']           [pt_bin]  .legendText = source_reco.texName
        h_cosThetaStar_pt['source']           [pt_bin]  .style = styles.lineStyle( ROOT.kBlue, errors = True) 
        h_cosThetaStar_pt['target']           [pt_bin]  .legendText = target_reco.texName
        h_cosThetaStar_pt['target']           [pt_bin]  .style = styles.lineStyle( ROOT.kGreen, errors = True) 
        h_cosThetaStar_pt['source_reweighted'][pt_bin]  .legendText = source_reco.texName+'(reweighted)' 
        h_cosThetaStar_pt['source_reweighted'][pt_bin]  .style = styles.lineStyle( ROOT.kRed, errors = True) 

    # Loop
    variables = map( TreeVariable.fromString, ["Z_pt/F", "cosThetaStar/F", "weight/F"] )

    r_source = source_reco.treeReader( variables = variables )
    r_source.start()
    while r_source.run():
        pt           = r_source.event.Z_pt
        cosThetaStar = r_source.event.cosThetaStar
        if not pt<float('inf'):continue
        reweight     = f(pt, cosThetaStar)
        h_pt['source'].Fill( pt, r_source.event.weight )
        h_pt['source_reweighted'].Fill( pt, r_source.event.weight*reweight )
        
        for pt_bin in pt_bins:
            if (pt_bin[0]<0 or pt>pt_bin[0]) and (pt_bin[1]<0 or pt<pt_bin[1]):
                h_cosThetaStar_pt['source'][pt_bin].Fill(cosThetaStar, r_source.event.weight) 
                h_cosThetaStar_pt['source_reweighted'][pt_bin].Fill(cosThetaStar, r_source.event.weight*reweight) 

    r_target = target_reco.treeReader( variables = variables )
    r_target.start()
    while r_target.run():
        pt = r_target.event.Z_pt
        cosThetaStar = r_target.event.cosThetaStar
        h_pt['target'].Fill( pt, r_target.event.weight )
        for pt_bin in pt_bins:
            if (pt_bin[0]<0 or pt>pt_bin[0]) and (pt_bin[1]<0 or pt<pt_bin[1]):
                h_cosThetaStar_pt['target'][pt_bin].Fill(cosThetaStar, r_target.event.weight) 

    # Scale     
    h_pt['source_reweighted'].Scale( h_pt['target'].Integral()/h_pt['source_reweighted'].Integral())
    for pt_bin in pt_bins:
        h_cosThetaStar_pt['source_reweighted'][pt_bin].Scale( h_cosThetaStar_pt['target'][pt_bin].Integral()/h_cosThetaStar_pt['source_reweighted'][pt_bin].Integral())

    # Plot
    histos = [ [h_pt['source']], [h_pt['target']], [h_pt['source_reweighted']] ]
    plot = Plot.fromHisto( "pt", texX = 'p_{T}(Z) (reco)' , histos = histos)
    plotting.draw( plot, plot_directory = os.path.join( plot_directory, 'reweightingPlots' ), logY = False, copyIndexPHP = True) 
    for pt_bin in pt_bins:
        histos = [ [h_cosThetaStar_pt['source'][pt_bin]], [h_cosThetaStar_pt['target'][pt_bin]], [h_cosThetaStar_pt['source_reweighted'][pt_bin]] ]
        plot = Plot.fromHisto( "cosThetaStar_pt_%i_%i"%pt_bin, texX = 'cos(#theta^{*}) (reco)' , histos = histos)
        plotting.draw( plot, plot_directory = os.path.join( plot_directory, 'reweightingPlots' ), logY = False) 
