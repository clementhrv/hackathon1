import pandas as pd 
import numpy as np 

#importation de la data avec toutes les données
df1 = pd.read_csv('toute_planetes.csv', skiprows=291)

#imoortation de la data avec les planètes habitables
df2 = pd.read_csv('cumulative_2023.10.31_07.12.57.csv', skiprows=90)


​
Clement HERVE
​
columns1 = ['Planet Name','Host Name', 'Default Parameter Set', 'Number of Stars','Number of Planets','Discovery Method','Discovery Year','Solution Type','Controversial Flag','Planetary Parameter Reference','Orbital Period','Orbit Semi-Major Axis','Planet Radius [Earth Radius]','Planet Radius [Jupiter Radius]','Planet Mass or Mass*sin(i) [Earth Mass]','Planet Mass or Mass*sin(i) [Jupiter Mass]','Planet Mass or Mass*sin(i) Provenance','Eccentricity','Insolation Flux','Equilibrium Temperature','Data Show Transit Timing Variations','Stellar Parameter Reference','Spectral Type','Stellar Effective Temperature','Stellar Radius ','Stellar Mass','Stellar Metallicity','Stellar Metallicity Ratio','Stellar Surface Gravity','System Parameter Reference','RA','Dec','Distance','V Magnitude','Ks Magnitude','Gaia Magnitude','Date of last Update','Planetary Parameter Reference Publication Date','Release Date']
columns1_inutiles = []


df1 = df1.set_index('Planete Name')

#df1.drop(columns = [''])

#suppression des lignes sans données utiles
df1 = df1[df1['Insolation Flux [Earth Flux]'].notna()]
df1 = df1[df1['Equilibrium Temperature [K]'].notna()]

#filtre pour la température
df1 = df1[df1['Equilibrium Temperature [K]']<353]
df1 = df1[df1['Equilibrium Temperature [K]']>0]
df1['temp_prc'] = df1['']