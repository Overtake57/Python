# Valeur
'''
Une voiture coûte 56 000 e et perd 7% de sa valeur chaque année.  
Rédiger le programme qui calcule et affiche la valeur de cette voiture au bout de 18 ans. 
BONUS : améliorer votre programme en demandant à l’utilisateur le prix d’achat de sa voiture et  l’année à laquelle il souhaite la vendre. (Faire les vérifications nécessaires)
'''

def prix(n):
    Prix = 56000
    for I in range(18):
        Prix= 56000 -7/100

prix()