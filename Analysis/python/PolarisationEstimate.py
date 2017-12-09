''' Polarisation fit
'''
# standard imports
import os

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


# TopEFT
from TopEFT.Analysis.Setup  import Setup
from TopEFT.Analysis.Region import Region
from TopEFT.Tools.u_float   import u_float
from TopEFT.Tools.helpers   import sum_histos
from TopEFT.Tools.user      import results_directory, plot_directory
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
            cuts.append( "genZ_gen_flavor==11" )
        elif channel in  ['3mu', '2mu1e']:
            cuts.append( "genZ_gen_flavor==13" )
        cut = "&&".join( cuts )

        logger.debug( "Making sub_template '%s' for polarisation fit using selection '%s' and weight '%s'", channel, cut, 'weight')
        templates = template_maker.cachedTemplate(cut, 'weight')

        # Obtain selection strings & weight from setup

        background_mc = []
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

                logger.info( "Get cosThetaStar histogram for sample %s channel %s cut %s weight %s" %( sample[ch].name, ch, cut, weight) )
                h = sample[ch].get1DHistoFromDraw( 'cosThetaStar', [20, -1, 1 ], selectionString = cut, weightString = weight )

                # Append & Scale
                if sample_name == 'Data':
                    data.append( h )
                elif sample_name == 'TTZ':
                    ttz_mc.append( h )
                    ttz_mc[-1].Scale( setup.lumi[ch]/1000. )
                else:
                    background_mc.append( h )
                    background_mc[-1].Scale( setup.lumi[ch]/1000. )

        h_background_mc = sum_histos(background_mc)
        h_ttz_mc        = sum_histos(ttz_mc       )
        h_data          = sum_histos(data         )

        # Subtract MC from Data
        if self.usePseudoData:
            h_data_subtracted = h_ttz_mc
        else:
            h_ttz_mc.Scale(-1)
            h_data.Add( h_background_mc )        
            h_data_subtracted = h_data 
        # Perform Fit

        fit_result = ZPolarisationFit( h_data_subtracted, [templates[p] for p in ['p','m','L']], \
            fit_plot_directory = os.path.join( plot_directory,  'polFits'),  
            fit_filename       = "fit_pseudoData_%s_%s_%s"%( self.usePseudoData,  channel, region),
        )

if __name__=='__main__':

    setup = Setup()
    estimator_mc = PolarisationEstimate( "polarisation_data", usePseudoData = True)
    estimator_mc._estimate( Region("Z_pt", (0, -1)), 'all', setup )
    estimator_data = PolarisationEstimate( "polarisation_data" )
    estimator_data._estimate( Region("Z_pt", (0, -1)), 'all', setup )
