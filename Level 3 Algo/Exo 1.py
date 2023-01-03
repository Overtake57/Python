'''
Exercice 1 :
Réalisez un jeu de dés utilisant les aiguillages conditionnels. Au démarrage du programme, il
calcule au hasard un nombre entre 1 à 6 (utilisez la fonction suivante : valeur <— HASARD(valeur
mini , valeur maxi)). Le programme affiche « Vous avez fait un six » et il affiche la face du dé, sur 3
lignes, par exemple :
«0 0»
« 0 »
«0 0»
'''

from random import randint
repeat_rolling = True
while repeat_rolling:
    print("Le nombre afficher sur le dée est le ->",randint(1,6))
    print("Voulais vous relancez ?")
    repeat_rolling = ("no" or "yes") in input().lower()
