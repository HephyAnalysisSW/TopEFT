from TopEFT.gencode.EFT import *

config = configuration('HEL_UFO')
config.setup()

HEL_couplings = coupling("newcoup", HEL_couplings_newcoup)
HEL_couplings.setCoupling('cuW',0.013)

ttz_test = process("ttZ", 50000, config)
ttz_test.addCoupling(HEL_couplings)

ttz_test.run()

del config
