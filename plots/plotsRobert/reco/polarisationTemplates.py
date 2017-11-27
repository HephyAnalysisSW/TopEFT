# Standard imports
import ROOT
import os
import pickle

# RootTools & TopEFT
from RootTools.core.standard import *
from TopEFT.tools.cutInterpreter import cutInterpreter
from TopEFT.tools.user import results_directory, plot_directory 

small = True
maxN = 1000 if small else -1

#
# Arguments
# 
import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--logLevel',           action='store',      default='INFO',          nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'TRACE', 'NOTSET'], help="Log level for logging")
argParser.add_argument('--overwrite',          action='store_true', help='overwrite?', )
args = argParser.parse_args()

# Logger
if __name__ == "__main__":
    import TopEFT.tools.logger as logger
    import RootTools.core.logger as logger_rt
    logger    = logger.get_logger(   args.logLevel, logFile = None)
    logger_rt = logger_rt.get_logger(args.logLevel, logFile = None)
else:
    import logging
    logger = logging.getLogger(__name__)

# polarisation bins
genZ_pt_bins  = [ (0, -1), (0, 100), (100, -1), (100, 200), (200, -1) ]
genZ_eta_bins = [ (0, -1), (0, 1.3), (1.3, -1) ]

# polarisation histos from sample
template_pkl = os.path.join( results_directory, 'ZPolarisationTemplates/templates.pkl' )
if not os.path.exists( template_pkl ) or args.overwrite:
    logger.info("pkl file %s not found. Making templates", template_pkl)

    # sample
    s  = Sample.fromDirectory( 'TTZ_LO', directory = ['/afs/hephy.at/data/rschoefbeck02/cmgTuples/TopEFT_PP_v12/inclusive/TTZ_LO'] )
    #s2 = Sample.fromDirectory( 'ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700', directory = ['/afs/hephy.at/data/rschoefbeck02/cmgTuples/TopEFT_PP_v12/inclusive/ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700'])
    sample = s

    # kinematic preselection
    cut_string = cutInterpreter.cutString('njet3p-btag1p')

    # make pure polarisation histograms
    polarisations = ["p", "m", "L"]
    #polarisation functions
    f_Z_pol = { 'p': ROOT.TF1("Z_pol_p_func", "1+x**2-0.437825*x"),
                'm': ROOT.TF1("Z_mol_m_func", "1+x**2+0.437825*x"),
                'L': ROOT.TF1("Z_mol_L_func", "1-x**2")
                }

    templates = {}
    sample_genZ_cosThetaStar = {}
    for i_genZ_pt_bin, genZ_pt_bin in enumerate(genZ_pt_bins):
        templates[genZ_pt_bin] = {}
        sample_genZ_cosThetaStar[genZ_pt_bin] = {}
        for i_genZ_eta_bin, genZ_eta_bin in enumerate(genZ_eta_bins):

            logger.info( "At pt %r and eta %r", genZ_pt_bin, genZ_eta_bin )
            
            kin_cut_string = "genZ_pt>=%i" % genZ_pt_bin[0]
            if genZ_pt_bin[1]>0: kin_cut_string+="&&genZ_pt<%i"%( genZ_pt_bin[1] )
            kin_cut_string+= "&&genZ_eta>=%i" % genZ_eta_bin[0]
            if genZ_eta_bin[1]>0: kin_cut_string+="&&genZ_eta<%i"%( genZ_eta_bin[1] )

            selectionString = kin_cut_string+"&&"+cut_string

            h_sample = sample.get1DHistoFromDraw( 'genZ_cosThetaStar', [20, -1, 1 ], selectionString = selectionString, weightString = 'weight*35.9' )
            h_sample.Scale(1./h_sample.Integral())
            sample_genZ_cosThetaStar[genZ_pt_bin][genZ_eta_bin] = h_sample

            #sample_cosThetaStar = sample.get1DHistoFromDraw( 'cosThetaStar', [20, -1, 1 ], selectionString = selectionString, weightString = 'weight*35.9' )
            #sample_cosThetaStar.Scale(1./sample_cosThetaStar.Integral()

            name = "h_Z_pol_%i_%i"%( i_genZ_pt_bin, i_genZ_eta_bin )
            templates[genZ_pt_bin][genZ_eta_bin] = { p : ROOT.TH1F(name+'_'+p, name+'_'+p, 20, -1, 1 ) for p in polarisations }

            r = sample.treeReader( \
                    variables = map( TreeVariable.fromString, ['genZ_cosThetaStar/F', 'cosThetaStar/F', 'weight/F']),
                    selectionString = selectionString )

            r.start()
            while r.run():
                for p in polarisations:

                    if not r.event.genZ_cosThetaStar<float('inf'): continue
                    w = r.event.weight*f_Z_pol[p].Eval(r.event.genZ_cosThetaStar)
                    h = sample_genZ_cosThetaStar[genZ_pt_bin][genZ_eta_bin]
                    sw = h.GetBinContent(h.FindBin(r.event.genZ_cosThetaStar))
                    if sw>0:
                        w/=sw
                    else:
                        w=0

                    templates[genZ_pt_bin][genZ_eta_bin][p].Fill( r.event.cosThetaStar, w )
                    #print r.event.weight, f_Z_pol[p].Eval(r.event.genZ_cosThetaStar), h.GetBinContent(h.FindBin(r.event.genZ_cosThetaStar))
            sample.chain.SetBranchStatus( "*", 1 )
    # Normalisation
    for i_genZ_pt_bin, genZ_pt_bin in enumerate(genZ_pt_bins):
        for i_genZ_eta_bin, genZ_eta_bin in enumerate(genZ_eta_bins):
            for p in polarisations:
                h = templates[genZ_pt_bin][genZ_eta_bin][p]
                s = h.Integral()
                if s>0:
                    h.Scale( 1./s )

    if not os.path.exists( os.path.dirname( template_pkl )):
        os.makedirs(os.path.dirname( template_pkl ))

    pickle.dump( templates, file( template_pkl, 'w') )
    logger.info( "Written %s", template_pkl )
else:
    logger.info("pkl file %s found. Loading templates.", template_pkl)
    templates = pickle.load( file( template_pkl ) )

if __name__ == "__main__":
    for i_genZ_pt_bin, genZ_pt_bin in enumerate(genZ_pt_bins):
        for i_genZ_eta_bin, genZ_eta_bin in enumerate(genZ_eta_bins):
            templates[genZ_pt_bin][genZ_eta_bin]['p'].legendText = '+' 
            templates[genZ_pt_bin][genZ_eta_bin]['m'].legendText = '-' 
            templates[genZ_pt_bin][genZ_eta_bin]['L'].legendText = 'L' 
            templates[genZ_pt_bin][genZ_eta_bin]['p'].style = styles.lineStyle( ROOT.kRed )
            templates[genZ_pt_bin][genZ_eta_bin]['m'].style = styles.lineStyle( ROOT.kGreen )
            templates[genZ_pt_bin][genZ_eta_bin]['L'].style = styles.lineStyle( ROOT.kBlue )

            histos = [ [templates[genZ_pt_bin][genZ_eta_bin]['p']], [templates[genZ_pt_bin][genZ_eta_bin]['m']], [templates[genZ_pt_bin][genZ_eta_bin]['L']] ]
            plot = Plot.fromHisto( "pt_%i_%i"%genZ_pt_bin + '_eta_%3.2f_%3.2f'%genZ_eta_bin, texX = 'cos#theta^{*} (reco)' , histos = histos)
            plotting.draw( plot, plot_directory = os.path.join( plot_directory, 'polPlots' ), logY = False) 
