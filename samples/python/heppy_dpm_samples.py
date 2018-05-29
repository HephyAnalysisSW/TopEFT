'''
Extract cmg samples from dpm'''

if __name__ == '__main__':
    # Parse args if main
    maxN_def = -1
    def get_parser():
        ''' Argument parser for post-processing module.
        '''
        import argparse
        argParser = argparse.ArgumentParser(description = "Argument parser for cmgPostProcessing")
        argParser.add_argument('--logLevel', action='store', nargs='?', choices=['CRITICAL', 'ERROR', 'WARNING', 'DEBUG', 'DEBUG', 'TRACE', 'NOTSET'], default='INFO', help="Log level for logging" )
        argParser.add_argument('--overwrite', action='store_true', default=False, help="Overwrite cache?" )
        argParser.add_argument('--nomultithreading', action='store_true', default=False, help="No multithreading?" )
        argParser.add_argument('--maxN', action='store', type=int, default=maxN_def, help="Overwrite cache?" )

        return argParser

    options = get_parser().parse_args()

    # Logging
    import TopEFT.Tools.logger as logger_
    logger = logger_.get_logger(options.logLevel, logFile = None )
    
    overwrite = options.overwrite
    multithreading = not options.nomultithreading
    maxN = options.maxN

else:
    # Logging
    import logging
    logger = logging.getLogger(__name__)
    multithreading = False
    overwrite = False 
    maxN =      -1

# TopEFT
from TopEFT.samples.walk_dpm import walk_dpm
from RootTools.core.helpers import checkRootFile

# Standard imports
import os
import pickle

class heppy_mapper:

    def __init__(self, heppy_samples, dpm_directories, cache_file, multithreading=True):
        # Read cache file, if exists
        if os.path.exists( cache_file ) and not overwrite:
            self.sample_map = pickle.load( file(cache_file) )
            logger.info( "Loaded cache file %s" % cache_file )
        else:
            logger.info( "Cache file %s not found. Recreate map.", cache_file)
            logger.info( "Check proxy.")

            # Proxy certificate
            from RootTools.core.helpers import renew_proxy
            # Make proxy in afs to allow batch jobs to run
            proxy_path = os.path.expandvars('$HOME/private/.proxy')
            proxy = renew_proxy( proxy_path )
            logger.info( "Using proxy %s"%proxy )

            # Read dpm directories
            self.cmg_directories = {}
            for data_path in dpm_directories:
                logger.info( "Walking dpm directory %s", data_path )
                walker = walk_dpm( data_path )
                self.cmg_directories[ data_path ] = walker.walk_dpm_cmgdirectories('.',  maxN = maxN )
                
                #del walker

            logger.info( "Now mapping directories to heppy samples" )
            for heppy_sample in heppy_samples:
                heppy_sample.candidate_directories = []
                pd, era = heppy_sample.dataset.split('/')[1:3]
                for data_path in self.cmg_directories.keys():
                    for dpm_directory in self.cmg_directories[data_path].keys():
                        if not ('/%s/'%pd in dpm_directory):
                            logger.debug( "/%s/ not in dpm_directory %s", pd, dpm_directory )
                            continue
                        if not ('/'+era in dpm_directory):
                            logger.debug( "/%s not in dpm_directory %s", era, dpm_directory )
                            continue
                        heppy_sample.candidate_directories.append([data_path, dpm_directory])
                        logger.debug( "heppy sample %s in %s", heppy_sample.name, dpm_directory)
                logger.info(  "Found heppy sample %s in %i directories.", heppy_sample.name, len(heppy_sample.candidate_directories) ) 

            # Merge
            from RootTools.core.Sample import Sample
            logger.info( "Now making new sample map from %i directories and for %i heppy samples to be stored in %s", len(dpm_directories), len(heppy_samples), cache_file )
            self.sample_map = {}
            for heppy_sample in heppy_samples:
                if len(heppy_sample.candidate_directories)==0:
                    logger.info("No directory found for %s", heppy_sample.name)
                else:
                    normalization, files = walker.combine_cmg_directories(\
                            cmg_directories = {dpm_directory:self.cmg_directories[data_path][dpm_directory] for data_path, dpm_directory in heppy_sample.candidate_directories }, 
                            multithreading = multithreading, 
                        )
                    logger.info( "Sample %s: Found a total of %i files with normalization %3.2f", heppy_sample.name, len(files), normalization)
                    tmp_files = []
                    for f in files:
                        isGoodFile = False
                        try:
                            isGoodFile = checkRootFile("root://hephyse.oeaw.ac.at/" + os.path.join( f ))
                            logger.debug("File %s got added", f)
                        except IOError:
                            logger.info("File %s is corrupted, skipping",f)
                        if isGoodFile: tmp_files.append(f)
                    self.sample_map[heppy_sample] = Sample.fromFiles(
                        heppy_sample.name,
                        files = ['root://hephyse.oeaw.ac.at/'+f for f in tmp_files],
                        normalization = normalization, 
                        treeName = 'tree', isData = heppy_sample.isData, maxN = maxN)
                    
                    logger.info("Combined %i directories for sample %s to a total of %i files with normalization %3.2f", len(heppy_sample.candidate_directories), heppy_sample.name, len(files), normalization)

            # Store cache file
            dir_name = os.path.dirname( cache_file ) 
            if len(self.sample_map.keys())>0:
                if not os.path.exists( dir_name ): os.makedirs( dir_name )
                pickle.dump( self.sample_map, file( cache_file, 'w') )
                logger.info( "Created MC sample cache %s", cache_file )
            else:
                logger.info( "Skipping to write %s because map is empty.", cache_file )

    @property                
    def heppy_sample_names( self ):
        return [s.name for s in self.sample_map.keys()]

    def from_heppy_sample( self, heppy_sample, maxN = -1):
        if self.sample_map.has_key( heppy_sample ):
            res = self.sample_map[heppy_sample]
            if maxN>0: res.files = res.files[:maxN]
            res.heppy = heppy_sample
            return res
    def from_heppy_samplename( self, heppy_samplename, maxN = -1):
        for heppy_sample in self.sample_map.keys():
            if heppy_samplename==heppy_sample.name:
                res = self.sample_map[heppy_sample]
                if maxN>0: res.files = res.files[:maxN]
                res.heppy = heppy_sample
                return res
        
