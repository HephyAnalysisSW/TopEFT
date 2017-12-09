''' Polarisation fit
'''
# standard imports
import os
import ROOT

# Stuff for testing
if __name__=='__main__':
    # Samples
    postProcessing_directory = "TopEFT_PP_v14/trilep/"
    data_directory           = "/afs/hephy.at/data/rschoefbeck01/cmgTuples/"
    # Logging
    import TopEFT.Tools.logger as logger
    logger = logger.get_logger('DEBUG', logFile = None )
else:
    # Logging
    import logging
    logger = logging.getLogger(__name__)

# RootTools
from RootTools.core.standard import *

# TopEFT
from TopEFT.Analysis.Setup  import Setup
from TopEFT.Analysis.Region import Region
from TopEFT.Tools.u_float   import u_float
from TopEFT.Tools.helpers   import sum_histos
from TopEFT.Tools.user      import results_directory, plot_directory
from TopEFT.samples.color import color
from TopEFT.Analysis.SystematicEstimator import SystematicEstimator
from TopEFT.Analysis.PolarisationTemplateMaker import PolarisationTemplateMaker
from TopEFT.Tools.ZPolarisation.ZPolarisationFit import ZPolarisationFit
from TopEFT.Analysis.SetupHelpers import channels, allChannels


class PolarisationEstimate(SystematicEstimator):

    def __init__(self, name, usePseudoData = False): #, cacheDir=None): # never cache
        super(PolarisationEstimate, self).__init__(name, cacheDir=None) # never cache
        self.usePseudoData = usePseudoData

    def _estimate(self, region, channel, setup):

        ''' Concrete implementation of abstract method 'estimate' as defined in Systematic
        '''

        logger.debug( "Obtain polarisation Estimate for channel %s region %s", channel, region )

        # Obtain fit template from an unbias Z sample. FIXME: Should be eta and pt reweighted
        #def_setup = setup.defaultClone() # Don't use systematic variations for templates
        sub_templates = []
        # Here, I assume the sample(!) is the same for all flavors
        template_maker = PolarisationTemplateMaker( setup.samples['TTZ']['3mu'], cacheDir = os.path.join( results_directory, 'PolarisationTemplateCache' ) )
        region_cut = region.cutString().replace('Z_pt','genZ_pt') # Make the template cut on genZ. Approximation. Don't uses sys. variations
        cuts = [region_cut]
        # If we know which Z flavor, then require it for the template
        if channel in ['3e', '2e1mu']:
            cuts.append( "genZ_daughter_flavor==11" )
        elif channel in  ['3mu', '2mu1e']:
            cuts.append( "genZ_daughter_flavor==13" )
        cut = "&&".join( cuts )

        logger.debug( "Making sub_template '%s' for polarisation fit using selection '%s' and weight '%s'", channel, cut, 'weight')
        templates = template_maker.cachedTemplate(cut, 'weight')

        # Obtain selection strings & weight from setup

        background_mc = {}
        background_mc_keys = []
        ttz_mc        = []
        data          = []
        for ch in ( [channel] if channel!='all' else channels):
            # Background MC
            for sample_name, sample in setup.samples.iteritems():
                if sample_name == 'Data':
                    pre_selection = setup.preselection('Data', channel=ch)
                    cut     = "&&".join( [ region.cutString(), pre_selection['cut'] ] )
                    weight  = pre_selection['weightStr']
                else:
                    pre_selection = setup.preselection('MC', channel=ch)
                    cut     = "&&".join( [ region.cutString(setup.sys['selectionModifier']), pre_selection['cut'] ] )
                    weight  = pre_selection['weightStr']
                    if sample_name not in background_mc_keys: background_mc_keys.append( sample_name )

                logger.info( "Get cosThetaStar histogram for sample %s channel %s cut %s weight %s" %( sample[ch].name, ch, cut, weight) )
                h = sample[ch].get1DHistoFromDraw( 'cosThetaStar', [20, -1, 1 ], selectionString = cut, weightString = weight )

                # Append & Scale
                if sample_name == 'Data':
                    data.append( h )
                elif sample_name == 'TTZ':
                    h.Scale( setup.lumi[ch]/1000. )
                    ttz_mc.append( h )
                else:
                    h.Scale( setup.lumi[ch]/1000. )
                    if background_mc.has_key(sample_name):
                        background_mc[sample_name].append(h)
                    else:
                        background_mc[sample_name] = [h]

        h_background_mc = []
        for sample_name in background_mc_keys:
            if sample_name=='TTZ': continue
            h_background_mc.append( sum_histos(background_mc[sample_name]) )
            h_background_mc[-1].style = styles.fillStyle( getattr(color, sample_name))
            h_background_mc[-1].legendText = sample_name

        h_ttz_mc        = sum_histos( ttz_mc )
        h_ttz_mc.style = styles.fillStyle( color.TTZtoLLNuNu  )
        h_ttz_mc.legendText = 'TTZ'

        h_data          = sum_histos(data)
        h_data.style = styles.errorStyle( ROOT.kBlack  )
        h_data.legendText = 'Data (%s)' % channel

        # Subtract MC from Data
        if self.usePseudoData:
            h_data_subtracted = h_ttz_mc.Clone()
            h_data_subtracted.Sumw2(0)
        else:
            scale = h_data.Integral() / (sum( [h.Integral() for h in h_background_mc ]) + h_ttz_mc.Integral())

            for h in h_background_mc:
                h.Scale( 1./scale )
            h_ttz_mc.Scale( 1./scale )

            h_data_subtracted = sum_histos( h_background_mc )
            h_data_subtracted.Scale(-1)
            h_data_subtracted.Add( h_data )

        h_data.style = styles.errorStyle( ROOT.kBlack  )
        h_data.legendText = 'Data (%s)' % channel
        h_data_subtracted.style = styles.errorStyle( ROOT.kBlack  )
        h_data_subtracted.legendText = 'Data (%s) subtr %3.1f' % ( channel, h_data_subtracted.Integral() )

        # Perform Fit

        y_p, y_m, y_L = map( u_float, ZPolarisationFit( h_data_subtracted, [templates[p] for p in ['p','m','L']], \
            fit_plot_directory = os.path.join( plot_directory,  'polFits'),  
            fit_filename       = "fit_pseudoData_%s_%s_%s"%( self.usePseudoData,  channel, region),
            sumW2Error = False # predict stat error
        ))

        templates['p'].Scale(y_p.val)
        templates['m'].Scale(y_m.val)
        templates['L'].Scale(y_L.val)
        templates['p'].style = styles.lineStyle( ROOT.kRed, width=2 )
        templates['m'].style = styles.lineStyle( ROOT.kGreen, width=2 )
        templates['L'].style = styles.lineStyle( ROOT.kMagenta, width=2 )

        h_fitresults = sum_histos( templates.values() )
        h_fitresults.style = styles.lineStyle( ROOT.kBlue, width = 2 )
        h_fitresults.legendText = "TTZ fit (sum)"

        histos = [ h_background_mc + [h_ttz_mc], [templates['p']], [templates['m']], [templates['L']], [h_fitresults], [h_data]]

        plot = Plot.fromHisto(name = "fit_plot_pseudoData_%s_%s_%s"%( self.usePseudoData,  channel, region), histos =  histos , texX = "cos#theta^{*}", texY = "Events" )  
        plotting.draw(plot, 
            plot_directory = os.path.join( plot_directory,  'polFits'), 
            logX = False, logY = False, sorting = False,
            legend      = ([0.15,0.7,0.90,0.90], 2)
            )

        templates['p'].legendText  = 'pol(+) %3.1f #pm %3.1f'%( y_p.val, y_p.sigma ) 
        templates['m'].legendText  = 'pol(-) %3.1f #pm %3.1f'%( y_m.val, y_m.sigma ) 
        templates['L'].legendText  = 'pol(L) %3.1f #pm %3.1f'%( y_L.val, y_L.sigma )

        histos = [ [h_ttz_mc], [templates['p']], [templates['m']], [templates['L']], [h_fitresults], [h_data_subtracted]]

        plot = Plot.fromHisto(name = "fit_plot_subtracted_pseudoData_%s_%s_%s"%( self.usePseudoData,  channel, region), histos =  histos , texX = "cos#theta^{*}", texY = "Events" )  
        plotting.draw(plot, 
            plot_directory = os.path.join( plot_directory,  'polFits'), 
            logX = False, logY = False, sorting = False,
            legend      = ([0.15,0.7,0.90,0.90], 2),
            yRange = (0, 30),
            )

if __name__=='__main__':

    setup = Setup()
    estimator_mc = PolarisationEstimate( "polarisation_data", usePseudoData = True)
    estimator_mc._estimate( Region("Z_pt", (0, -1)), 'all', setup )
    estimator_data = PolarisationEstimate( "polarisation_data" )
    estimator_data._estimate( Region("Z_pt", (0, -1)), 'all', setup )
