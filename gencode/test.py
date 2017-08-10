from TopEFT.gencode.EFT import *

config = configuration()

HEL_couplings = coupling("newcoup", HEL_couplings_newcoup)

ttz_test = process("ttz_test", 10, config)
ttz_test.addCoupling(HEL_couplings)
ttz_test.couplings[0].setCoupling('cu',1.0)

ttz_test.updateRestrictCard()
