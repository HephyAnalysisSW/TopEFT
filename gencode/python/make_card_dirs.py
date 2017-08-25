import os
from coupling_card import coupling_card

process = "ttZ0j_5f_TopEFT"

for i in range(2,3):
    for j in range(-10,11):
            if j == 0: continue
            coup = coupling_card(process,i,j/10.)
            coup.writeCards(v=0)
            print "./gridpack_generation.sh %s %s 1nd"%(coup.identifier, coup.outDir)
