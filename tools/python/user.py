import os

runOnGentT2 = True

if os.environ['USER'] in ['schoef', 'rschoefbeck', 'schoefbeck']:
    results_directory   = "/afs/hephy.at/data/rschoefbeck02/TopEFT/results/"
    tmp_directory       = "/afs/hephy.at/data/rschoefbeck02/TopEFT_tmp/"
    plot_directory      = "/afs/hephy.at/user/r/rschoefbeck/www/TopEFT/"
    runOnGentT2 = False

if os.environ['USER'] in ['dspitzbart', 'dspitzba']:
    tmp_directory       = "/afs/hephy.at/data/dspitzbart01/Top_tmp/"
    results_directory   = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/"
    plot_directory      = "/afs/hephy.at/user/d/dspitzbart/www/TopEFT/"
    runOnGentT2 = False

