"""
Calculez la moyenne des notes d’un élève après avoir saisi les notes de français, de math, de 
géométrie et d’informatique.
"""
from os import system

subjects = []
subjectsCount = int(input("Combien de matières souhaitez-vous ajouter ? "))
for i in range(0, subjectsCount):
    subjects += [input("Saisir le nom de la matière : ")]


# subjects_menu_items = [f"Afficher la note de {subject}" for subject in subjects]
subjects_menu_items = []
for subject in subjects:
    subjects_menu_items = subjects_menu_items + [f"Afficher la note de {subject}"]

menu = ["Quitter","Afficher les notes"] + subjects_menu_items + ["Calculer la moyenne"]
notes = []

total = 0
for subject in subjects:
    note = int(input(f"Veuillez saisir la note de {subject} : "))
    notes += [note]
    total += note
moyenne = total / len(subjects)

choice = 1
while choice != 0:
    # Affichage du menu
    print()
    print("### MENU ###")
    for i in range(0, len(menu)):
        print(f"{i}. {menu[i]}")

    # On demande le choix 
    choice = int(input("\nVotre choix : "));
    system("cls") # Permet de nettoyer la console pour l'affichage
    print('--------------------------------')
    if choice == 1:
        for i in range(0,len(notes)):
            print(f"Note de {subjects[i]} : {notes[i]}/20 ")
    elif choice >= 2 and choice <= len(menu)-2:
        print(f"Note de {subjects[choice-2]} : {notes[choice-2]}/20 ")
    elif choice == len(menu)-1:
        print(f"La moyenne est de {moyenne}/20")
    print('--------------------------------')

print("\nBye bye !\n")