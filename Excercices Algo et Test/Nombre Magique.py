'''
Saisissez un nombre compris entre 1 et 10.

En cas d’erreur de saisie, il y a affichage d’un message « Valeur non permise ».

Si le nombre est égal au nombre magique connu du programme, il affiche « Gagné » sinon il affiche
un message « Trop petit » ou « Trop grand » suivant la valeur saisie 
'''

from random import randrange    # Ce module implémente des générateurs de nombres pseudo-aléatoires définie
from tkinter import *   # Interface visuelle
 
    # Boucle avec plusieurs niveau de difficulté en définition de fonction 
def GO1 ():
 
 x = randrange(10)
 y=0
 print('Veuillez entrez un nom entre 1 et 10')
 
 while(y != x):
    y = int(input())
 
    if(y<x):
        print("C'est plus grand")
    if(y>x):
        print("C'est plus petit")
    if( y==x):
        print("BRAVO")
 
def GO2 ():
 
 x = randrange(100)
 y=0
 print('Veuillez entrez un nom entre 1 et 100')
 
 while(y != x):
    y = int(input())
 
    if(y<x):
        print("C'est plus grand")
    if(y>x):
        print("C'est plus petit")
    if( y==x):
        print("BRAVO")
 
def GO3 ():
 
 x = randrange(1000)
 y=0
 print('Veuillez entrez un nom entre 1 et 1000')
 
 while(y != x):
    y = int(input())
 
    if(y<x):
        print("C'est plus grand")
    if(y>x):
        print("C'est plus petit")
    if( y==x):
        print("BRAVO")
 
def GO4 ():
 
 x = randrange(10000)
 y=0
 print('Veuillez entrez un nom entre 1 et 10 000')
 
 while(y != x):
    y = int(input())
 
    if(y<x):
        print("C'est plus grand")
    if(y>x):
        print("C'est plus petit")
    if( y==x):
        print("BRAVO")
 

fen = Tk()                      # Fenetre du jeu
fen.title('Nombre Magique Yoann') # Titre du jeu
fen.minsize(width=350, height=75) # Taille de la fenetre
fen.config(background='#08b8b1')  # Cyan

# Bouton du jeu  
bou1 = Button(fen, text= 'Facile', command = GO1).pack(side=BOTTOM)
bou1 = Button(fen, text= 'Intermédiaire', command = GO2).pack(side=BOTTOM)
bou1 = Button(fen, text= 'Difficile', command = GO3).pack(side=BOTTOM)
bou1 = Button(fen, text= 'FOLIE', command = GO4).pack(side=BOTTOM)
 
 
fen.mainloop() # elle affiche la fenêtre principale à l'écran puis elle attend que l'usager pose une action.