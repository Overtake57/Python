
# Place de cinema

# recolter l'age de la personne "Quel est votre age ?"
age = int(input("Quel est votre age ?"))

# si la personne est mineur -> 7€
if age < 18:
    prix_total = 7
# si la personne est majeur -> 12€
else:
    prix_total = 12

# ou alors en ternaire
# prix_total = (7, 12)[age < 18]

# souhaitez-vous du pop corn ?
pop_corn_request = input("Souhaitez-vous du pop corn ? (Oui, Non)")

# si oui
if pop_corn_request == "Oui":
    prix_total += 5

print("Vous devez payer", prix_total, "€")