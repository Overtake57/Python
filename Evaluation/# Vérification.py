# Vérification 
'''Écrire un algorithme qui demande un nombre compris entre 10 et 20, jusqu’à ce que la réponse  convienne. En cas de réponse supérieure à 20, on fera apparaître un message : « Plus petit ! », et  inversement, « Plus grand ! » si le nombre est inférieur à 10.'''

from random import randrange 
x = randrange(10,20)
y=0
print('Veuillez entrez un nom entre 10 et 20')
 
while(y != x):
    y = int(input())
 
    if(y<x):
        print("C'est plus grand")
    if(y>x):
        print("C'est plus petit")
    if( y==x):
        print("BRAVO")