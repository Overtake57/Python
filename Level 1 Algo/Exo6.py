'''Exo6 - Calculateur  prix TTC'''

def prixTTC():
    tva = prix_ht * 0.200
    print("Le montant touts taxtes comprises est de", prix_ht + tva, "€") 

prix_ht = float(input("Quel est le montant hors taxe ? "))
prixTTC()
