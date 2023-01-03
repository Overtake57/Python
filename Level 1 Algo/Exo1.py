'''Exo1 - Calculatrice'''

def calculatrice():
    somme = a + b
    diff = a - b 
    produit = a * b
    print("La somme de",a,"et",b, "vaut",somme)
    print("Le produit de",a,"et",b, "vaut",produit)
    print("La difference de",a,"et",b, "vaut",diff)
    if b != 0:
        div = a / b
        print("Le resultat de la division de",a,"et",b, "vaut",div)
    else:
        print("Division par 0 impossible.")
        
a = int(input("Veuillez saisir un nombre a : "))
b = int(input("Veuillez saisir un nombre b : "))
calculatrice()


