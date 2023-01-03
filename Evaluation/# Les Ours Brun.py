# Les Ours Brun

print("Bienvene chez Les Ours Brun")

print("")

age = int(input("Quel age avez vous ? "))

if age > 1 and age <= 12:
    prix_enfant = str(input("Vous êtes un enfant le prix est de 18.70 € la journée Et 300 € Pour la saison / Quel offre vous intéresse journée ou saison ? : "))
    if prix_enfant == "journée":
        print("Vous avez choisis la journée")
    elif prix_enfant == "saison":
        print("Vous avez choisis l'abonnement saisonnier")

    elif age > 12 and age <= 59:
        prix_adulte = str(input("Vous êtes un adulte le prix est de 25.80 € la journée Et 510 € Pour la saison / Quel offre vous intéresse journee ou saison ? : "))
        if prix_adulte == "journée":
            print("Vous avez choisis la journée")
        elif prix_adulte == "saison":
            print("Vous avez choisis l'abonnement saisonnier")

    elif age >= 60:
        prix_senior = str(input("Vous êtes un seniors le prix est de 21.40 € la journée Et 340 € Pour la saison / Quel offre vous intéresse journee ou saison ? "))
        if prix_senior == "journée":
            print("Vous avez choisis la journée")
        elif prix_senior == "saison":
            print("Vous avez choisis l'abonnement saisonnier")
