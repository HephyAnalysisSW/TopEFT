# Standard imports
import ROOT
import os
import pickle

# RootTools & TopEFT
from TopEFT.Tools.PickleCache import PickleCache
from RootTools.core.standard import *
from TopEFT.Tools.cutInterpreter import cutInterpreter
from TopEFT.Tools.user import results_directory, plot_directory 

# Logger & Args
if __name__ == "__main__":
    #
    # Arguments
    # 
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser")
    argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
    args = argParser.parse_args()

    import TopEFT.Tools.logger as logger
    import RootTools.core.logger as logger_rt
    logger    = logger.get_logger(   args.logLevel, logFile = None)
    logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)
else:
    import logging
    logger = logging.getLogger(__name__)


class PolarisationTemplateMaker: 

    polarisations = ["p", "m", "L"]

    def __init__( self, sample, cacheDir = None):

        self.initCache( cacheDir )

        self.sample     = sample

        # make pure polarisation histograms
        #polarisation functions
        self.f_Z_pol = { 'p': ROOT.TF1("Z_pol_p_func", "1+x**2-0.437825*x"),
                         'm': ROOT.TF1("Z_mol_m_func", "1+x**2+0.437825*x"),
                         'L': ROOT.TF1("Z_mol_L_func", "1-x**2") }

    def initCache(self, cacheDir):
        if cacheDir:
            self.cacheDir = cacheDir
            try:    os.makedirs(cacheDir)
            except: pass
            cacheFileName = os.path.join(cacheDir, 'polarisationTemplates.pkl')
            self.cache    = PickleCache(cacheFileName)
        else:
            self.cache=None

    def uniqueKey( self, *arg ):
        '''No dressing required'''
        return arg

    def cachedTemplate( self, selection, weight = 'weight', save = True, overwrite = False):

        key =  self.uniqueKey( selection, weight, self.sample.name)
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

        h_gen = self.sample.get1DHistoFromDraw( 'genZ_cosThetaStar', [20, -1, 1 ], selectionString = selection, weightString = weight )
        if h_gen.Integral()>0:
            h_gen.Scale(1./h_gen.Integral())
        else:
            raise ValueError

        templates = { p : ROOT.TH1F('template_'+p, 'template_'+p, 20, -1, 1 ) for p in self.polarisations }

        r = self.sample.treeReader( \
                variables = map( TreeVariable.fromString, ['genZ_cosThetaStar/F', 'cosThetaStar/F', 'weight/F']),
                selectionString = selection )

        r.start()
        while r.run():
            for p in self.polarisations:

                if not r.event.genZ_cosThetaStar<float('inf'): continue
                w = r.event.weight*self.f_Z_pol[p].Eval(r.event.genZ_cosThetaStar)
                sw = h_gen.GetBinContent(h_gen.FindBin(r.event.genZ_cosThetaStar))
                if sw>0:
                    w/=sw
                else:
                    w=0
                if r.event.cosThetaStar<float('inf'):
                    templates[p].Fill( r.event.cosThetaStar, w )
                #print r.event.weight, f_Z_pol[p].Eval(r.event.genZ_cosThetaStar), h.GetBinContent(h.FindBin(r.event.genZ_cosThetaStar))

        self.sample.chain.SetBranchStatus( "*", 1 )

        # Normalisation
        for p in self.polarisations:
            h = templates[p]
            s = h.Integral()
            if s>0:
                h.Scale( 1./s )

        return templates

if __name__ == "__main__":

    # Sample
    s  = Sample.fromDirectory( 'TTZ_LO', directory = ['/afs/hephy.at/data/rschoefbeck02/cmgTuples/TopEFT_PP_v12/inclusive/TTZ_LO'] )

    t_maker = PolarisationTemplateMaker(s, cacheDir = os.path.join( results_directory, 'PolarisationTemplateCache' ) )

    # polarisation bin  -> will be argument
    genZ_pt_bin  = (0,25)
    genZ_eta_bin = (0, -1)
    # kinematic preselection
    cut_string = cutInterpreter.cutString('njet3p-btag1p')
    kin_cut_string = "genZ_pt>=%i" % genZ_pt_bin[0]
    if genZ_pt_bin[1]>0: kin_cut_string+="&&genZ_pt<%i"%( genZ_pt_bin[1] )
    kin_cut_string+= "&&genZ_eta>=%i" % genZ_eta_bin[0]
    if genZ_eta_bin[1]>0: kin_cut_string+="&&genZ_eta<%i"%( genZ_eta_bin[1] )
    selectionString = kin_cut_string+"&&"+cut_string

    templates = t_maker.cachedTemplate( selectionString, 'weight')

    templates['p'].legendText = '+' 
    templates['m'].legendText = '-' 
    templates['L'].legendText = 'L' 
    templates['p'].style = styles.lineStyle( ROOT.kRed )
    templates['m'].style = styles.lineStyle( ROOT.kGreen )
    templates['L'].style = styles.lineStyle( ROOT.kBlue )

    histos = [ [templates['p']], [templates['m']], [templates['L']] ]
    plot = Plot.fromHisto( "pt_%i_%i"%genZ_pt_bin + '_eta_%3.2f_%3.2f'%genZ_eta_bin, texX = 'cos#theta^{*} (reco)' , histos = histos)
    plotting.draw( plot, plot_directory = os.path.join( plot_directory, 'polPlots' ), logY = False) 
