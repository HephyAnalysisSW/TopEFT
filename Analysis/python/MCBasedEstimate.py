# Logging
import logging
logger = logging.getLogger(__name__)

from TopEFT.Analysis.Region import Region
from TopEFT.Tools.u_float import u_float
from TopEFT.Analysis.SystematicEstimator import SystematicEstimator
from TopEFT.Analysis.SetupHelpers import trilepChannels, quadlepChannels, channel


class MCBasedEstimate(SystematicEstimator):
    def __init__(self, name, sample, cacheDir=None):
        super(MCBasedEstimate, self).__init__(name, cacheDir=cacheDir)
        self.sample=sample

        # FastSim and 76X only for the MCBasedEstimate. Dirty. Looks whether one of the samples is fastsim.
        self.isFastSim = getattr(sample, "isFastSim", False) 
        
    def _estimate(self, region, channel, setup):

        ''' Concrete implementation of abstract method 'estimate' as defined in Systematic
        '''

        logger.debug( "MC prediction for %s channel %s" %(self.name, channel.name) )

        if channel.name=='all':
            # 'all' is the total of all contributions
            if setup.nLeptons == 3: channels = trilepChannels
            elif setup.nLeptons == 4: channels = quadlepChannels
            else: raise NotImplementedError
            return sum([self.cachedEstimate(region, c, setup) for c in channels])

        #elif channel=='SF':
        #    # 'all' is the total of all contributions
        #    return sum([self.cachedEstimate(region, c, setup) for c in ['MuMu', 'EE']])

        else:
            preSelection = setup.preselection('MC', nElectrons=channel.nE, nMuons=channel.nM, isFastSim = self.isFastSim)
            cut = "&&".join([region.cutString(setup.sys['selectionModifier']), preSelection['cut']])
            weight = preSelection['weightStr']

            logger.debug( "Using cut %s and weight %s"%(cut, weight) )
            res = setup.lumi/1000.*u_float(**self.sample.getYieldFromDraw(selectionString = cut, weightString = weight) )
            return setup.lumi/1000.*u_float(**self.sample.getYieldFromDraw(selectionString = cut, weightString = weight) )
