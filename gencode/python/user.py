import os

runOnGentT2 = True

if os.environ['USER'] in ['schoef', 'rschoefbeck', 'schoefbeck']:
    runOnGentT2 = False

if os.environ['USER'] in ['dspitzbart', 'dspitzba']:
    # Where the plots go
    plot_directory      = "/afs/hephy.at/user/d/dspitzbart/www/TopEFT/"
    runOnGentT2 = False