# Proxy certificate
from RootTools.core.helpers import renew_proxy
# Make proxy in afs to allow batch jobs to run
proxy_path = os.path.expandvars('$HOME/private/.proxy')
proxy = renew_proxy( proxy_path )
logger.info( "Using proxy %s"%proxy )

# Data 2016, 03Feb2017
data_cache_file = '/afs/hephy.at/data/rschoefbeck01/TopEFT/dpm_sample_caches/Run2016_data_2016_1l_v1.pkl'
robert_2016_1l_v1 = ['/dpm/oeaw.ac.at/home/cms/store/user/schoef/cmgTuples/2016_1l_v1']
data_dpm_directories = robert_2016_1l_v1
from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import dataSamples as heppy_data_samples
data_03Feb2017_heppy_mapper = heppy_mapper( heppy_data_samples, data_dpm_directories , data_cache_file, multithreading=multithreading)

# Summer16 MC
mc_cache_file = '/afs/hephy.at/data/rschoefbeck01/TopEFT/dpm_sample_caches/80X_MC_Summer16_2016_1l_v1_4.pkl'
robert_2016_1l_v1 = ['/dpm/oeaw.ac.at/home/cms/store/user/schoef/cmgTuples/2016_1l_v1']
mc_dpm_directories = robert_2016_1l_v1
from CMGTools.RootTools.samples.samples_13TeV_RunIISummer16MiniAODv2 import mcSamples as heppy_mc_Moriond_samples
mc_heppy_mapper = heppy_mapper( heppy_mc_Moriond_samples, mc_dpm_directories, mc_cache_file, multithreading=multithreading)

# Private signal MC with 0 jets (LO) and 0 lepton requirement
signal_cache_file = '/afs/hephy.at/data/rschoefbeck01/TopEFT/dpm_sample_caches/80X_signal_ttX0j_0l_5f_MLM_signals_RunIISummer16MiniAODv2_2016_0l_v1.pkl'
robert = ['/dpm/oeaw.ac.at/home/cms/store/user/schoef/cmgTuples/2016_0l_v1']
signal_dpm_directories = robert
from CMGTools.StopsDilepton.ttX0j_5f_MLM_signals_RunIISummer16MiniAODv2 import signalSamples as ttX0j_signal_samples
signal_0j_0l_heppy_mapper = heppy_mapper( ttX0j_signal_samples, signal_dpm_directories, signal_cache_file, multithreading=multithreading)

# Data 2017, 17Nov2017
data_cache_file_2017 = '/afs/hephy.at/data/rschoefbeck01/TopEFT/dpm_sample_caches/Run2017_data_94X_1l_v9.pkl'
robert_1l_94X = ['/dpm/oeaw.ac.at/home/cms/store/user/schoef/cmgTuples/94X_1l_v9']
data_dpm_directories = robert_1l_94X
from CMGTools.RootTools.samples.samples_13TeV_DATA2017 import dataSamples as heppy_data_samples_2017
data_Run2017_heppy_mapper = heppy_mapper( heppy_data_samples_2017, data_dpm_directories , data_cache_file_2017, multithreading=multithreading)

# Fall17 MC
Fall17_cache_file = '/afs/hephy.at/data/dspitzbart01/TopEFT/dpm_sample_caches/94X_MC_Fall17_94X_1l_v10_2.pkl'
robert_94X = ['/dpm/oeaw.ac.at/home/cms/store/user/schoef/cmgTuples/94X_1l_v10', '/dpm/oeaw.ac.at/home/cms/store/user/dspitzba/cmgTuples/94X_1l_v10']
mc_dpm_directories = robert_94X
from CMGTools.RootTools.samples.samples_13TeV_RunIIFall17MiniAOD import mcSamples as heppy_Fall17_samples
Fall17_heppy_mapper = heppy_mapper( heppy_Fall17_samples, mc_dpm_directories, Fall17_cache_file, multithreading=multithreading)
