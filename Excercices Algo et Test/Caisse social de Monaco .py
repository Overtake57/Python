# Direction Caisse Socials Monaco

# mensualité entière 160.60 au 1er Octobre N;
# 85h00 de travail au cours du mois
# M = (120.60/145) * 85 = 70.70 €

imma = str(input("Veuillez saisir votre immatriculation: oui ou non ?"))
if imma == "oui":
    next
if imma == "non":
    quit

enfant = str(input("Enfant a charge: Oui ou Non ?"))
if enfant == "oui":
     next
if enfant == "non":
     quit

age = int(input("L'age de votre enfant en fin de mois : "))
if age > 0 and age <= 3: 
    aloc = 120.60 
elif age > 3 and age <= 6:
    aloc = 180.90
elif age > 6 and age <= 10:
    aloc = 217.00
elif age > 10 and age<= 21:
    aloc = 253.20
elif age > 21 :
    print("Refus!")

nhbt = int(input("nombre d'heures de travail du chef de foyer pendant le mois? : "))

calc = (aloc / 145 ) * nhbt

print("la mensualité des allocations familiales de votre foyer est de :", round(calc))








