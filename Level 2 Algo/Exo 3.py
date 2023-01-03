# tombola de la palette de petits pots
def winORloose():
    res = a - b 

    print ("Vous avez", res, "ans")

    baby = 3

    if res <= baby:
        print("L'enfant gagne une palette de petits pots")

    elif res > baby:
        print("L'enfant ne gagne pas la palette de petits pots")
    
a = int(input("Veuillez saisir l'année actuelle : "))

b = int(input("En quelle année l'enfant est née? "))

winORloose()
