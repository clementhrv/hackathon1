import pandas as pd 
import numpy as np 

#importation de la data avec toutes les données
df1 = pd.read_csv('PS_2023.10.31_08.27.48.csv', skiprows=96)

#imoortation de la data avec les planètes habitables
df2 = pd.read_csv('cumulative_2023.10.31_07.12.57.csv', skiprows=96)




columns1 = ['Planet Name','Host Name', 'Default Parameter Set', 'Number of Stars','Number of Planets','Discovery Method','Discovery Year','Solution Type','Controversial Flag','Planetary Parameter Reference','Orbital Period','Orbit Semi-Major Axis','Planet Radius [Earth Radius]','Planet Radius [Jupiter Radius]','Planet Mass or Mass*sin(i) [Earth Mass]','Planet Mass or Mass*sin(i) [Jupiter Mass]','Planet Mass or Mass*sin(i) Provenance','Eccentricity','Insolation Flux','Equilibrium Temperature','Data Show Transit Timing Variations','Stellar Parameter Reference','Spectral Type','Stellar Effective Temperature','Stellar Radius ','Stellar Mass','Stellar Metallicity','Stellar Metallicity Ratio','Stellar Surface Gravity']


columns1_inutiles = [ 'pl_orbpererr1',
       'pl_orbpererr2',  'pl_orbsmaxerr1',
       'pl_orbsmaxerr2',  'pl_radeerr1',
       'pl_radeerr2',  'pl_radjerr1', 'pl_radjerr2',
         'pl_bmasseerr1', 'pl_bmasseerr2',
        'pl_bmassjerr1', 'pl_bmassjerr2',
         'pl_orbeccenerr1',
       'pl_orbeccenerr2', 'pl_insolerr1',
       'pl_insolerr2',  'pl_eqterr1', 'pl_eqterr2',
       'st_tefferr1', 'st_tefferr2', 'st_raderr1',
       'st_raderr2', 'st_masserr1', 'st_masserr2',
       'st_meterr1', 'st_meterr2',  'st_loggerr1', 'st_loggerr2',  'sy_disterr1',
       'sy_disterr2', 'sy_vmag', 'sy_vmagerr1', 'sy_vmagerr2', 'sy_kmag',
       'sy_kmagerr1', 'sy_kmagerr2',  'sy_gaiamagerr1',
       'sy_gaiamagerr2' ]

c2_i = ['pl_orbperlim',
        'pl_orbsmaxlim',  'pl_radelim', 
       'pl_radjlim',  'pl_bmasselim',  'pl_bmassjlim',
        'pl_orbeccenlim', 
       'pl_insollim',  'pl_eqtlim', 'st_tefflim', 'st_radlim',
        'st_masslim',  'st_metlim', 'st_logglim', ]

df1.set_index('pl_name', inplace = True)

df1.drop(axis=1 , labels= columns1_inutiles, inplace = True)
df1.drop(axis=1 , labels= c2_i, inplace = True)
print(df1)
print(df1.columns)

df1 = df1[df1['pl_eqt'].notna()]
print(df1['pl_eqt'])
df1 = df1[df1['pl_insol'].notna()]
print(df1)
print(df1["pl_insol"])
#pour aboutir à la fin du projet il faut récupérer les bons noms dans df1.columns pour les colonnes voulue
#pour ensuite appliquer les filtres puis ensuite calculer les scores




"""
#suppression des lignes sans données utiles
df1 = df1[df1['Insolation Flux [Earth Flux]'].notna()]
df1 = df1[df1['Equilibrium Temperature [K]'].notna()]

#filtre pour la température
df1 = df1[df1['Equilibrium Temperature [K]']<353]
df1 = df1[df1['Equilibrium Temperature [K]']>0]
#df1 = df1[293<df1['Equilibrium Temperature [K]']<353]
#df = df[0.1>df['Eccentricity']>0.067]
#df =df[10>df ['Planet Mass Mass*sin(i)']>1]
df1['temp_prc'] = df1['']"""