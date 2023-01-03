'''
Exercice 9 :
Une pointe est constituée d’une tête symbolisée par le caractère « _ » et d’une tige symbolisée par le
caractère « | ». La dimension d’une pointe est la longueur de sa tige, qui correspond au nombre de
caractères « | » présents.
'''

nombre = input("Saisir le nombre de pointes : ")
while nombre.isnumeric() == False :
    nombre = input("Valeur inccorect !")
nombre = int(nombre)

taille = input("Saisir la taille des pointes ")
while taille.isnumeric() == False :
    taille = input("Valeur inccorect !")
taille = int(taille)

for i in range (0, nombre ):
    print("_", end =' ')
for j in range(0,taille):
    print()
    for i in range(0, taille):
        print("|", end=' ')
