# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 15:32:58 2023

@author: franc
"""


elenco_parametri = {'veicoli'   :   0,    # PERICOLOSITA' STRUTTURALE
                    'lim_traff' :   1,
                    #-------------------- # VULNERABILITA' STRUTTURALE
                    'dif'       :   2,   
                    'an_rif'    :   3,
                    'norma'     :   4,
                    'sali'      :   5,
                    # 's_st'      :   5,
                    # 'mat'       :   6, 
                    # 'L_max'     :   7,
                    'V_4_stru'  :   6,
                    'n_camp'    :   7,
                    #-------------------- # ESPOSIZIONE STRUTTURALE
                    'tgm'       :   8,   
                    'L_med'     :   9,
                    'persone'   :   10,
                    'alt_strad' :   11,
                    'scavalc'   :   12}
                     # 'merci_per':    12
                     
elenco_parametri_sism = {              
                        #-------------------- # PERICOLOSITA' SISMICA
                         'ag'        :   0,  
                         'Ti'        :   1,
                         'cat_sot'   :   2,
                         #-------------------- # VULNERABILITA' SISMICA
                         'mat_sc-st_luce_camp':   3,
                         'el_vuln'   :   4,
                         'difsism'   :   5,
                         'Crit_prog' :   6,
                         #-------------------- # ESPOSIZIONE SISMICA
                         'tgm'       :   7,   
                         'L_med'     :   8,
                         'persone'   :   9,
                         'alt_strad' :   10,
                         'scavalc'   :   11,
                         'strat'     :   12}

elenco_parametri_frane= {              
                        #-------------------- # PERICOLOSITA' Frane
                         'st_attività'        :   0,  
                         'max_velocità'        :   1,
                         'magnitudo'   :   2,
                         'aff_valut':   3,
                         'mis_miti'   :   4,
                         #-------------------- # VULNERABILITA' FRANE
                         'tip_strutt_fond'   :   5,
                         'est_interf' :   6,
                         #-------------------- # ESPOSIZIONE FRANE
                         'esp_sism'       :   7}
#---- 1 ------------------------------------    
#---- Valutazione CdA Strutturale e fondazionale
#----  ------------------------------------
#---- 1.1 Classe di Pericolosità strutturale
#Combinazione attraverso la tabella 4.3 di: 
    #Frequenza passaggi veicoli commerciali (tab 4.4) 
        #1-->Alta
        #2-->Media
        #3-->Bassa
    #Classificazione delle strade in funzione della massima massa ammissibile (tab 4.2)
        #1-->Classe A
        #2-->Classe B
        #3-->Classe C
        #4-->Classe D
        #5-->Classe E
P_str = {   (1,1) : 1,
            (2,1) : 1,
            (3,1) : 2,
            (1,2) : 1,
            (2,2) : 2,
            (3,2) : 3,
            (1,3) : 2,
            (2,3) : 3,
            (3,3) : 4,
            (1,4) : 3,
            (2,4) : 4,
            (3,4) : 5,
            (1,5) : 5,
            (2,5) : 5,
            (3,5) : 5}

#---- 1.2 Classe di Vulnerabilità strutturale:
    #Definizione della Rapidità di evoluzione del degrado [Classe V1] (fig 4.2) attraverso la combinazione di:
        #Difetti di gravità   
            #1-->Alto
            #2-->Medio-Alto
            #3-->Medio
            #4-->Medio-Basso
            #5-->Basso
        #Periodo di costruzione- ultimo intervento di manutenzione significativo 
            #1--> antecedente al 1945
            #2--> compreso tra il 1945 e il 1980
            #3--> posteriore al 1980
            
V_1str = {  (1,1): 1,
            (2,1): 2,
            (3,1): 4,
            (4,1): 5,
            (5,1): 5,
            (1,2): 1,
            (2,2): 2,
            (3,2): 3,
            (4,2): 4,
            (5,2): 5,
            (1,3): 1,
            (2,3): 1,
            (3,3): 2,
            (4,3): 3,
            (5,3): 4}
 
# for i in [1,2,3,4,5]:
#     for j in [1,2,3]:
#         print('(Livello difettosità  = ',i,' Anno di riferimento = ',j,') --> V1str = ',V_1str[(i,j)])  
             

    #Definizione Norma di progettazione [Classe V2] (fig4.2) attraverso la combinazione di:
        #Classe V1 
            #1-->Alta
            #2-->Medio-Alta
            #3-->Media
            #4-->Medio-Bassa
            #5-->Bassa
        #Anno di progettazione, categoria del ponte, luce complessiva
            #1--> Classe A
            #2--> Classe B
            #3--> Classe C
         # Presenza di sali mari marini o sali antigelo
             #1--> Presenti
             #2--> Non Presenti

       
V_2str = {(1,1,1): 1,
          (1,2,1): 1,
          (1,3,1): 1,
          (2,1,1): 1,
          (2,2,1): 1,
          (2,3,1): 2,
          (3,1,1): 2,
          (3,2,1): 2,
          (3,3,1): 3,
          (4,1,1): 3,
          (4,2,1): 3,
          (4,3,1): 4,
          (5,1,1): 5,
          (5,2,1): 5,
          (5,3,1): 5,
          
          (1,1,2): 1,
          (1,2,2): 1,
          (1,3,2): 1,
          (2,1,2): 1,
          (2,2,2): 2,
          (2,3,2): 3,
          (3,1,2): 2,
          (3,2,2): 3,
          (3,3,2): 4,
          (4,1,2): 3,
          (4,2,2): 4,
          (4,3,2): 5,
          (5,1,2): 5,
          (5,2,2): 5,
          (5,3,2): 5}

# for i in [1,2,3,4,5]:
#     for j in [1,2,3]:        
#         print('(V1  = ',i,' Norma = ',j,') --> V2str = ', V_2str[(i,j)])
    
    #Definizione Schema statico-Luce-Materiale [classe V4] (tab 4.6) attraverso la combinazione di 
        #Classe V3 {Schema statico + materiale} 
            #Unità materiale:
                #1-->C.a
                #2-->C.a.p.
                #3-->Acciaio
                #4-->Metallo (ponti storici)
                #5-->Legno
                #6-->Misto
                #7-->Muratura
            #Decine Schema statico:
                #1-->Travate appoggiate
                #2-->Travate continue/Telaio
                #3-->Arco massiccio
                #4-->Arco sottile
                #5-->Travate Gerber/ Ponti a stampella con travi tampone
                #6-->Soletta appoggiata
                #7-->Soletta incastrata
        #Luce max
            #1-->L<=5
            #2-->5<L<15
            #3-->15<L<25
            #4-->L>=25
            
V_4str = { (1,1,1): 4,
           (1,1,2): 3,
           (1,1,3): 2,
           (1,1,4): 1,
           (1,2,1): 4,
           (1,2,2): 3,
           (1,2,3): 3,
           (1,2,4): 2,
           (1,3,1): 5,
           (1,3,2): 4,
           (1,3,3): 3,
           (1,3,4): 2,
           (1,4,1):	4,
           (1,4,2): 3,
           (1,4,3):	2,
           (1,4,4):	1,
           (1,5,1):	3,
           (1,5,2):	2,
           (1,5,3):	1,
           (1,5,4):	1,
           (1,6,1):	4,
           (1,6,2):	3,
           (1,6,3):	2,
           (1,6,4):	1,
           (2,1,1):	5,
           (2,1,2):	4,
           (2,1,3):	3,
           (2,1,4):	2,
           (2,2,1):	5,
           (2,2,2):	4,
           (2,2,3):	3,
           (2,2,4):	3,
           (2,3,1):	5,
           (2,3,2): 5,
           (2,3,3): 4,
           (2,3,4): 3,
           (2,4,1): 5,
           (2,4,2): 4,
           (2,4,3): 3,
           (2,4,4): 2,
           (2,6,1): 5,
           (2,6,2): 4,
           (2,6,3): 3,
           (2,6,4): 2,
           (3,7,1): 5,
           (3,7,2): 4,
           (3,7,3): 4,
           (3,7,4): 3,
           (3,1,1): 5,
           (3,1,2): 4,
           (3,1,3): 3,
           (3,1,4): 3,
           (4,1,1): 4,
           (4,1,2): 3,
           (4,1,3): 3,
           (4,1,4): 2,
           (5,1,1): 2,
           (5,1,2): 1,
           (5,1,3): 1,
           (5,1,4): 1,
           (5,2,1): 2,
           (5,2,2): 2,
           (5,2,3): 2,
           (5,2,4): 1,
           (5,3,1): 3,
           (5,3,2): 2,
           (5,3,3): 2,
           (5,3,4): 1,
           (5,4,1): 2,
           (5,4,2): 2,
           (5,4,3): 1,
           (5,4,4): 1,
           (5,6,1): 2,
           (5,6,2): 1,
           (5,6,3): 1,
           (5,6,4): 1,
           (6,1,1): 4,
           (6,1,2): 3,
           (6,1,3): 2,
           (6,1,4): 1,
           (7,1,1): 5,
           (7,1,2): 4,
           (7,1,3): 3,
           (7,1,4): 2}


# for i in [11,12,13,14,15,16,21,22,23,24,26,37,31,41,51,52,53,54,56,61,71]:
#     for j in [1,2,3,4]:        
#         print('(V3  = ',i,' lucemax = ',j,') --> V_4str = ', V_4str[(i,j)])

    #Definizione Classe di vulnerabilità 0 (tab4.2) attraverso la combinazione di
        #n° campate
            #1--> maggiore di 3
            #2--> minore o uguale di 3
        #Classe V4
            #1-->Alta
            #2-->Medio-Alta
            #3-->Media
            #4-->Medio-Bassa
            #5-->Bassa
            
V_5str= {   (1, 1):	1,
            (1,	2):	1,
            (1,	3): 2,
            (1,	4):	3,
            (1,	5):	4,
            (2,	1):	1,
            (2,	2):	2,
            (2,	3):	3,
            (2,	4):	4,
            (2,	5):	5}

#Classe di esposizione strutturale
    #Definizione di Livello di TGM e luce media campata [Classe E1_0] (tab4.8) combianndo 
        #TGM (tab4.7) 
            #1-->Alta >=25000 veicoli/giorno
            #2-->Media 10000<veicoli/giorno<25000
            #3-->Bassa <=10000 veicoli/giorno
        #luce media
            #1-->Grande luce: Lm >50m
            #2-->Media luce: 20m<Lm<=50m
            #3-->Piccola luce Lm<=20m


    #Definizione Classe di vulnerabilità combinando 
        #Classe V5
            #1-->Alta
            #2-->Medio-Alta
            #3-->Media
            #4-->Medio-Bassa
            #5-->Bassa
        #Classe V2
            #1-->Alta
            #2-->Medio-Alta
            #3-->Media
            #4-->Medio-Bassa
            #5-->Bassa
V_str = {   (1,	1):	1,
            (1,	2):	1,
            (1,	3): 2,
            (1,	4):	2,
            (1,	5):	3,
            (2,	1):	2,
            (2,	2):	2,
            (2,	3):	2,
            (2,	4):	3,
            (2,	5):	3,
            (3,	1):	2,
            (3,	2):	2,
            (3,	3):	3,
            (3,	4):	3,
            (3,	5):	4,
            (4,	1):	3,
            (4,	2):	3,
            (4,	3):	4,
            (4,	4):	4,
            (4,	5):	5,
            (5,	1):	4,
            (5,	2):	4,
            (5,	3):	5,
            (5,	4):	5,
            (5,	5):	5}

#---- 1.3 Classe di Esposizione strutturale
    #Definizione di Livello di TGM e luce media campata [Classe E1_0] (tab4.8) combianndo 
        #TGM (tab4.7) 
            #1-->Alta >=25000 veicoli/giorno
            #2-->Media 10000<veicoli/giorno<25000
            #3-->Bassa <=10000 veicoli/giorno
        #luce media
            #1-->Grande luce: Lm >50m
            #2-->Media luce: 20m<Lm<=50m
            #3-->Piccola luce Lm<=20m

E_1_0str = {   (1,	1):	1,
            (2,	1):	2,
            (3,	1): 3,
            (1,	2):	2,
            (2,	2):	3,
            (3,	2):	4,
            (1,	3):	3,
            (2,	3):	4,
            (3,	3):	5,
            }

# for i in [1,2,3]:
#     for j in [1,2,3]:        
#         print('(TGM  = ',i,' Luce media = ',j,') --> E_1_0str = ',E_1_0str[(i,j)])
        
    #Definizione Classe E1 combinando 
        #Frequente passaggio di persone 
            #1--> si
            #2--> no
        #Classe E1_0
            #1-->Alta
            #2-->Medio-Alta
            #3-->Media
            #4-->Medio-Bassa
            #5-->Bassa
            
E_1str = { (1,	1):	1,
          (1,	2):	1,
          (1,	3):	2,
          (1,	4):	3,
          (1,	5):	4,
          (2,	1):	1,
          (2,	2):	2,
          (2,	3):	3,
          (2,	4):	4,
          (2,	5):	5}

# for i in [1,2]:
#     for j in [1,2,3,4,5]:        
#         print('(Persone  = ',i,' E_1_0 = ',j,') --> E_1str = ',E_1str [(i,j)])       

    #Definizione Classe E2 (tab4.3) combinando 
    #Alternative stradali
        #1-->Assenza
        #2-->Presenza
    #Classe E1        
        #1-->Alta
        #2-->Medio-Alta
        #3-->Media
        #4-->Medio-Bassa
        #5-->Bassa
E_2str = {(1,	1):	1,
          (1,	2):	1,
          (1,	3):	2,
          (1,	4):	3,
          (1,	5):	4,
          (2,	1):	1,
          (2,	2):	2,
          (2,	3):	3,
          (2,	4):	4,
          (2,	5):	5}

# for i in [1,2]:
#     for j in [1,2,3,4,5]:        
#         print('(altstradali  = ',i,' E1 = ',j,') --> E_2 = ',E_2[(i,j)])  

    #Definizione Classe di esposizione 0 (tab4.3)combinando 
       #Classe E2 
            #1-->Alta
            #2-->Medio-Alta
            #3-->Media
            #4-->Medio-Bassa
            #5-->Bassa           
       #Tipologia di ente scavalcato (tab 4.9)
            #1-->Alta
            #2-->Media
            #3-->Bassa
E_str = {   (1,	1):	1,
            (1,	2):	1,
            (1,	3):	2,
            (2,	1):	1,
            (2,	2):	2,
            (2,	3):	3,
            (3,	1):	2,
            (3,	2):	3,
            (3,	3): 4,
            (4,	1):	3,
            (4,	2):	4,
            (4,	3):	5,
            (5,	1):	4,
            (5,	2):	5,
            (5,	3):	5}

# for i in [1,2,3,4,5]:
#     for j in [1,2,3]:        
#         print('(E2  = ',i,' scavalc = ',j,') --> E_str = ',E_str_0[(i,j)])  

    #Definizione Classe di esposizione combiando 
    #Classe di esposizione 0 
         #1-->Alta
         #2-->Medio-Alta
         #3-->Media
         #4-->Medio-Bassa
         #5-->Bassa  
    #Trasporto merci pericolose
         #1--> si saltuariamente
         #2--> si
         #3--> no    
# E_str = {   (1,	1):	1,
#             (2,	1):	2,
#             (3,	1):	3.1,
#             (4,	1):	4.1,
#             (5,	1):	5.1,
#             (1,	2):	1,
#             (2,	2):	1,
#             (3,	2):	2,
#             (4,	2):	3,
#             (5,	2):	4,
#             (1,	3):	1,
#             (2,	3):	2,
#             (3,	3):	3,
#             (4,	3):	4,
#             (5,	3):	5,

#                }
#---- ------------------------------------
#---- Calcolo Classe di Attenzione strutturale e fondazionale
Tabella_CdA ={  (1,	1,	1):	1,
                (1,	1,	2):	1,
                (1,	1,	3):	1,
                (1,	1,	4):	1,
                (1,	1,	5):	1,
                (1,	2,	1):	1,
                (1,	2,	2):	1,
                (1,	2,	3):	2,
                (1,	2,	4):	2,
                (1,	2,	5):	2,
                (1,	3,	1):	1,
                (1,	3,	2):	2,
                (1,	3,	3):	2,
                (1,	3,	4):	3,
                (1,	3,	5):	3,
                (1,	4,	1):	2,
                (1,	4,	2):	3,
                (1,	4,	3):	3,
                (1,	4,	4):	3,
                (1,	4,	5):	3,
                (1,	5,	1):	2,
                (1,	5,	2):	3,
                (1,	5,	3):	3,
                (1,	5,	4):	4,
                (1,	5,	5):	4,
                (2,	1,	1):	1,
                (2,	1,	2):	1,
                (2,	1,	3):	1,
                (2,	1,	4):	1,
                (2,	1,	5):	1,
                (2,	2,	1):	1,
                (2,	2,	2):	2,
                (2,	2,	3):	2,
                (2,	2,	4):	2,
                (2,	2,	5):	3,
                (2,	3,	1):	2,
                (2,	3,	2):	2,
                (2,	3,	3):	3,
                (2,	3,	4):	3,
                (2,	3,	5):	3,
                (2,	4,	1):	3,
                (2,	4,	2):	3,
                (2,	4,	3):	3,
                (2,	4,	4):	4,
                (2,	4,	5):	4,
                (2,	5,	1):	3,
                (2,	5,	2):	3,
                (2,	5,	3):	4,
                (2,	5,	4):	4,
                (2,	5,	5):	5,
                (3,	1,	1):	1,
                (3,	1,	2):	1,
                (3,	1,	3):	1,
                (3,	1,	4):	1,
                (3,	1,	5):	1,
                (3,	2,	1):	2,
                (3,	2,	2):	2,
                (3,	2,	3):	2,
                (3,	2,	4):	3,
                (3,	2,	5):	3,
                (3,	3,	1):	2,
                (3,	3,	2):	3,
                (3,	3,	3):	3,
                (3,	3,	4):	3,
                (3,	3,	5): 3,
                (3,	4,	1):	3,
                (3,	4,	2):	3,
                (3,	4,	3):	3,
                (3,	4,	4):	4,
                (3,	4,	5):	4,
                (3,	5,	1):	3,
                (3,	5,	2):	3,
                (3,	5,	3):	4,
                (3,	5,	4):	5,
                (3,	5,	5):	5,
                (4,	1,	1):	1,
                (4,	1,	2):	1,
                (4,	1,	3):	1,
                (4,	1,	4):	1,
                (4,	1,	5):	1,
                (4,	2,	1):	2,
                (4,	2,	2):	2,
                (4,	2,	3):	3,
                (4,	2,	4):	3,
                (4,	2,	5):	3,
                (4,	3,	1):	2,
                (4,	3,	2):	3,
                (4,	3,	3):	3,
                (4,	3,	4):	4,
                (4,	3,	5):	4,
                (4,	4,	1):	3,
                (4,	4,	2):	3,
                (4,	4,	3):	4,
                (4,	4,	4):	4,
                (4,	4,	5):	5,
                (4,	5,	1):	3,
                (4,	5,	2):	4,
                (4,	5,	3):	4,
                (4,	5,	4):	5,
                (4,	5,	5):	5,
                (5,	1,	1):	1,
                (5,	1,	2):	1,
                (5,	1,	3):	1,
                (5,	1,	4):	1,
                (5,	1,	5):	1,
                (5,	2,	1):	2,
                (5,	2,	2):	3,
                (5,	2,	3):	3,
                (5,	2,	4):	3,
                (5,	2,	5):	4,
                (5,	3,	1):	3,
                (5,	3,	2):	3,
                (5,	3,	3):	3,
                (5,	3,	4):	4,
                (5,	3,	5):	5,
                (5,	4,	1):	3,
                (5,	4,	2):	3,
                (5,	4,	3):	4,
                (5,	4,	4):	5,
                (5,	4,	5):	5,
                (5,	5,	1):	4,
                (5,	5,	2):	4,
                (5,	5,	3):	5,
                (5,	5,	4):	5,
                (5,	5,	5): 5}

#---- 2 ------------------------------------               
#---- Valutazione CdA Sismica
#---- ------------------------------------
#---- 2.1 Classe di Pericolosità sismica
    #Definizione Ag,Ti [Classe P1] (tab 4.12) combinando:
        #Ag con probabilità di eccedenza del 10% in 50 anni riferita a suoli rigidi
            #1-->ag>=0.25g
            #2-->0.15<ag<0.25
            #3-->0.10<ag<0.15
            #4-->0.05<ag<0.10
            #5-->ag<0.05g
        #Categoria topografica Ti
            #1--> T1 ,T2, T3
            #2--> T4
P_1sism = { (1,	1):	1,
            (2,	1):	2,
            (3,	1):	3,
            (4,	1):	4,
            (5,	1):	5,
            (1,	2):	1,
            (2,	2):	1,
            (3,	2):	2,
            (4,	2):	3,
            (5,	2):	4,}

    #Classe di pericolosità (tab 4.4) combiando
        #Classe P1
            #1-->Alta
            #2-->Medio-Alta
            #3-->Media
            #4-->Medio-Bassa
            #5-->Bassa           
        #Categoria di sottosuolo
            #1--> A-B
            #2--> C-D-E
P_sism = {  (1,	1):	1,
            (1,	2):	1,
            (2,	1):	2,
            (2,	2):	1,
            (3,	1):	3,
            (3,	2):	2,
            (4,	1):	4,
            (4,	2):	3,
            (5,	1):	5,
            (5,	2):	4,}

#---- 2.2 Classe di Vulnerabilità sismica
#Classe di Vulnerabilità sismica
    #Definizione Schema strutturale,luce,materiale [Classe V2_0] (tab 4.13)combinando:
        #Schema strutturale+materiale [Classe V1]
            #Unità schema statico
               #1--> Schema isostatico
               #2--> Schema iperstatico
            #Decine materiale:
                #1-->C.a
                #2-->C.a.p.
                #7-->Muratura
                #3-->Acciaio
        #Luce
            #1--> L medio-piccola
            #2--> L elevata
        #N° campate
            #1--> Singola campata
            #2--> Multi campata
V_2_0_sism = {  (1, 1,	1,	1):	3, #(mat, schema statico, luce, n_campate) : classe (1 alta...)
                (1, 1,	1,	2):	2,
                (1, 1,	2,	1):	2,
                (1, 1,	2,	2):	1,
                (1, 2,	1,	1):	5,
                (1, 2,	1,	2):	4,
                (1, 2,	2,	1):	4,
                (1, 2,	2,	2):	3,
                (2, 1,	1,	1):	3,
                (2, 1,	1,	2):	2,
                (2, 1,	2,	1):	2,
                (2, 1,	2,	2):	1,
                (2, 2,	1,	2):	4,
                (2, 2,	2,	2):	3,
                (7, 2,	1,	1):	5,
                (7, 2,	1,	2):	4,
                (7, 2,	2,	1):	4,
                (7, 2,	2,	2):	3,
                (3, 1,	1,	1):	4,
                (3, 1,	1,	2):	3,
                (3, 1,	2,	1):	4,
                (3, 1,	2,	2):	3,
                (3, 2,	1,	1):	5,
                (3, 2,	1,	2):	4,
                (3, 2,	2,	1):	5,
                (3, 2,	2,	2):	4,}

    #Definizione Classe V2 combinando
        #Classe V2_0
            #1-->Alta
            #2-->Medio-Alta
            #3-->Media
            #4-->Medio-Bassa
            #5-->Bassa 
        #Elementi di vulnerabilità pg 24 LG20
            #1-->Presenza
            #2-->Assenza
V_2_sism={  (1,	1):	1,
            (2,	1):	1,
            (3,	1):	2,
            (4,	1):	3,
            (5,	1):	4,
            (1,	2):	1,
            (2,	2):	2,
            (3,	2):	3,
            (4,	2):	4,
            (5,	2):	5,}

    #Definizione Criteri di progettazione [Classe V3] (fig 4.5) combinando
        #Classe V2
            #1-->Alta
            #2-->Medio-Alta
            #3-->Media
            #4-->Medio-Bassa
            #5-->Bassa 
        #Criteri di progettazione
            #1-->Sismici
            #2-->Non sismici
V_3_sism={  (1,	2):	1,
            (2,	2):	1,
            (3,	2):	2,
            (4,	2):	3,
            (5,	2):	4,
            (1,	1):	1,
            (2,	1):	2,
            (3,	1):	3,
            (4,	1):	4,
            (5,	1):	5,}
    #Definizione Classe di Vulnerabilità sismica (fig 4.5)
        #Classe V3
            #1-->Alta
            #2-->Medio-Alta
            #3-->Media
            #4-->Medio-Bassa
            #5-->Bassa 
        #Livello di difettosità (tab4.14)
            #1-->Alta
            #2-->Medio-Alta
            #3-->Media
            #4-->Medio-Bassa
            #5-->Bassa 
V_sism={    (1,	1):	1,
            (1,	2):	1,
            (1,	3):	2,
            (1,	4):	2,
            (1,	5):	3,
            (2,	1):	1,
            (2,	2):	2,
            (2,	3):	2,
            (2,	4):	3,
            (2,	5):	4,
            (3,	1):	1,
            (3,	2):	2,
            (3,	3):	3,
            (3,	4):	3,
            (3,	5):	4,
            (4,	1):	1,
            (4,	2):	3,
            (4,	3):	3,
            (4,	4):	4,
            (4,	5):	4,
            (5,	1):	2,
            (5,	2):	3,
            (5,	3):	4,
            (5,	4):	5,
            (5,	5):	5,}


#---- 2.3 Classe di Esposizione sismica
#Classe di esposizione sismica (tab4.6) combinando
    #Classe di esposizione strutturale e fondazionale
            #1-->Alta
            #2-->Medio-Alta
            #3-->Media
            #4-->Medio-Bassa
            #5-->Bassa 
    #Strategicità dell'opera
            #1-->Strategica
            #2-->Non strategica   
E_sism={    (1,	1):	1,
            (2,	1):	1,
            (3,	1):	2,
            (4,	1):	3,
            (5,	1):	4,
            (1,	2):	1,
            (2,	2):	2,
            (3,	2):	3,
            (4,	2):	4,
            (5,	2):	5,}


#---- Dizionari dei parametri dipendenti da altri parametri

schema_statico = { 1 :  (1, 1),  # trave appoggiata: (trave app, iso)
                   2 :  (2, 2),  # trave continua:   (trave con, iper)
                   3 :  (3, 2),  # arco massiccio: (arco mass, iper)
                   41 : (4, 1),  # arco sottile: (arco sott, iso)
                   42 : (4, 2),  # arco sottile: (arco sott, iper)
                   5 : (5, 1),  # trave gerber: (trave ger, iso)
                   6 : (6, 1),  # soletta appoggiata: (sole app, iso)
                   7 : (7, 2),  # soletta incastrata: (sol inc, iper)
                   }

Tabella_CdA_fra=   {(1, 1,	1):	1,
                    (1,	2,	1):	1,
                    (1,	3,	1):	1,
                    (1,	4,	1):	2,
                    (1,	5,	1):	2,
                    (1,	1,	2):	1,
                    (1,	2,	2):	1,
                    (1,	3,	2):	2,
                    (1,	4,	2):	2,
                    (1,	5,	2):	2,
                    (1,	1,	3):	1,
                    (1,	2,	3):	2,
                    (1,	3,	3):	2,
                    (1,	4,	3):	2,
                    (1,	5,	3):	2,
                    (1,	1,	4):	2,
                    (1,	2,	4):	2,
                    (1,	3,	4):	2,
                    (1,	4,	4):	2,
                    (1,	5,	4):	3,
                    (1,	1,	5):	2,
                    (1,	2,	5):	2,
                    (1,	3,	5):	2,
                    (1,	4,	5):	3,
                    (1,	5,	5):	3,
                    
                    (2,	1,	1):	1,
                    (2,	2,	1):	2,
                    (2,	3,	1):	2,
                    (2,	4,	1):	2,
                    (2,	5,	1):	2,
                    (2,	1,	2):	2,
                    (2,	2,	2):	2,
                    (2,	3,	2):	2,
                    (2,	4,	2):	2,
                    (2,	5,	2):	3,
                    (2,	1,	3):	2,
                    (2,	2,	3):	2,
                    (2,	3,	3):	2,
                    (2,	4,	3):	3,
                    (2,	5,	3):	3,
                    (2,	1,	4):	2,
                    (2,	2,	4):	2,
                    (2,	3,	4):	3,
                    (2,	4,	4):	3,
                    (2,	5,	4):	3,
                    (2,	1,	5):	2,
                    (2,	2,	5):	3,
                    (2,	3,	5):	3,
                    (2,	4,	5):	3,
                    (2,	5,	5):	3,
                    
                    (3,	1,	1):	2,
                    (3,	2,	1):	2,
                    (3,	3,	1):	2,
                    (3,	4,	1):	3,
                    (3,	5,	1):	3,
                    (3,	1,	2):	2,
                    (3,	2,	2):	2,
                    (3,	3,	2):	3,
                    (3,	4,	2):	3,
                    (3,	5,	2):	3,
                    (3,	1,	3):	2,
                    (3,	2,	3):	3,
                    (3,	3,	3):	3,
                    (3,	4,	3):	3,
                    (3,	5,	3):	3,
                    (3,	1,	4):	3,
                    (3,	2,	4):	3,
                    (3,	3,	4):	3,
                    (3,	4,	4):	3,
                    (3,	5,	4):	4,
                    (3,	1,	5):	3,
                    (3,	2,	5):	3,
                    (3,	3,	5):	3,
                    (3,	4,	5):	4,
                    (3,	5,	5):	4,
                    
                    (4,	1,	1):	2,
                    (4,	2,	1):	3,
                    (4,	3,	1):	3,
                    (4,	4,	1):	3,
                    (4,	5,	1):	3,
                    (4,	1,	2):	3,
                    (4,	2,	2):	3,
                    (4,	3,	2):	3,
                    (4,	4,	2):	3,
                    (4,	5,	2):	4,
                    (4,	1,	3):	3,
                    (4,	2,	3):	3,
                    (4,	3,	3):	3,
                    (4,	4,	3):	4,
                    (4,	5,	3):	4,
                    (4,	1,	4):	3,
                    (4,	2,	4):	3,
                    (4,	3,	4):	4,
                    (4,	4,	4):	4,
                    (4,	5,	4):	4,
                    (4,	1,	5):	3,
                    (4,	2,	5):	4,
                    (4,	3,	5):	4,
                    (4,	4,	5):	4,
                    (4,	5,	5):	4,
                    
                    (5,	1,	1):	3,
                    (5,	2,	1):	3,
                    (5,	3,	1):	3,
                    (5,	4,	1):	4,
                    (5,	5,	1):	4,
                    (5,	1,	2):	3,
                    (5,	2,	2):	3,
                    (5,	3,	2):	4,
                    (5,	4,	2):	4,
                    (5,	5,	2):	4,
                    (5,	1,	3):	3,
                    (5,	2,	3):	3,
                    (5,	3,	3):	4,
                    (5,	4,	3):	4,
                    (5,	5,	3):	4,
                    (5,	1,	4):	4,
                    (5,	2,	4):	4,
                    (5,	3,	4):	4,
                    (5,	4,	4):	4,
                    (5,	5,	4):	5,
                    (5,	1,	5):	4,
                    (5,	2,	5):	4,
                    (5,	3,	5):	4,
                    (5,	4,	5):	5,
                    (5,	5,	5):	5,}


vuln_fr =    {(1, 1) : 1,
              (2, 1) : 1,
              (3, 1) : 2,
              (4, 1) : 3,
              (5, 1) : 4,
              (1, 2) : 1,
              (2, 2) : 2,
              (3, 2) : 3,
              (4, 2) : 4,
              (5, 2) : 5,
              (1, 3) : 2,
              (2, 3) : 3,
              (3, 3) : 4,
              (4, 3) : 5,
              (5, 3) : 5,}


S_fr_inst_vers = {( 1, 1, 1 ) : 1,   #prima key riferità al parametro di attività 
                  ( 1, 2, 1 ) : 1,   #seconda key riferita la parametro di velocità
                  ( 1, 3, 1 ) : 1,   #terzaa key riferita la parametro di magnitudo
                  ( 1, 4, 1 ) : 1,
                  ( 1, 5, 1 ) : 1,
                  ( 2, 1, 1 ) : 1,
                  ( 2, 2, 1 ) : 1,
                  ( 2, 3, 1 ) : 1,
                  ( 2, 4, 1 ) : 1,
                  ( 2, 5, 1 ) : 2,
                  ( 3, 1, 1 ) : 1,
                  ( 3, 2, 1 ) : 1,
                  ( 3, 3, 1 ) : 2,
                  ( 3, 4, 1 ) : 2,
                  ( 3, 5, 1 ) : 2,
                  ( 1, 1, 2 ) : 1,
                  ( 1, 1, 3 ) : 2,
                  ( 1, 1, 4 ) : 2,
                  ( 1, 1, 5 ) : 3,
                  ( 2, 1, 2 ) : 1,
                  ( 2, 1, 3 ) : 2,
                  ( 2, 1, 4 ) : 3,
                  ( 2, 1, 5 ) : 4,
                  ( 3, 1, 2 ) : 2,
                  ( 3, 1, 3 ) : 3,
                  ( 3, 1, 4 ) : 3,
                  ( 3, 1, 5 ) : 4,
                  ( 1, 2, 2 ) : 1,
                  ( 1, 2, 3 ) : 2,
                  ( 1, 2, 4 ) : 3,
                  ( 1, 2, 5 ) : 3,
                  ( 2, 2, 2 ) : 2,
                  ( 2, 2, 3 ) : 2,
                  ( 2, 2, 4 ) : 3,
                  ( 2, 2, 5 ) : 4,
                  ( 3, 2, 2 ) : 2,
                  ( 3, 2, 3 ) : 3,
                  ( 3, 2, 4 ) : 4,
                  ( 3, 2, 5 ) : 4,
                  ( 1, 3, 2 ) : 1,
                  ( 1, 3, 3 ) : 2,
                  ( 1, 3, 4 ) : 3,
                  ( 1, 3, 5 ) : 4,
                  ( 2, 3, 2 ) : 2,
                  ( 2, 3, 3 ) : 3,
                  ( 2, 3, 4 ) : 3,
                  ( 2, 3, 5 ) : 4,
                  ( 3, 3, 2 ) : 2,
                  ( 3, 3, 3 ) : 3,
                  ( 3, 3, 4 ) : 4,
                  ( 3, 3, 5 ) : 5,
                  ( 1, 4, 2 ) : 2,
                  ( 1, 4, 3 ) : 2,
                  ( 1, 4, 4 ) : 3,
                  ( 1, 4, 5 ) : 4,
                  ( 2, 4, 2 ) : 2,
                  ( 2, 4, 3 ) : 3,
                  ( 2, 4, 4 ) : 4,
                  ( 2, 4, 5 ) : 4,
                  ( 3, 4, 2 ) : 3,
                  ( 3, 4, 3 ) : 3,
                  ( 3, 4, 4 ) : 4,
                  ( 3, 4, 5 ) : 5,
                  ( 1, 5, 2 ) : 2,
                  ( 1, 5, 3 ) : 3,
                  ( 1, 5, 4 ) : 3,
                  ( 1, 5, 5 ) : 4,
                  ( 2, 5, 2 ) : 2,
                  ( 2, 5, 3 ) : 3,
                  ( 2, 5, 4 ) : 4,
                  ( 2, 5, 5 ) : 5,
                  ( 3, 5, 2 ) : 3,
                  ( 3, 5, 3 ) : 4,
                  ( 3, 5, 4 ) : 4,
                  ( 3, 5, 5 ) : 5}


#Classe di Suscettibilità Frane
#Combinazione attraverso la figura 4.7 di: 
    #Instabilità di versante (tab 4.17) 
        #1-->Alta
        #2-->Medio-Alta
        #3-->Media
        #4-->Medio-Bassa
        #5-->Bassa
    #Affidabilità della Valutazione 
        #1-->Limitata
        #2-->Buona
               
s_01 = {    (1,1) : 1,
            (2,1) : 1,
            (3,1) : 2,
            (4,1) : 3,
            (5,1) : 4,
            (1,2) : 1,
            (2,2) : 2,
            (3,2) : 3,
            (4,2) : 4,
            (5,2) : 5}

# #Combinazione attraverso la figura 4.7 di: 
    
#     #Misure di mitigazione 
#         #1-->Assenti
#         #2-->Monitorato
#         #3-->Stabilizzato
#    #P_fr_01
#             #1-->Alta
#             #2-->Medio-Alta
#             #3-->Media
#             #4-->Medio-Bassa
#             #5-->Bassa
        
s_02 = { (1,1) : 1,
            (2,1) : 1,
            (3,1) : 2,
            (4,1) : 3,
            (5,1) : 4,
            (1,2) : 1,
            (2,2) : 2,
            (3,2) : 3,
            (4,2) : 4,
            (5,2) : 5,
            (1,3) : 2,
            (2,3) : 3,
            (3,3) : 4,
            (4,3) : 4,
            (5,3) : 5}



               