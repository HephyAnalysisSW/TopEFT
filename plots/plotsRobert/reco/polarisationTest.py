from RootTools.core.standard import *
from TopEFT.tools.ZPolarisationFit import ZPolarisationFit
from TopEFT.tools.cutInterpreter import cutInterpreter

s  = Sample.fromDirectory( 'TTZ_LO', directory = ['/afs/hephy.at/data/rschoefbeck02/cmgTuples/TopEFT_PP_v12/inclusive/TTZ_LO'] )
s2 = Sample.fromDirectory( 'ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700', directory = ['/afs/hephy.at/data/rschoefbeck02/cmgTuples/TopEFT_PP_v12/inclusive/ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700'])

sample = s2
h = sample.get1DHistoFromDraw( 'genZ_cosThetaStar', [20, -1, 1 ], selectionString = cutInterpreter.cutString('njet3p-btag1p')+'&&genZ_pt>200', weightString = 'weight*35.9' )

ZPolarisationFit( h, isData = False, 
    var_name        = 'cosThetaStar', 
    fit_plot_directory  = '/afs/hephy.at/user/r/rschoefbeck/www/TopEFT/polFits', 
    fit_filename    = sample.name)
