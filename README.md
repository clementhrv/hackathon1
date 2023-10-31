
# hackathon1
sujet sur les exoplanètes : 
idées à développer : filtrer les donénes et définir les critères qui permettent de comparer à la Terre
On va calculer un pourcentage de ressemblance en ce basant sur la Terre 

Deuxième idée : utliser les planètes définis comme habitables sur le site de la NASA et comparer aux résultats obtenus en utlisant les mêmes critères mais également avec d'autres
but final: réduire au maximum le nombre de planètes en utilisant des critères d'ordre scientifique 

Répartition des taches : plusieurs filtres à faire -> filtrer pour uniquement les planètes dont les données sont présentes, période d'ensolliement, période, température...
                         choisir les données exactement
                         pondérer les critères pour le pourcentage 



### SCHEMA TRAVAIL

```python
    
       Alban # établit les critères d'habitabilité
   _______/______
  /             \   
 /               \
Clément        Antoine #Clément extrait+fusionne les données, 
\                 /     #Antoine les pondère
 \               / 
  \_____________/
        /
      Paul   #Code un filtre sur chaque critère qui donne un critère score
       |
       |
       |
  Tout le monde #on code un filtre global qui les prend tous en compte pondérés et donne un pourcentage ou un score à chaque planère
```
