import os
from coupling_card import coupling_card

process = "ttZ0j_5f_TopEFT"

for i in range(2,7):
    for j in range(-10,11):
            if j == 0: continue
            coupling_card(process,i,j/10.).writeCards()
