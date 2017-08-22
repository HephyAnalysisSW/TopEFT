from TopEFT.gencode.EFT import *


couplingValues = [0.051,0.056,0.061,0.066,0.072]

def main():
    config = configuration('HEL_UFO')
    config.setup()
    
    #HEL_couplings = coupling("newcoup", HEL_couplings_newcoup)
    #HEL_couplings.setCoupling('cuW',0.051)

    for cv in couplingValues:
        getXsec(cv,config)
        #HEL_couplings.setCoupling('cuW',0.061)

        #ttz_test = process("ttZ", 50000, config)
        #ttz_test.addCoupling(HEL_couplings)
    
        #ttz_test.run(keepGridpack=False)
    
    #del ttz_test
    del config


def getXsec(cv,config):
    HEL_couplings = couplings()
    HEL_couplings = addBlock("newcoup", HEL_couplings_newcoup)
    HEL_couplings.setCoupling('cuW',cv)

    print "cuW", cv
    ttz_test = process("ttZ", 50000, config)
    ttz_test.addCoupling(HEL_couplings)

    ttz_test.run(keepGridpack=False)

