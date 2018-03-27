# Standard imports 
import os
import ROOT

# RootTools
from RootTools.core.standard import *

# Logging
import logging
logger = logging.getLogger(__name__)

def singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance


def getSubDir(dataset, path):
    import re
    m=re.match("\/(.*)\/(.*)\/(.*)",dataset)
    if not m :
        print "NO GOOD DATASET"
        return
    if os.environ['USER'] in ['tomc']: 
      d=re.match("(.*)/cmgTuples/(.*)",path)
      return m.group(1)+"/"+m.group(2)+'_'+d.group(2)
    else :                             
      return m.group(1)+"_"+m.group(2)

def fromHeppySample(sample, data_path, module = None, maxN = None, MCgeneration = "Summer16"):
    ''' Load CMG tuple from local directory
    '''

    import importlib
    if module is not None:
        module_ = module
    elif "Run2016" in sample:
        module_ = 'CMGTools.RootTools.samples.samples_13TeV_DATA2016'
    elif "Run2017" in sample:
        module_ = 'CMGTools.RootTools.samples.samples_13TeV_DATA2017'
    elif "ttZ0j_ll" in sample or "ttGamma0j_ll" in sample:
        module_ = 'CMGTools.StopsDilepton.ttX0j_5f_MLM_signals_RunIISummer16MiniAODv2'
    elif "ewkDM" in sample:
        module_ = 'CMGTools.StopsDilepton.ewkDM_signals_RunIISummer16MiniAODv2'
    else: 
        if MCgeneration == "Summer17":
            module_ = 'CMGTools.RootTools.samples.samples_13TeV_RunIISummer17MiniAODv2'
        elif MCgeneration == "Fall17":
            module_ = 'CMGTools.RootTools.samples.samples_13TeV_RunIIFall17MiniAOD'
        else:
            module_ = 'CMGTools.RootTools.samples.samples_13TeV_RunIISummer16MiniAODv2'

    try:
        heppy_sample = getattr(importlib.import_module( module_ ), sample)
    except:
        raise ValueError( "Could not load sample '%s' from %s "%( sample, module_ ) )

    subDir = getSubDir(heppy_sample.dataset, data_path)
    if not subDir:
        raise ValueError( "Not a good dataset name: '%s'"%heppy_sample.dataset )

    path = os.path.join( data_path, subDir )
    from TopEFT.Tools.user import runOnGentT2
    if runOnGentT2: 
        sample = Sample.fromCMGCrabDirectory(
            heppy_sample.name, 
            path, 
            treeFilename = 'tree.root', 
            treeName = 'tree', isData = heppy_sample.isData, maxN = maxN)
    else:  # Vienna -> Load from DPM 
        if True: #'/dpm' in data_path:

            from RootTools.core.helpers import renew_proxy
            user = os.environ['USER']
            # Make proxy in afs to allow batch jobs to run
            proxy_path = os.path.expandvars('$HOME/private/.proxy')
            proxy = renew_proxy( proxy_path )
            logger.info( "Using proxy %s"%proxy )

            if module is not None:
                module_ = module
            if "Run2016" in sample:
                from TopEFT.samples.heppy_dpm_samples import data_03Feb2017_heppy_mapper as data_heppy_mapper
                return data_heppy_mapper.from_heppy_samplename(heppy_sample.name, maxN = maxN)
            elif "Run2017" in sample:
                from TopEFT.samples.heppy_dpm_samples import data_Run2017_heppy_mapper as data_Run2017_heppy_mapper
                return data_Run2017_heppy_mapper.from_heppy_samplename(heppy_sample.name, maxN = maxN)
            elif "Summer17" in heppy_sample.dataset:
                from TopEFT.samples.heppy_dpm_samples import Summer17_heppy_mapper
                return Summer17_heppy_mapper.from_heppy_samplename(heppy_sample.name, maxN = maxN)
            elif "Fall17" in heppy_sample.dataset:
                from TopEFT.samples.heppy_dpm_samples import Fall17_heppy_mapper
                return Fall17_heppy_mapper.from_heppy_samplename(heppy_sample.name, maxN = maxN)
            elif "ttZ0j_ll" in sample or "ttGamma0j_ll" in sample:
                from TopEFT.samples.heppy_dpm_samples import signal_0j_0l_heppy_mapper
                return signal_0j_0l_heppy_mapper.from_heppy_samplename(heppy_sample.name, maxN = maxN)
            elif "TTZToLL_LO" in sample:
                from TopEFT.samples.heppy_dpm_samples import signal_madspin_heppy_mapper
                return signal_madspin_heppy_mapper.from_heppy_samplename(heppy_sample.name, maxN = maxN)
            elif "ewkDM" in sample:
                from TopEFT.samples.heppy_dpm_samples import signal_heppy_mapper
                return signal_heppy_mapper.from_heppy_samplename(heppy_sample.name, maxN = maxN)
            else: 
                from TopEFT.samples.heppy_dpm_samples import mc_heppy_mapper
                return mc_heppy_mapper.from_heppy_samplename(heppy_sample.name, maxN = maxN)
            raise ValueError
        else:                           
            sample = Sample.fromCMGOutput(
                heppy_sample.name, 
                path, 
                treeFilename = 'tree.root', 
                treeName = 'tree', isData = heppy_sample.isData, maxN = maxN)

    sample.heppy = heppy_sample
    return sample

