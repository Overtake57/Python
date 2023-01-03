#Boucle while et for

#imprime ligne par ligne jusqu'a la fin du mot
'''
v = "Bonjour"
for lettre in v:
    print(lettre) 
'''

#Imprime 5 fois

'''
i = 0
while i < 5 :
    print("Metz Numeric School")
    i = i + 1 
'''
# Multiplication

'''
n = 5 
for i in range(1,11):
    print(i,"x",n,"=",i*n)
'''

# Boucle simple nombre magique

'''from random import randint

input("Veuillez choisir le niveau entre 1 , 2 et 3")

n = randint(1,10)
while True:
    nombre = int(input("Saisire le nombre entre 1 et"))
    if nombre < n :
        print("Trop petit")
    elif nombre > n :
        print("Trop grand")
    if nombre == n:
        print("Bravo")
        break
'''
'''
from random import randint
A=1
while A==1:
    M=randint(1,100)
    print(M)
    N=int(input("Entrer un nombre:"))
    c=1
    while not(N==M):
        if N>M:
            print("Trop grand")
        else:
            print("Trop petit")
        N=int(input("Entrer un nombre:"))
        c=c+1
    print("Gagné !")
    print("nombre de coups:",c)
    A=int(input("Une autre partie 1-Oui/ 2-Non ?"))
'''