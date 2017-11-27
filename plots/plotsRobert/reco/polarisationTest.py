#Standard imports

import os
import pickle

# RootTools
from RootTools.core.standard import *

# TopEFT
from TopEFT.tools.ZPolarisation.ZPolarisationFit import ZPolarisationFit
from TopEFT.tools.cutInterpreter import cutInterpreter
from TopEFT.tools.user import results_directory

s     = Sample.fromDirectory( 'TTZ_LO', directory = ['/afs/hephy.at/data/rschoefbeck02/cmgTuples/TopEFT_PP_v12/inclusive/TTZ_LO'] )
s_BSM = Sample.fromDirectory( 'ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700', directory = ['/afs/hephy.at/data/rschoefbeck02/cmgTuples/TopEFT_PP_v12/inclusive/ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700'])

h_TTZ_LO = s.get1DHistoFromDraw( 'genZ_cosThetaStar', [20, -1, 1 ], 
        selectionString = cutInterpreter.cutString('njet3p-btag1p')+'&&genZ_pt>200', 
        #selectionString = cutInterpreter.cutString('lepSelTTZ-njet3p-btag1p-onZ')+'&&genZ_pt>0', 
        weightString = 'weight*100' )

h_BSM = s_BSM.get1DHistoFromDraw( 'genZ_cosThetaStar', [20, -1, 1 ], 
        selectionString = cutInterpreter.cutString('njet3p-btag1p')+'&&genZ_pt>200', 
        #selectionString = cutInterpreter.cutString('lepSelTTZ-njet3p-btag1p-onZ')+'&&genZ_pt>0', 
        weightString = 'weight*100' )

h_BSM.Scale( h_TTZ_LO.Integral()/h_BSM.Integral() )

ZPolarisationFit( h_TTZ_LO,
    fit_plot_directory  = '/afs/hephy.at/user/r/rschoefbeck/www/TopEFT/polFits', 
    fit_filename    = 'gen_'+s.name,
    sumW2Error = False, 
    #sumW2Error = True, 
    )

ZPolarisationFit( h_BSM,
    fit_plot_directory  = '/afs/hephy.at/user/r/rschoefbeck/www/TopEFT/polFits', 
    fit_filename    = 'gen_'+s_BSM.name,
    sumW2Error = False, 
    #sumW2Error = True, 
    )

templates = pickle.load(file( os.path.join( results_directory, 'ZPolarisationTemplates/templates.pkl' ) ))

pol_histos = [ templates[(100,200)][(0,-1)][p] for p in ['p','m','L']]

s     = Sample.fromDirectory( 'TTZ_LO', directory = ['/afs/hephy.at/data/rschoefbeck02/cmgTuples/TopEFT_PP_v12/inclusive/TTZ_LO'] )
s_BSM = Sample.fromDirectory( 'ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700', directory = ['/afs/hephy.at/data/rschoefbeck02/cmgTuples/TopEFT_PP_v12/inclusive/ttZ0j_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700'])

h_TTZ_LO = s.get1DHistoFromDraw( 'cosThetaStar', [20, -1, 1 ], 
        selectionString = cutInterpreter.cutString('lepSelTTZ-njet3p-btag1p-onZ')+'&&Z_pt>100&&Z_pt<200', 
        weightString = 'weight*100' )

h_BSM = s_BSM.get1DHistoFromDraw( 'cosThetaStar', [20, -1, 1 ], 
        selectionString = cutInterpreter.cutString('lepSelTTZ-njet3p-btag1p-onZ')+'&&Z_pt>100&&Z_pt<200', 
        weightString = 'weight*100' )

h_BSM.Scale( h_TTZ_LO.Integral()/h_BSM.Integral() )

ZPolarisationFit( h_TTZ_LO,
    fit_plot_directory  = '/afs/hephy.at/user/r/rschoefbeck/www/TopEFT/polFits', 
    fit_filename    = s.name,
    pol_histos = pol_histos,
    sumW2Error = False, 
    #sumW2Error = True, 
    )

ZPolarisationFit( h_BSM,
    fit_plot_directory  = '/afs/hephy.at/user/r/rschoefbeck/www/TopEFT/polFits', 
    fit_filename    = s_BSM.name,
    pol_histos = pol_histos,
    sumW2Error = False, 
    #sumW2Error = True, 
    )
