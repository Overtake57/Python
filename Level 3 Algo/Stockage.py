from tkinter import * 
import random

# Demande de film

films = []
yearFilm = []
filmsCount = int(input("Combien de film souhaitez-vous ajouter ? "))
for i in range(0, filmsCount):
    films += [input("Saisir le nom du film : ")]
    yearFilm += [input("Saisir l'année de sortie du film : ")]

def GO1 ():
    print('Vous avez ajouter', filmsCount , 'films')

def GO2 ():
    for i in range(0,filmsCount):
            print(f"Le film {films[i]} est sortie en {yearFilm[i]}")
def GO3 ():
    print("Program Off")

#tkinter /

fen = Tk()                         # Fenetre du jeu
fen.title('### Menu ###')          # Titre de la w/
fen.minsize(width=350, height=75)  # Taille de la fenetre
fen.config(background='#08b8b1')   # Cyan

# Bouton de la fenetre fonction
bou1 = Button(fen, text= 'Nombre de film', command = GO1).pack(side=BOTTOM)
bou1 = Button(fen, text= 'Liste de films', command = GO2).pack(side=BOTTOM)
bou1 = Button(fen, text="Quit", command=fen.destroy).pack()

fen.mainloop() # elle affiche la fenêtre principale à l'écran puis elle attend que l'usager pose une action.

# Quiz Guess the year
'''
input(print("Voulez vous participé au Quizz : Guess the year Oui/Non : ")).lower() == "oui"
if "Oui" :
    name = input('Quel est votre prénom : ')
    print('Bievenue sur Guess the year',name)
    answer = input("En quel année est sortie", films)
    if answer == yearFilm[films]:
        print("Correct!")
        
'''
    
   


