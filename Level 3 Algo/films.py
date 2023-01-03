from random import shuffle

films = []
years = []
for i in range(0, 10):
    films += [input("Saisir le nom du film : ")]
    years += [input("Saisir l'année de  : ")] 
var =[]
for film in films:
    var = var + [f"Afficher l'année du film : {film}"]
   

menu = ["Quitter"] + var + ["Jeu quiz"]

choice = 1
while choice != 0:
    # Affichage du menu
    print()
    print("-###- MENU -###-")
    for i in range(0, 12):
        print(f"{i}. {menu[i]}")

    # On demande le choix 
    choice = int(input("\nVotre choix : "))
    
    print('--------------------------------')
    if choice == 1:
        for i in range(0,11):
            print(f"Année de {film[i]} : {years[i]}")
    elif choice >= 1 and choice <= 11-1:
        print(f"Année de {films[choice-1]} : {years[choice-1]}")
    elif choice == 11 :
        
        
        '''
        for i in range(0,3) :
            import random
            name = input('Votre prénom ? : ')
            print('Bienvenue sur le quizz',name)
            guess = 0
            tries = 0
            answer = 1
            score = 0
                                                '''
                                                
print('--------------------------------')

print("\nBye bye !\n")