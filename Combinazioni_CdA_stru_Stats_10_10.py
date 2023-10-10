

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:29:03 2023

@author: franc
"""
#====================================
#questo serve per fare il prodotto cartesiano tra due liste
from itertools import product 
#====================================
#importo le funzioni dal file relativo
from Funzioni_CdA_Str_10_10 import calcolo_CdA_str
# import json
import pandas as pd
import numpy  as np
import os
import matplotlib.pyplot as plt
import sys
# file_json = "Database_CdA_stru2.json"


#
# ---- Definizione delle liste per la P_stru
#
# Queste sono le liste dei possibili dati di imput dei due parametri che caratterizzano la valutazione della Pericolosità Strutturale

X_veicoli   =     [1,2,3]     # pos.0 #Frequenza di transito dei veicoli commerciali 1: alta, 2: media, 3: bassa
X_lim_traff =     [1,2,3,4,5] # pos.1 #Classi di pericolosità in funzione della classe stradale 1: alta, 2: media-alta, 3: media, 4: medio-bassa, 5: bassa

#
# ---- Definizione delle liste per la V_stru
#

X_dif       =     [1,2,3,4,5]     # pos.2 [1 Alta, 2 Medio-Alta, 3 Media, 4 MB, 5 Bassa]
X_an_rif    =     [1,2,3]         # pos.3 [1 < 1945, 2 1945<<1980, 3 >1980]
X_norma     =     [1,2,3]         # pos.4 [1 Classe A, 2 Classe B, 3 Classe C]
X_sali      =     [1,2]  # pos. 5
X_V_4str    =     [(1,1,1), (1,1,2), (1,1,3), (1,1,4), (1,2,1), (1,2,2), (1,2,3), (1,2,4),
                    (1,3,1), (1,3,2), (1,3,3), (1,3,4), (1,4,1), (1,4,2), (1,4,3), (1,4,4),
                    (1,5,1), (1,5,2), (1,5,3), (1,5,4), (1,6,1), (1,6,2), (1,6,3), (1,6,4),
                    (2,1,1), (2,1,2), (2,1,3), (2,1,4), (2,2,1), (2,2,2), (2,2,3), (2,2,4),
                    (2,3,1), (2,3,2), (2,3,3), (2,3,4), (2,4,1), (2,4,2), (2,4,3), (2,4,4),
                    (2,6,1), (2,6,2), (2,6,3), (2,6,4), (3,7,1), (3,7,2), (3,7,3), (3,7,4),
                    (3,1,1), (3,1,2), (3,1,3), (3,1,4), (4,1,1), (4,1,2), (4,1,3), (4,1,4), 
                    (5,1,1), (5,1,2), (5,1,3), (5,1,4), (5,2,1), (5,2,2), (5,2,3), (5,2,4),
                    (5,3,1), (5,3,2), (5,3,3), (5,3,4), (5,4,1), (5,4,2), (5,4,3), (5,4,4), 
                    (5,6,1), (5,6,2), (5,6,3), (5,6,4), (6,1,1), (6,1,2), (6,1,3), (6,1,4), 
                    (7,1,1), (7,1,2), (7,1,3), (7,1,4)]  # pos.6   (s_st, mat, L_max)

#---- ponti in c.a.p. con luce >15m
# X_V_4str    =     [(1,2,3), (1,2,4), (2,2,3), (2,2,4), (5,2,3), (5,2,4)] 
#---- ponti in c.a.p. con luce <15m
#X_V_4str    =     [(1,2,1), (1,2,2), (2,2,1), (2,2,2), (5,2,1), (5,2,2)]  # pos.5    (s_st, mat, L_max) # pos.5    (s_st, mat, L_max)
X_n_camp    =     [1,2] # pos.7

#
# ---- Definizione delle liste per la E_stru
#

X_tgm         =   [1,2,3] # # pos.8  [1 Alta, 2 Media, 3 Bassa]
X_L_med       =   [1,2,3] # # pos.9  [1 grande luce, 2 media luce, 3 piccola luce]
X_persone     =   [1,2]   # # pos.10  [1 frequente passaggio, 2 no passaggio]
X_alt_strad   =   [1,2]   # # pos.11 [1 assenza, 2 presenza]
X_scavalc     =   [1,2,3] # # pos.12 [1 Alta, 2 Media, 3 Bassa]
# X_merci_per   =   [1,2]   # 7 # da commentare


X = [X_veicoli,     # SE MODIFICO L'ORDINE DEI PARAMETRI DEVO AGGIORNARE IL DIZIONARIO "elenco_parametri"
     X_lim_traff,
     #---------------
     X_dif,
     X_an_rif,
     X_norma,
     X_sali,
     X_V_4str,
     # X_s_st,
     # X_mat,  
     # X_L_max, 
     X_n_camp, 
     #---------------
     X_tgm,
     X_L_med,
     X_persone,
     X_alt_strad,
     X_scavalc]
#
# ---- Calcolo delle combinazioni possibili
#

# n_parametri = len(X)

# Devo prima inserire delle condizioni per le combinazioni tra s_st, mat, L_max
combinazioni = list(product(*X))

# print(combinazioni)

#
# ---- Calcolo della CdA
#
CdA_numero = {5 : 'Low', 4 : 'Medium-Low', 3 :'Medium', 2 : 'Medium-High', 1 : 'High'}
CdA_stru = []
Comb     = []

for parametri in combinazioni:
    CdA_stru.append(calcolo_CdA_str(parametri))
    # Per spacchettare X_V_4str e avere in input un vettore di soli numeri
    Comb.append(parametri[0:6] + parametri[6] + parametri[7:14])

target    = ["Pstr", 'Vstr','Estr', 'CdA_str']
nomi_parametri_Estr = ['tgm', 'L_med', 'persone', 'alt_strad', 'scavalc']
nomi_parametri_Pstr = ['veicoli','lim_traff']
nomi_parametri_Vstr = ['dif', 'an_rif','norma', 'sali', 's_st', 'mat', 'L_max', 'n_camp']


# Database_CdA_stru = pd.DataFrame([Comb + CdA_stru], columns = nomi_parametri_Pstr + nomi_parametri_Vstr + nomi_parametri_Estr + target)

df_features_CdA_stru = pd.DataFrame(Comb, columns = nomi_parametri_Pstr + nomi_parametri_Vstr + nomi_parametri_Estr)

df_target_CdA_stru = pd.DataFrame(CdA_stru, columns = target)

# Salva il DataFrame df_target_CdA_stru come file CSV
nome_file_csv = "stats_CdA_Stru_10_10.csv"
df_target_CdA_stru.to_csv(nome_file_csv, index=False)

print(f"Il DataFrame df_target_CdA_stru è stato salvato come file CSV: {nome_file_csv}")





