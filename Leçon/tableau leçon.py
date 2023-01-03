tab = [] # tableau vide
alphabet = ["a","b","c","d"] # tableau avec des chaînes de caractères
entiers = [1,2,3,4] # tableau avec de entiers

noteMath = 12
noteFrancais = 15
notes = [noteMath,noteFrancais] # tableau de variables

tabMulti = ["a",1,entiers] # tableau avec différents type de variables/valeurs
print(tabMulti) # affiche ['a', 1, [1, 2, 3, 4]]

tailleAlphabet = len(alphabet) 
print(tailleAlphabet) # affiche 4 
dernierIndex = tailleAlphabet - 1
# il y a 4 éléments dans le tableau alphabet 
indexesAlphabet = range(0, tailleAlphabet) # permet de récupérer les indices du tableau alphabet
print(indexesAlphabet) # [0,1,2,3]

# Ci-dessous, 3 exemple de parcours boucle (TMTC Enzo)

# parcourir un tableau à l'aide des indices
for i in range(0, tailleAlphabet):
    print(f"L'élément à l'indice {i} du tableau alphabet est : {alphabet[i]}") # on accède à l'élement situé à i
    # le petit f ici sert à utiliser les {} (accolades) pour afficher la valeur de l'expression utiliser entre ces mêmes accolades
    # ici on affiche la valeur de l'indice ainsi que la valeur de l'élement situé à cet indice

# parcourir un tableau élement par élement sans avoir besoin des indexes
for lettre in alphabet: # équivalent foreach dans d'autres languages
    print(f"L'élement à la valeur {lettre}")

# parcourir un tableau élement par élement avec en plus l'indice de l'élement (ou le numéro de la boucle)
for indice,lettre in enumerate(alphabet): # toujours dans l'ordre (indice,valeur) # couple clé/valeur
    print(f"L'élément à l'indice {indice} du tableau alphabet est : {lettre}")

# parcourir un tableau avec une boucle TANT QUE (beurk)
i = 0
while i < tailleAlphabet:
    print(f"L'élément à l'indice {i} du tableau alphabet est : {alphabet[i]}")
    i = i + 1

# Ajouter un élement dans un tableau
valeurAajouter = 5
tab = tab + [valeurAajouter] # OU tab += [valeurAajouter]
# concaténation de cellules 
# tab = [] + [5] ==> [5]
print("tab + [5] = ",tab)
# OU on utilise la méthode append (ajouter)
tab.append(valeurAajouter)
print("tab.append(5) =>", tab) # affiche tab.append(5) => [5, 5]

# Ajouter plusieurs élement dans un tableau
# Exemple : on souhaite ajouter dans un tableau les chiffres de 1 à 10
chiffres = []
print(chiffres)
for chiffre in range(1, 11): # 11 ici car le dernier élement du range est exclu donc ici chiffre >= 1 and chiffre < 11
    chiffres += [chiffre]
    print(chiffres)
    # ou chiffres.append(chiffre)

# Ajouter plusieurs élements saisis par l'utilisateur dans un tableau
notes = []
print(notes)
for i in range(5): # pareil que range(0,5)
    saisie = float(input("Saisir une note sur 20 : "))
    notes += [saisie]
    # notes += [float(input("Saisir une note sur 20 : "))] (pareil que la ligne 65)
    print(notes)

# Modifier une valeur dans un tableau
tabAmodifier = ["John","Enzo","Hugo"]
print("Avant modif :",tabAmodifier)
# on va remplacer "John" par "Maxime"
tabAmodifier[0] = "Maxime" # on modifie la valeur à l'indice 0
print("Après modif :",tabAmodifier)

# Supprimer une valeur dans un tableau
classe = ["Marvyn","Céline","Fadime"]
print("Avant suppession:", classe)
del classe[0] # on supprime
# classe.pop(0) : alternative à la ligne 79

# Supprimer un élément d'un tableau via sa valeur
classe.remove("Céline",)
# Supprimer toutes les occurence dans un tableau
# while "Céline" in classe:
#     classe.remove("Céline")

print("Après suppression:", classe)

# Tricks spécial python
monTableau = [0] * 10 # multiplication de cellule
print(monTableau)

