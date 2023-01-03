#                                                     Tp4 - Tableau note élève
# Note de l'élève a implanter 
print("Note de l'élève entre 0 et 20")
Notes = ['Français', 'Maths', 'Géométrie', 'Informatique']
Notes[0] = float(input("Veuillez entrer la note de français: "))
Notes[1] = float(input("Veuillez entrer la note de math: "))
Notes[2] = float(input("Veuillez entrer la note de géometrie: "))
Notes[3] = float(input("Veuillez entrer la note d' informatique: "))
# Calcule de la moyenne
calcMoyenne = (Notes[0] + Notes[1] + Notes[2] + Notes[3]) / 4
# Fonction Tableau
def options():
    print("Entrer 1 pour afficher les notes")
    print("Entrer 2 pour calculer la moyenne")
    print("Entrer 3 pour afficher la note de Français")
    print("Entrer 4 pour afficher la note de Maths")
    print("Entrer 5 pour afficher la note de Géométrie")
    print("Entrer 6 pour afficher la note d'Informatique")
    print("Entrer 7 pour quitter le programme ")
# Boucle du tableau
while True:
    options()
    option = int(input())
    if option == 1:
        print("=======================================================")
        print(" ")
        print("Les notes de l'élève son : ", Notes)
        print(" ")
        print("=======================================================")
    elif option == 2:
        print("=======================================================")
        print(" ")
        print("La moyenne de l'élève est de : ", calcMoyenne)
        print(" ")
        print("=======================================================")
    elif option == 3:
        print("=======================================================")
        print(" ")
        print("La note de français de l'élève :", Notes[0])
        print(" ")
        print("=======================================================")
        print(" ")
    elif option == 4:
        print(" ")
        print("=======================================================")
        print(" ")
        print("La note de mathématique de l'élève :", Notes[1])
        print(" ")
        print("=======================================================")
        print(" ")
    elif option == 5:
        print(" ")
        print("=======================================================")
        print(" ")
        print("La note de géométrie de l'élève :", Notes[2])
        print(" ")
        print("=======================================================")
        print(" ")
    elif option == 6:
        print(" ")
        print("=======================================================")
        print(" ")
        print("La note d'informatique de l'élève :", Notes[3])
        print(" ")
        print("=======================================================")
        print(" ")
    elif option == 7:
        print(" ")
        print("=======================================================")
        print(" ")
        print("Aurevoir")
        print(" ")
        print("=======================================================")
        break
    else : 
        print("=======================================================")
        print(" ")
        print("Valeur non comprise")
        print(" ")
        print("=======================================================")

