import pandas as pd 
import numpy as np 

#importation de la data avec toutes les données
df1 = pd.read_csv('toute_planetes.csv', skiprows=291)

#imoortation de la data avec les planètes habitables
df2 = pd.read_csv('cumulative_2023.10.31_07.12.57.csv', skiprows=90)

print(df2)

columns = ['Planet Name','Host Name', 'Defaull Parameter Set', 'Number of Stars',]


