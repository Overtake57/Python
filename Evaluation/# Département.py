# Département

'''Cet algorithme est un petit jeu pour enfant. Faites la saisie des noms (et numéro) de 10  départements puis, dans une boucle, demandez la saisie d’un numéro.  L’algorithme affichera le nom du département correspondant au numéro saisi. '''

'''
Ain 01
Aisne 02
Allier 03
Ardêche 07
Ardennes 08
Moselle 57
Rhône 69
Paris 75
Somme 80
Var 83
Loire 42
'''
departement = ["Ain","Aisne","Allier","Ardeche","Ardennes","Moselle","Rhone","Paris","Somme","Var","Loire"]
nombre = [1,2,3,8,57,69,75,80,83,42]
# Fonction Tableau
def options():
    print("Entrer 1 pour afficher les départements")
    print("Entrer 2 pour afficher les nombres")
    print("Entrer 3 pour afficher les départements et leur nombre")
    print("Entrer 4 pour quitter le programme ")
# Boucle du tableau
while True:
    options()
    option = int(input())
    if option == 1:
        print("=======================================================")
        print(" ")
        print("La liste des départements son : ", departement)
        print(" ")
        print("=======================================================")
    elif option == 2:
        print("=======================================================")
        print(" ")
        print("La liste des nombres son : ", nombre)
        print(" ")
        print("=======================================================")
    elif option == 3:
        print("=======================================================")
        print(" ")
        print("Les départements:", departement , nombre)
        print(" ")
        print("=======================================================")
        print(" ")
    elif option == 4:
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


