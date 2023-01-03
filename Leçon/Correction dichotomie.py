students = ["Alonso","Remy","Damien","Joris","Héléna","Océane","Yoann","Rémy","Jimmy","Fouad","Benjamin","Kostandin","Antoine","Pierre","Aymeric"]
studentToSearch = input("Saisir le nom d'un.e stagiaire à rechercher : ")
finded = False
for index,student in enumerate(students):
    if student.lower() == studentToSearch.lower():
        print(f"Trouvé.e ! Le stagiaire {studentToSearch} est à l'index {index} de la liste de stagiaires.")
        finded = True
        break # Je veux qu'une occurence

if not finded:
    print(f"Il semble que le stagiaire {studentToSearch} ne soit pas dans la liste...")