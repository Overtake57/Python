'''Exo9 - Calcul de moyenne'''
def moyenne():
    calc = (note1 + note2 + note3 + note4) / 4
    print("La moyenne de l'élève est de :", calc)

note1 = int(input("Veuillez entrer la note de français: "))
note2 = int(input("Veuillez entrer la note de math: "))
note3 = int(input("Veuillez entrer la note de géometrie: "))
note4 = int(input("Veuillez entrer la note de informatique: "))
moyenne()
