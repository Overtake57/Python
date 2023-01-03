'''
TriSelection [Difficile]

Nous allons écrire une procédure de tri. Le traitement consiste à :
 — rechercher le plus petit élément du tableau, et l’échanger avec l’élément d’indice 0 ;
 — rechercher le second plus petit élément du tableau, et l’échanger avec l’élément d’indice 1 ;
 — continuer de cette façon jusqu’à ce que le tableau soit entièrement trié.
 
 '''

import random
 
def tri_insertion(liste):
    memoListe = list(liste) # copie de la liste
    indice = len(memoListe)
    for n in range(1,indice):
        key = memoListe[n]
        j = n-1
        while j>=0 and memoListe[j] > key:
            memoListe[j+1] = memoListe[j] # decalage
            j = j-1
        memoListe[j+1] = key
    return memoListe
    
liste = []
for k in range(6):
    liste.append(random.randint(0,10))
liste_triee = tri_insertion(liste)

print(liste)
print(liste_triee)

