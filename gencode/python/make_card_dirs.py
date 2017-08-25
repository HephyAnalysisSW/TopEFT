#Standard imports
import os

# TopEFT
from TopEFT.gencode.coupling_card import coupling_card

# Logger
import logging
logger = logging.getLogger(__name__)

process = "ttZ0j_5f_TopEFT"

for i in range(2,3):
    for j in range(-10,11):
            if j == 0: continue
            coup = coupling_card(process,i,j/10.)
            coup.writeCards(v=0)
            logger.info( "./gridpack_generation.sh %s %s 1nd", coup.identifier, coup.outDir )
