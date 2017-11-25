from RootTools.core.standard import *
from TopEFT.tools.ZPolarisationFit import ZPolarisationFit

s = Sample.fromDirectory( 's', directory = ['/afs/hephy.at/data/rschoefbeck02/cmgTuples/TopEFT_PP_v12/inclusive/TTZ_LO'] )

h = s.get1DHistoFromDraw( 'genZ_cosThetaStar', [20, -1, 1 ], 'Z_pt<100&&abs(Z_eta)<1', weight )

ZPolarisationFit( h, isData = True, 
    var_name        = 'cosThetaStar', 
    fit_plot_directory  = '/afs/hephy.at/user/r/rschoefbeck/www/etc/', 
    fit_filename    = 'pol_fit')
