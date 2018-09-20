import os

runOnGentT2 = True

if os.environ['USER'] in ['schoef', 'rschoefbeck', 'schoefbeck']:
    results_directory   = "/afs/hephy.at/data/rschoefbeck02/TopEFT/results/"
    skim_output_directory      = "/afs/hephy.at/data/rschoefbeck02/TopEFT/skims/"
    skim_directory      = "/afs/hephy.at/data/dspitzbart01/TopEFT/skims/"
    tmp_directory       = "/afs/hephy.at/data/rschoefbeck02/TopEFT_tmp/"
    plot_directory      = "/afs/hephy.at/user/r/rschoefbeck/www/TopEFT/"
    data_directory      = "/afs/hephy.at/data/rschoefbeck01/cmgTuples/"
    #data_directory      = "/afs/hephy.at/data/rschoefbeck02/cmgTuples/"
    #postprocessing_output_directory = "/afs/hephy.at/data/rschoefbeck01/cmgTuples/"
    postprocessing_output_directory = "/afs/hephy.at/data/rschoefbeck02/cmgTuples/"
    analysis_results    = results_directory

    runOnGentT2 = False

if os.environ['USER'] in ['dspitzbart', 'dspitzba']:
    tmp_directory       = "/afs/hephy.at/data/dspitzbart01/Top_tmp/"
    results_directory   = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/"
    skim_directory      = "/afs/hephy.at/data/dspitzbart01/TopEFT/skims/"
    skim_output_directory      = "/afs/hephy.at/data/dspitzbart01/TopEFT/skims/"
    plot_directory      = "/afs/hephy.at/user/d/dspitzbart/www/TopEFT/"
    combineReleaseLocation = '/afs/hephy.at/work/d/dspitzbart/top/devel/CMSSW_8_1_0/src'
    dpm_directory = '/dpm/oeaw.ac.at/home/cms/store/user/dspitzba/'
    #data_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
    data_directory     = "/afs/hephy.at/data/rschoefbeck02/cmgTuples/"
    postprocessing_output_directory = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
    analysis_results    = results_directory
    
    runOnGentT2 = False

if os.environ['USER'] in ['gmoertl']:
    plot_directory      = "/afs/hephy.at/user/g/gmoertl/www/"
    plot_directory          = "/afs/hephy.at/user/g/gmoertl/www/"
    skim_output_directory   = "/afs/hephy.at/data/gmoertl01/lepton/skims/"
    trainingFiles_directory = "/afs/hephy.at/data/gmoertl01/lepton/trainfiles/"

if os.environ['USER'] in ['llechner']:
    tmp_directory                   = "/afs/hephy.at/data/llechner01/Top_tmp/"
    results_directory               = "/afs/hephy.at/data/llechner01/TopEFT/results/"
    skim_directory                  = "/afs/hephy.at/data/llechner01/TopEFT/skims/"
    skim_output_directory           = "/afs/hephy.at/data/llechner01/TopEFT/skims/"
    plot_directory                  = "/afs/hephy.at/user/l/llechner/www/TopEFT/"
    data_directory                  = "/afs/hephy.at/data/dspitzbart02/cmgTuples/"
    postprocessing_output_directory = "/afs/hephy.at/data/llechner01/TopEFT/cmgTuples/"
    analysis_results                = results_directory
    
    runOnGentT2 = False

