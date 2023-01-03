#Correction Magic Number

from random import randint
# J'initialise une variable pour la valeur de mon joueur
player = 0

# Je demande la difficulté au joueur
print("Choisir le niveau de difficulté !")
print("Niveau 1 : trouver le chiffre magique entre 1 et 10, taper a")
print("Niveau 2 : trouver le chiffre magique entre 1 et 100, taper b")
print("Niveau 3 : trouver le chiffre magique entre 1 et 1000, taper c")
choice = input("Votre choix : ")
# On vérifie le choix et on le redemande si choix n'est pas valide
while choice != "a" and choice != "b" and choice != "c":
    choice = input("Choix invalide. Recommencez : ")

# On genère notre nombre aléatoire en fonction de la difficulté
diff = 10
if choice == "b":
    diff = 100
elif choice == "c":
    diff = 1000
magic = randint(1, diff)

# Je commence le jeu avec une boucle
# Le joueur gagne quand player == magic

while player != magic:
    player = input(f"Veuillez saisir un nombre entre 1 et {diff} : ")
    # On vérifie si la valeur saisie par le joeur est bien un nombre
    if player.isnumeric():
        player = int(player)
        if player < 1 or player > diff:
            print("Attention, valeur non permise.")
        elif player > magic:
            print("Trop grand !")
        elif player < magic:
            print("Trop petit !")
    else:
        print("Saisie invalide !")

# En dessous de la boucle le joueur à forcément gagné (puisque la boucle s'est arrêtée)
print("Gagné !")