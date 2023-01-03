'''
Exercice 11 :
Réécrire l’algorithme précédent, mais cette fois-ci on ne connaît pas d’avance combien l’utilisateur
souhaite saisir de nombres. La saisie des nombres s’arrête lorsque l’utilisateur entre un zéro.
'''
# Ask numbers with space
numbers = input("Veuillez saisir un nombre et appuyer sur entrée pour terminer votre saisie: ")
while numbers.isnumeric() == False :
    numbers = input("Valeur inccorect !")
numbers = int(numbers)
variant = 1

while numbers != 0 and variant != 0 :
    numbers = input("Entrer la valeur : ")
    while numbers.isnumeric() == False :
        numbers = input("Valeur inncorect !")
    numbers = int(numbers)
    if numbers > variant :
       variant = numbers

# Highest number pick
print(f"La plus grande valeur de votre liste est : {variant}")

"""# Ask numbers with space
print("Veuillez mettre un espace à chaque nombre et appuyer sur entrée pour terminer votre saisie")
numbers = [int(x) for x in input().split()]
# Highest number pick
max_value = max(numbers)
print("La plus grande valeur de votre liste est : ", max_value)
"""