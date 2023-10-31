import pandas as pd 
import numpy as np 

#importation de la data avec toutes les données
df1 = pd.read_csv('toute_planetes.csv', skiprows=291)

#imoortation de la data avec les planètes habitables
df2 = pd.read_csv('cumulative_2023.10.31_07.12.57.csv', skiprows=90)

columns1 = ['Planet Name','Host Name', 'Defaull Parameter Set', 'Number of Stars',]

df1 = df1.set_index('Planete Name')

df1.drop(columns = [''])

#suppression des lignes sans données utiles
df1 = df1[df1['Insolation Flux [Earth Flux]'].notna()]
df1 = df1[df1['Equilibrium Temperature [K]'].notna()]
