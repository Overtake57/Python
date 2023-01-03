'''Exo7 - Calcul du volume d'un parallélépipède'''
def volumeParallelepipede():
    calc = profondeur * largeur * hauteur
    print("Le volume est de", calc, "cm3")

profondeur = int(input("Veuillez entrer la profondeur : "))
largeur = int(input("Veuillez entrer la largeur : "))
hauteur = int(input("Veuillez entrer la hauteur : "))
volumeParallelepipede()