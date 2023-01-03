# Exercice : indemnité formateur

KM = float(input("Distance entre résidence et lieu de remplacement: "))
Q = int(input("Nombre de jours de remplacement : "))

if KM < 15 : 
    TauxIndRemp = 12.50

elif KM < 30 : 
    TauxIndRemp = 23.50

elif KM < 45 :
    TauxIndRemp = 30.00

elif KM < 65 : 
    TauxIndRemp = 37.00

elif KM < 85 :
    TauxIndRemp = 44.00

else:
    TauxIndRemp = 50.00

repas = Q * 15 * 2
indemnite = TauxIndRemp * Q + repas

print("Montant de l’indemnité total: ",indemnite, "€")


