'''
Exercice 10 :
Écrire un algorithme qui demande successivement 20 nombres à l’utilisateur, et qui lui dise ensuite
quel était le plus grand parmi ces 20 nombres
'''

# Ask numbers with space
numbers = input("Veuillez saisir un nombre et appuyer sur entrée pour terminer votre saisie: ")
while numbers.isnumeric() == False :
    numbers = input("Valeur inccorect !")
numbers = int(numbers)
variant = 0

for i in range(19):
    numbers = input("Entrer la valeur : ")
    while numbers.isnumeric() == False :
        numbers = input("Valeur inncorect !")
    numbers = int(numbers)
    if numbers > variant :
        variant = numbers
    
# Highest number pick

print(f"La plus grande valeur de votre liste est : {variant}")

'''
# Ask numbers with space
print("Veuillez saisir un nombre et appuyer sur entrée pour terminer votre saisie")
for i in range(20):
    numbers = [int(x) for x in input().split()]
# Highest number pick
max_value = max(numbers)
print("La plus grande valeur de votre liste est : ", max_value)
'''