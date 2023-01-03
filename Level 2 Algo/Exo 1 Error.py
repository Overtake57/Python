#Moyenne de l'eleve 

note1 = int(input("Veuillez entrer la note de français: "))
note2 = int(input("Veuillez entrer la note de math: "))
note3 = int(input("Veuillez entrer la note de géometrie: "))
note4 = int(input("Veuillez entrer la note de informatique: "))

coef1 = int(input("Veuillez entrer le coefficient de français: "))
coef2 = int(input("Veuillez entrer le coefficient de math: "))
coef3 = int(input("Veuillez entrer le coefficient de géometrie: "))
coef4 = int(input("Veuillez entrer le coefficient de informatique: "))

calc = ((note1*coef1)+ (note2*coef2) + (note3*coef3) + (note4*coef4)) / 8

print("La moyenne de l'élève est de :", calc)