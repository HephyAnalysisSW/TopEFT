import os

runOnGentT2 = True

if os.environ['USER'] in ['schoef', 'rschoefbeck', 'schoefbeck']:
    results_directory   = "/afs/hephy.at/data/rschoefbeck01/TopEFT/results/"
    runOnGentT2 = False

if os.environ['USER'] in ['dspitzbart', 'dspitzba']:
    results_directory   = "/afs/hephy.at/data/dspitzbart01/TopEFT/results/"
    plot_directory      = "/afs/hephy.at/user/d/dspitzbart/www/TopEFT/"
    runOnGentT2 = False

