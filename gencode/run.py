from TopEFT.gencode.EFT import *


## cuW
#coup = "cuW"
#couplingValues = [ i*0.077/15 for i in range(-15,15) ]

## cuG
#coup = "cuG"
#couplingValues = [ i*0.007/15 for i in range(-15,15) ]

# cuB
coup = "cuB"
couplingValues = [ i*0.3/15 for i in range(-15,15) ]

processes = ['ttZ','ttW','ttH']
#processes = ['ttZ','ttH']
#processes = ['ttW']

def wrapper(p):
    config = configuration('HEL_UFO')
    config.setup()

    for cv in couplingValues[:17]:
        HEL_couplings = couplings()
        HEL_couplings.addBlock("newcoup", HEL_couplings_newcoup)
        HEL_couplings.setCoupling(coup,cv)

        print coup, cv
        ttz_test = process(p, 50000, config)
        ttz_test.addCoupling(HEL_couplings)

        ttz_test.run(keepGridpack=False, overwrite=True)
        del ttz_test

    config.clean()
    del config

from multiprocessing import Pool
pool = Pool(processes=8)
results = pool.map(wrapper, processes)

pool.close()
pool.join()

