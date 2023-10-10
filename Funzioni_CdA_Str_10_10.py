# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 15:17:17 2023

@author: franc
"""
from Dizionari_10_10 import *

# =======================================================
# CdA_stru = 
# Calcolo CdA strutturale
# =======================================================

def calcolo_CdA_str(parametri):
        
    # ---- Calcolo della pericolosità strutturale
    # Elenco dei parametri per P_stru
    nomi_parametri_Pstr = ['veicoli','lim_traff']
    # lista delle posizioni dei parametri all'interno di X per la pericolosità strutturale
    # pos_X_Pstr = [elenco_parametri.get(i) for i in nomi_parametri_Pstr]
    pos_X_Pstr = [elenco_parametri[i] for i in nomi_parametri_Pstr]
    # estraggo i parametri necessari per Pstr
    par_Pstr = tuple([parametri[i] for i in pos_X_Pstr]) 
    # Valuto la pericolosità strutturale
    Pstr = P_strutt(*par_Pstr)
    
    
    
#     # ---- Calcolo vulnerabilità strutturale
#     # Elenco dei parametri per v_stru
    #nomi_parametri_Vstr = ['dif', 'an_rif','norma','s_st', 'mat', 'L_max', 'n_camp']
    nomi_parametri_Vstr = ['dif', 'an_rif','norma','sali','V_4_stru', 'n_camp']
#     # lista delle posizioni dei parametri all'interno di X[V_stru]
    pos_X_Vstr = [elenco_parametri.get(i) for i in nomi_parametri_Vstr]
#     # estraggo i parametri necessari per Pstr
    par_Vstr = tuple([parametri[i] for i in pos_X_Vstr]) 
#     # Valuto la pericolosità strutturale
    Vstr = V_strutt(*par_Vstr)
    
    
    
#     # ---- Calcolo dell'esposizione strutturale
#     # Elenco dei parametri per E_stru
    nomi_parametri_Estr = ['tgm', 'L_med', 'persone', 'alt_strad', 'scavalc']
#     # lista delle posizioni dei parametri all'interno di X[E_stru]
    pos_X_Estr = [elenco_parametri.get(i) for i in nomi_parametri_Estr]
#     # estraggo i parametri necessari per Pstr
    par_Estr = tuple([parametri[i] for i in pos_X_Estr]) 
#     # Valuto la pericolosità strutturale
    Estr = E_strutt(*par_Estr)
    
    
#     # ---- Calcolo cda strutturale
    # CdA_stru = 0
    CdA_stru = CdA_strutt(Pstr, Vstr, Estr)
    
    
    return Pstr,Vstr,Estr,CdA_stru

# #CDA Strutturale
# #---------------------------------------
#---- Pericolosità strutturale
# #---------------------------------------
def P_strutt(veicoli, lim_traff):
    
    Pstr = P_str[(veicoli, lim_traff)]
    
    return Pstr
# #---------------------------------------
#---- Vunerabilità strutturale
# #---------------------------------------
def V_strutt(dif, an_rif, norma, sali, V_4_stru, n_camp):
        
    if   dif == 1:
          Vstr = 1
    else:
        # SSstr    = s_st*10 + mat
        V1    = V_1str[(dif, an_rif)]
        V2    = V_2str[(V1, norma, sali)]
        V4    = V_4str[(V_4_stru)]
        V5    = V_5str[(n_camp, V4)]
        
        Vstr  = V_str[(V2, V5)]
    
    return Vstr
# #---------------------------------------
#---- Esposizione strutturale
# #---------------------------------------
def E_strutt(tgm, L_med, persone, alt_strad, scavalc):
    
    E10 = E_1_0str[(tgm, L_med)]
    E1  = E_1str[(persone, E10)]
    E2  = E_2str[(alt_strad,E1)]
    
    Estr = E_str[(E2, scavalc)]
    
    # Estr = E_str[(Estr0, merci_per)]
    
    return Estr

# #---------------------------------------
#---- CdA strutturale e fondazionale
# #---------------------------------------

def CdA_strutt(Pstr, Vstr, Estr):
    
    CdAstr = Tabella_CdA[(Pstr, Vstr, Estr)]
    
    return CdAstr