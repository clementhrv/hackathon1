import pandas as pd 
import numpy as np 

#importation de la data avec toutes les données
df1 = pd.read_csv('git-sandbox/PS_2023.10.31_08.27.48.csv.csv', skiprows=96)

#imoortation de la data avec les planètes habitables
df2 = pd.read_csv('cumulative_2023.10.31_07.12.57.csv', skiprows=90)




columns1 = ['Planet Name','Host Name', 'Default Parameter Set', 'Number of Stars','Number of Planets','Discovery Method','Discovery Year','Solution Type','Controversial Flag','Planetary Parameter Reference','Orbital Period','Orbit Semi-Major Axis','Planet Radius [Earth Radius]','Planet Radius [Jupiter Radius]','Planet Mass or Mass*sin(i) [Earth Mass]','Planet Mass or Mass*sin(i) [Jupiter Mass]','Planet Mass or Mass*sin(i) Provenance','Eccentricity','Insolation Flux','Equilibrium Temperature','Data Show Transit Timing Variations','Stellar Parameter Reference','Spectral Type','Stellar Effective Temperature','Stellar Radius ','Stellar Mass','Stellar Metallicity','Stellar Metallicity Ratio','Stellar Surface Gravity']


columns1_inutiles = []

#df1.columns=columns1

print(df1)
"""
df1 = df1.set_index('Planet Name')

#df1.drop(columns = [''])

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