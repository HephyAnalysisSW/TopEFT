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


class SignalReweighting:

    def __init__( self, source_sample, target_sample, cacheDir = None):

        self.source_sample = source_sample
        self.target_sample = target_sample 
        self.initCache( cacheDir )
        #self.cache = Cache( os.path.join(cacheDir, 'signalReweightingTemplates.sql') )

        self.cosThetaStar_binning = [ i/5. for i in range(-5,6) ] 
        self.Z_pt_binning         = [ 0, 50, 100, 150, 200, 250, 300, 400, 500, 2000 ]
        self.template_draw_string = 'Z_pt:Z_cosThetaStar'

    def initCache(self, cacheDir):
        self.cache = resultsDB(os.path.join(cacheDir, 'signalReweightingTemplates_v2.sql'), "signalWeights", ["selection", "weight", "source", "target"])
        #if cacheDir:
        #    self.cacheDir = cacheDir
        #    try:    os.makedirs(cacheDir)
        #    except: pass
        #    cacheFileName = os.path.join(cacheDir, 'signalReweightingTemplates.pkl')
        #    self.cache    = PickleCache(cacheFileName)
        #else:
        #    self.cache=None

    def uniqueKey( self, *arg ):
        '''No dressing required'''
        return arg


    def cachedReweightingFunc( self, selection, weight = '(1)', save = True, overwrite = False):

        t = self.cachedTemplate( selection=selection, weight=weight, save=save, overwrite=overwrite)

        def reweight_func( pt, cosThetaStar):
            return t.GetBinContent( t.FindBin( cosThetaStar, pt ) )

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

        h_source = self.source_sample.get2DHistoFromDraw(self.template_draw_string , ( self.cosThetaStar_binning, self.Z_pt_binning), selectionString = selection, weightString = weight, binningIsExplicit = True )
        logger.info( "Source histogram contains %s weighted events", h_source.Integral() )
        if h_source.Integral()>0:
            h_source.Scale(1./h_source.Integral())
        else:
            return False
            raise ValueError
        h_target = self.target_sample.get2DHistoFromDraw(self.template_draw_string , ( self.cosThetaStar_binning, self.Z_pt_binning), selectionString = selection, weightString = weight, binningIsExplicit = True )
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

    # Benchmarks for testing
    from TopEFT.samples.gen_fwlite_benchmarks import *
    from TopEFT.Tools.user import results_directory, plot_directory

    # reweighting class
    cacheDir = os.path.join( results_directory, 'SignalReweightingTemplate' )
    
    source_gen = ewkDM_ttZ_ll_gen
    target_gen = ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700
    #target_gen = ewkDM_ttZ_ll_gen_DC2A_0p200000_DC2V_0p200000
    #target_gen = ewkDM_ttZ_ll_gen_DC1A_0p500000_DC1V_0p500000
    #target_gen = ewkDM_ttZ_ll_gen_DC1A_1p000000
    #target_gen = ewkDM_ttZ_ll_gen_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000
    
    #source_gen = dim6top_all[0]
    #target_gen = dim6top_dipoles[313]
    #target_gen = dim6top_LO_ttZ_ll_ctZ_0p00_ctZI_0p00

    signalReweighting = SignalReweighting( source_sample = source_gen, target_sample = target_gen, cacheDir = cacheDir)

    # reweighting selection
    selection = "Sum$(GenJet_pt>30)>=3&& abs(Z_mass-91.2)<10&&(abs(Z_daughterPdg)==11 || abs(Z_daughterPdg)==13 || abs(Z_daughterPdg)==15 )"#&&Sum$(GenLep_pt>40&&{l_match})>=1&&Sum$(GenLep_pt>20&&{l_match})>=2&&Sum$(GenLep_pt>10&&{l_match})>=3".format(l_match="(abs(GenLep_motherPdgId)==23||abs(GenLep_motherPdgId)==24)")
    #selection = "Sum$(GenJet_pt>30)>=3&& abs(Z_mass-91.2)<10 && (abs(Z_daughterPdg)==11 || abs(Z_daughterPdg)==13 || abs(Z_daughterPdg)==15 ) && Sum$(GenLep_pt>40&&{l_match})>=1&&Sum$(GenLep_pt>20&&{l_match})>=2&&Sum$(GenLep_pt>10&&{l_match})==3".format(l_match="((abs(GenLep_motherPdgId)==23||abs(GenLep_motherPdgId)==24||abs(GenLep_motherPdgId)==15)&&(abs(GenLep_pdgId)==11||abs(GenLep_pdgId)==13)&&abs(GenLep_eta)<2.4)")

    
    # reweighting function
    f = signalReweighting.cachedReweightingFunc( selection )
    
    matrix = signalReweighting.cachedTemplate( selection )
    
    #ROOT.gStyle.SetPaintTextFormat("2.2f") 
    
    matrixPlot = Plot2D.fromHisto( target_gen.name, texY = "p_{T}(Z) [GeV]", texX = "cos(#Theta*)", histos = [[matrix]])
    matrixPlot.drawOption = "colz text"
    def optimizeLogZ(histo):
            histo.GetZaxis().SetMoreLogLabels()
            histo.GetZaxis().SetNoExponent()
            histo.Draw("colz")
            histo.GetYaxis().SetRangeUser(10,1000)
            #histo.GetYaxis().SetMinimum(10)
    
    def setTextPrecision(can):
            ROOT.gStyle.SetPaintTextFormat("2.2f")

    plotting.draw2D( matrixPlot, plot_directory = os.path.join( plot_directory, 'reweightingMatrices', source_gen.name), logY = True, canvasModifications = [setTextPrecision],  histModifications = [optimizeLogZ], copyIndexPHP = True, zRange = [0.5, 5.])
    
    # A real world test
    
    if args.makePlots:
    
        # reco signals
        postProcessing_directory = "TopEFT_PP_2016_mva_v21/trilep/"
        data_directory           = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
        from TopEFT.samples.cmgTuples_ttZ0j_Summer16_mAODv2_postProcessed import *

        source_reco = ttZ0j_ll
        target_reco = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700
        #target_reco = ttZ0j_ll_DC2A_0p200000_DC2V_0p200000
        #target_reco = ttZ0j_ll_DC1A_0p500000_DC1V_0p500000
        #target_reco = ttZ0j_ll_DC1A_1p000000
        #target_reco = ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000

        # cutInterpreter & selectionString
        from TopEFT.Tools.cutInterpreter import cutInterpreter
        reco_selection = cutInterpreter.cutString( 'lepSelTTZ-njet3p-btag1p-onZ')
        logger.debug("Setting selectionString %s for reco samples", reco_selection)
        source_reco.setSelectionString( reco_selection )
        target_reco.setSelectionString( reco_selection )

        # Histos
        pt_bins = [(0,100), (100,200), (200,-1), (-1,-1)]
        h_pt = {s:ROOT.TH1F('h_pt', 'h_pt', 10, 0, 500) for s in ['source', 'target', 'source_reweighted']}

        h_pt['source']              .legendText = "SM (reco)"
        h_pt['source']              .style = styles.lineStyle( ROOT.kBlue, errors = True, width=2) 
        h_pt['target']              .legendText = "BSM (reco)"
        h_pt['target']              .style = styles.lineStyle( ROOT.kGreen-1, errors = True, width=2) 
        h_pt['source_reweighted']   .legendText = "SM (reco, reweighted)"
        h_pt['source_reweighted']   .style = styles.lineStyle( ROOT.kRed, errors = True, width=2) 

        h_g_pt = {s:ROOT.TH1F('h_g_pt', 'h_g_pt', 10, 0, 500) for s in ['source', 'target', 'source_reweighted']}
        h_g_pt['source']              .legendText = "SM (gen)"
        h_g_pt['source']              .style = styles.lineStyle( ROOT.kBlue, errors = False, width=2)
        h_g_pt['target']              .legendText = "BSM (gen)"
        h_g_pt['target']              .style = styles.lineStyle( ROOT.kGreen+1, errors = False, width=2)
        h_g_pt['source_reweighted']   .legendText = "SM (gen, reweighted)"
        h_g_pt['source_reweighted']   .style = styles.lineStyle( ROOT.kRed, errors = False, width=2)


        h_cosThetaStar_pt = {s:{p:ROOT.TH1F('h_pt_%i_%i'%p, 'h_pt_%i_%i'%p, 10, -1,1) for p in pt_bins} for s in ['source', 'target', 'source_reweighted']} 
        for pt_bin in pt_bins:
            h_cosThetaStar_pt['source']           [pt_bin]  .legendText = "SM (reco)"
            h_cosThetaStar_pt['source']           [pt_bin]  .style = styles.lineStyle( ROOT.kBlue, errors = True, width=2) 
            h_cosThetaStar_pt['target']           [pt_bin]  .legendText = "BSM (reco)"
            h_cosThetaStar_pt['target']           [pt_bin]  .style = styles.lineStyle( ROOT.kGreen, errors = True, width=2) 
            h_cosThetaStar_pt['source_reweighted'][pt_bin]  .legendText = "SM (reco, reweighted)"
            h_cosThetaStar_pt['source_reweighted'][pt_bin]  .style = styles.lineStyle( ROOT.kRed, errors = True, width=2) 

        h_g_cosThetaStar_pt = {s:{p:ROOT.TH1F('h_g_pt_%i_%i'%p, 'h_pt_%i_%i'%p, 10, -1,1) for p in pt_bins} for s in ['source', 'target', 'source_reweighted']}
        for pt_bin in pt_bins:
            h_g_cosThetaStar_pt['source']           [pt_bin]  .legendText = "SM (gen)"
            h_g_cosThetaStar_pt['source']           [pt_bin]  .style = styles.lineStyle( ROOT.kOrange, errors = False, width=2)
            h_g_cosThetaStar_pt['target']           [pt_bin]  .legendText = "BSM (gen)"
            h_g_cosThetaStar_pt['target']           [pt_bin]  .style = styles.lineStyle( ROOT.kCyan+1, errors = False, width=2)
            h_g_cosThetaStar_pt['source_reweighted'][pt_bin]  .legendText = "SM (gen, reweighted)"
            h_g_cosThetaStar_pt['source_reweighted'][pt_bin]  .style = styles.lineStyle( ROOT.kRed, errors = False, width=2)



        # Loop
        g_variables = map( TreeVariable.fromString, ["Z_pt/F", "Z_cosThetaStar/F"] )

        variables = map( TreeVariable.fromString, ["Z_pt/F", "cosThetaStar/F", "weight/F", "met_pt/F", "Z_mass/F", "nJetSelected/I", "nBTag/I", 'Z_l1_index/I', 'Z_l2_index/I', 'nonZ_l1_index/I', 'nonZ_l2_index/I' ] )
        variables += [VectorTreeVariable.fromString('lep[pt/F,eta/F,phi/F]')]

        h = {}
        h["met_pt"]         = {s:ROOT.TH1F('h_met_pt', 'h_met_pt', 10, 0, 500) for s in ['source', 'target', 'source_reweighted']}
        h["Z_mass"]         = {s:ROOT.TH1F('h_Z_mass', 'h_Z_mass', 20, 70, 110) for s in ['source', 'target', 'source_reweighted']}
        h["nJetSelected"]   = {s:ROOT.TH1F('h_njet', 'h_njet', 7, 3, 10) for s in ['source', 'target', 'source_reweighted']}
        h["nBTag"]          = {s:ROOT.TH1F('h_nbtag', 'h_nbtag', 5, 0, 5) for s in ['source', 'target', 'source_reweighted']}

        h["lep_pt1"]        = {s:ROOT.TH1F('h_lep_pt1', 'h_lep_pt1', 15, 0, 450) for s in ['source', 'target', 'source_reweighted']}
        h["lep_pt2"]        = {s:ROOT.TH1F('h_lep_pt2', 'h_lep_pt2', 15, 0, 300) for s in ['source', 'target', 'source_reweighted']}
        h["lep_pt3"]        = {s:ROOT.TH1F('h_lep_pt3', 'h_lep_pt3', 15, 0, 150) for s in ['source', 'target', 'source_reweighted']}

        h["Z_lep_pt1"]        = {s:ROOT.TH1F('h_Z_lep_pt1', 'h_Z_lep_pt1', 15, 0, 450) for s in ['source', 'target', 'source_reweighted']}
        h["Z_lep_pt2"]        = {s:ROOT.TH1F('h_Z_lep_pt2', 'h_Z_lep_pt2', 15, 0, 300) for s in ['source', 'target', 'source_reweighted']}
        h["nonZ_lep_pt"]      = {s:ROOT.TH1F('h_nonZ_lep', 'h_nonZ_lep_pt', 15, 0, 150) for s in ['source', 'target', 'source_reweighted']}


        h["met_pt"]["texX"]         = "E_{T}^{miss} (GeV)"
        h["Z_mass"]["texX"]         = "M(ll) (GeV)"
        h["nJetSelected"]["texX"]   = "N_{jet}"
        h["nBTag"]["texX"]          = "N_{b-jet}"
        
        h["lep_pt1"]["texX"]        = "p_{T} (leading l) (GeV)"
        h["lep_pt2"]["texX"]        = "p_{T} (sub-leading l) (GeV)"
        h["lep_pt3"]["texX"]        = "p_{T} (trailing l) (GeV)"

        h["Z_lep_pt1"]["texX"]        = "p_{T} (leading l from Z) (GeV)"
        h["Z_lep_pt2"]["texX"]        = "p_{T} (sub-leading l from Z) (GeV)"
        h["nonZ_lep_pt"]["texX"]      = "p_{T} (l from W) (GeV)"

        plotVars = ["met_pt", "Z_mass", "nJetSelected", "nBTag", "lep_pt1", "lep_pt2", "lep_pt3", "Z_lep_pt1", "Z_lep_pt2", "nonZ_lep_pt"]

        for var in plotVars:
            h[var]['source']              .legendText = "SM (reco)"
            h[var]['source']              .style = styles.lineStyle( ROOT.kBlue, errors = True, width=2)
            h[var]['target']              .legendText = "BSM (reco)"
            h[var]['target']              .style = styles.lineStyle( ROOT.kGreen, errors = True, width=2)
            h[var]['source_reweighted']   .legendText = "SM (reco, reweighted)"
            h[var]['source_reweighted']   .style = styles.lineStyle( ROOT.kRed, errors = True, width=2)



        source_gen.setSelectionString( selection )
        target_gen.setSelectionString( selection )
        g_source = source_gen.treeReader( variables = g_variables )
        
        g_source.start()
        while g_source.run():
            pt           = g_source.event.Z_pt
            cosThetaStar = g_source.event.Z_cosThetaStar
            if not pt<float('inf'):continue
            reweight     = f(pt, cosThetaStar)
            h_g_pt['source'].Fill( pt )
            h_g_pt['source_reweighted'].Fill( pt, reweight )
            for pt_bin in pt_bins:
                if (pt_bin[0]<0 or pt>pt_bin[0]) and (pt_bin[1]<0 or pt<pt_bin[1]):
                    h_g_cosThetaStar_pt['source'][pt_bin].Fill(cosThetaStar)
                    h_g_cosThetaStar_pt['source_reweighted'][pt_bin].Fill(cosThetaStar, reweight)

        g_target = target_gen.treeReader( variables = g_variables )
        g_target.start()
        while g_target.run():
            pt = g_target.event.Z_pt
            if not pt<float('inf'):continue
            cosThetaStar = g_target.event.Z_cosThetaStar
            h_g_pt['target'].Fill( pt )
            for pt_bin in pt_bins:
                if (pt_bin[0]<0 or pt>pt_bin[0]) and (pt_bin[1]<0 or pt<pt_bin[1]):
                    h_g_cosThetaStar_pt['target'][pt_bin].Fill(cosThetaStar)

        r_source = source_reco.treeReader( variables = variables )
        r_source.start()
        while r_source.run():
            leps = [ x for x in r_source.event.lep_pt ]
            r_source.event.lep_pt1 = leps[0]
            r_source.event.lep_pt2 = leps[1]
            r_source.event.lep_pt3 = leps[2]
            r_source.event.Z_lep_pt1 = leps[r_source.event.Z_l1_index]
            r_source.event.Z_lep_pt2 = leps[r_source.event.Z_l2_index]
            r_source.event.nonZ_lep_pt = leps[r_source.event.nonZ_l1_index]

            for var in plotVars:
                h[var]["value"] = getattr(r_source.event, var)
            pt           = r_source.event.Z_pt
            cosThetaStar = r_source.event.cosThetaStar
            if not pt<float('inf'):continue
            reweight     = f(pt, cosThetaStar)
            h_pt['source'].Fill( pt, r_source.event.weight )
            h_pt['source_reweighted'].Fill( pt, r_source.event.weight*reweight )
            
            for var in plotVars:
                h[var]['source'].Fill(h[var]["value"], r_source.event.weight )
                h[var]['source_reweighted'].Fill(h[var]["value"], r_source.event.weight*reweight )

            
            for pt_bin in pt_bins:
                if (pt_bin[0]<0 or pt>pt_bin[0]) and (pt_bin[1]<0 or pt<pt_bin[1]):
                    h_cosThetaStar_pt['source'][pt_bin].Fill(cosThetaStar, r_source.event.weight) 
                    h_cosThetaStar_pt['source_reweighted'][pt_bin].Fill(cosThetaStar, r_source.event.weight*reweight) 

        r_target = target_reco.treeReader( variables = variables )
        r_target.start()
        while r_target.run():
            leps = [ x for x in r_target.event.lep_pt ]
            r_target.event.lep_pt1 = leps[0]
            r_target.event.lep_pt2 = leps[1]
            r_target.event.lep_pt3 = leps[2]
            r_target.event.Z_lep_pt1    = leps[r_target.event.Z_l1_index]
            r_target.event.Z_lep_pt2    = leps[r_target.event.Z_l2_index]
            r_target.event.nonZ_lep_pt  = leps[r_target.event.nonZ_l1_index]

            for var in plotVars:
                h[var]["value"] = getattr(r_target.event, var)
            pt = r_target.event.Z_pt
            cosThetaStar = r_target.event.cosThetaStar
            h_pt['target'].Fill( pt, r_target.event.weight )

            for var in plotVars:
                h[var]['target'].Fill(h[var]["value"], r_source.event.weight )

            for pt_bin in pt_bins:
                if (pt_bin[0]<0 or pt>pt_bin[0]) and (pt_bin[1]<0 or pt<pt_bin[1]):
                    h_cosThetaStar_pt['target'][pt_bin].Fill(cosThetaStar, r_target.event.weight) 

        # Scale     
        h_pt['source_reweighted'].Scale( h_pt['target'].Integral()/h_pt['source_reweighted'].Integral())
        h_g_pt['source_reweighted'].Scale( h_g_pt['target'].Integral()/h_g_pt['source_reweighted'].Integral())
        for pt_bin in pt_bins:
            h_cosThetaStar_pt['source_reweighted'][pt_bin].Scale( h_cosThetaStar_pt['target'][pt_bin].Integral()/h_cosThetaStar_pt['source_reweighted'][pt_bin].Integral())

        # Plot
        def drawObjects( plotData, dataMCScale, lumi_scale ):
            tex = ROOT.TLatex()
            tex.SetNDC()
            tex.SetTextSize(0.04)
            tex.SetTextAlign(11) # align right
            lines = [
              (0.15, 0.95, 'CMS Preliminary' if plotData else 'CMS Simulation'), 
              (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV) Scale %3.2f'% ( lumi_scale, dataMCScale ) ) if plotData else (0.45, 0.95, 'L=%3.1f fb{}^{-1} (13 TeV)' % lumi_scale)
            ]
            return [tex.DrawLatex(*l) for l in lines] 
        
        scaling = {1:0, 2:0}
        ghistos = [ [h_g_pt['source']], [h_g_pt['target']], [h_g_pt['source_reweighted']] ]
        gplot = Plot.fromHisto( "pt_gen", texX = 'p_{T}(Z) (gen)' , texY = 'a.u.', histos = ghistos)
        plotting.draw( gplot, plot_directory = os.path.join( plot_directory, 'reweightingPlots_closure', target_reco.name ), logY = False, copyIndexPHP = True, scaling = scaling)

        histos = [ [h_pt['source']], [h_pt['target']], [h_pt['source_reweighted']] ]
        plot = Plot.fromHisto( "pt", texX = 'p_{T}(Z) (reco)', texY = 'a.u.', histos = histos)
        plotting.draw( plot, plot_directory = os.path.join( plot_directory, 'reweightingPlots_closure', target_reco.name ), logY = False, copyIndexPHP = True, scaling = scaling, drawObjects = drawObjects( False, 1, 1 )) 

        for var in plotVars:
            h[var]['source_reweighted'].Scale( h[var]['target'].Integral()/h[var]['source_reweighted'].Integral())
            histos = [ [h[var]['source']], [h[var]['target']], [h[var]['source_reweighted']] ]
            plot = Plot.fromHisto( var, texX = h[var]['texX'], texY = 'a.u.', histos = histos)
            plotting.draw( plot, plot_directory = os.path.join( plot_directory, 'reweightingPlots_closure', target_reco.name ), logY = True, yRange = (0.008,8.), copyIndexPHP = True, scaling = scaling, drawObjects = drawObjects( False, 1, 1 ))


        for pt_bin in pt_bins:
            histos = [ [h_cosThetaStar_pt['source'][pt_bin]], [h_cosThetaStar_pt['target'][pt_bin]], [h_cosThetaStar_pt['source_reweighted'][pt_bin]] ]
            plot = Plot.fromHisto( "cosThetaStar_pt_%i_%i"%pt_bin, texX = 'cos(#theta^{*}) (reco)', texY = 'a.u.', histos = histos)
            plotting.draw( plot, plot_directory = os.path.join( plot_directory, 'reweightingPlots_closure', target_reco.name ), logY = False, scaling = scaling, drawObjects = drawObjects( False, 1, 1 )) 

        for pt_bin in pt_bins:
            histos = [ [h_g_cosThetaStar_pt['source'][pt_bin]], [h_g_cosThetaStar_pt['target'][pt_bin]], [h_g_cosThetaStar_pt['source_reweighted'][pt_bin]] ]
            plot = Plot.fromHisto( "cosThetaStar_pt_%i_%i_gen"%pt_bin, texX = 'cos(#theta^{*}) (gen)', texY = 'a.u.', histos = histos)
            plotting.draw( plot, plot_directory = os.path.join( plot_directory, 'reweightingPlots_closure', target_reco.name ), logY = False, scaling = scaling, drawObjects = drawObjects( False, 1, 1 ))

        scaling = {1:0}
        for pt_bin in pt_bins:
            histos = [ [h_g_cosThetaStar_pt['target'][pt_bin]], [h_cosThetaStar_pt['target'][pt_bin]] ]
            plot = Plot.fromHisto( "cosThetaStar_pt_%i_%i_target"%pt_bin, texX = 'cos(#theta^{*}) (target)', texY = 'a.u.', histos = histos)
            plotting.draw( plot, plot_directory = os.path.join( plot_directory, 'reweightingPlots_closure', target_reco.name ), logY = False, scaling = scaling, drawObjects = drawObjects( False, 1, 1 ))
        
        for pt_bin in pt_bins:
            histos = [ [h_g_cosThetaStar_pt['source'][pt_bin]], [h_cosThetaStar_pt['source'][pt_bin]] ]
            plot = Plot.fromHisto( "cosThetaStar_pt_%i_%i_source"%pt_bin, texX = 'cos(#theta^{*}) (source)', texY = 'a.u.', histos = histos)
            plotting.draw( plot, plot_directory = os.path.join( plot_directory, 'reweightingPlots_closure', target_reco.name ), logY = False, scaling = scaling, drawObjects = drawObjects( False, 1, 1 ))

        for pt_bin in pt_bins:
            h_g_cosThetaStar_pt['target'][pt_bin].Divide(h_g_cosThetaStar_pt['source'][pt_bin])
            h_cosThetaStar_pt['target'][pt_bin].Divide(h_cosThetaStar_pt['source'][pt_bin])
            histos = [ [h_g_cosThetaStar_pt['target'][pt_bin]], [h_cosThetaStar_pt['target'][pt_bin]] ]
            plot = Plot.fromHisto( "cosThetaStar_pt_%i_%i_ratio"%pt_bin, texX = 'cos(#theta^{*}) (ratio)', texY = 'a.u.', histos = histos)
            plotting.draw( plot, plot_directory = os.path.join( plot_directory, 'reweightingPlots_closure', target_reco.name ), logY = False, scaling = scaling, drawObjects = drawObjects( False, 1, 1 ))

    
