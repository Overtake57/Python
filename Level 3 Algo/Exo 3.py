'''
Exercice 3 :
Saisissez un nombre compris entre 1 et 10. En cas d’erreur de saisie, il y a affichage d’un message «
Valeur non permise ». Si le nombre est égal au nombre magique connu du programme, il affiche «
Gagné » sinon il affiche un message « Trop petit » ou « Trop grand » suivant la valeur saisie.
(reprise de « Chiffre magique 1 » pour utiliser des boucles)
'''


from random import randint

player = 0

print("Choisir le niveau de difficulté !")
print("Niveau 1 : trouver le chiffre magique entre 1 et 10, taper a")
print("Niveau 2 : trouver le chiffre magique entre 1 et 100, taper b")
print("Niveau 3 : trouver le chiffre magique entre 1 et 1000, taper c")
choice = input("Votre choix : ")

while choice != "a" and choice != "b" and choice != "c":
    choice = input("Choix invalide. Recommencez : ")

diff = 10
if choice == "b":
    diff = 100
elif choice == "c":
    diff = 1000
magic = randint(1, diff)

while player != magic:
    player = input(f"Veuillez saisir un nombre entre 1 et {diff} : ")
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


print("Gagné !")