'''Exo8 - Saisissez le prix unitaire HT d’un produit et la quantité 
commandée. Calculez le montant HT de la commande, appliquez une remise de
15% et calculez le prix TTC après avoir saisi le taux de TVA'''

def prixTTC():
    TTC = prix_ht * quantité * 0.85 * 1.20
    print("Votre montant TTC est de :",TTC)

prix_ht = int(input("Quel est le montant hors taxe ? "))
quantité = int(input("Quel est la quantité ? "))
prixTTC()

