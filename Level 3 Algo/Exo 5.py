'''
Exercice 5 :
On se propose de calculer la moyenne des notes d’un élève pour certaines matières ; français,
maths, géographie et informatique.
Pour chacune de ces matières, il faudra saisir un coefficient de pondération compris entre 1 et 10.
Calculez la moyenne en tenant compte des coefficients de pondération.
Affichez une appréciation :
Si la moyenne est comprise entre 16 et 20, la mention est « Très bien ».
Si la moyenne est comprise entre 12 et 16, la mention est « Bien ».
Si la moyenne est comprise entre 8 et 12, la mention est « Assez bien ».
Si la moyenne est comprise entre 4 et 8, la mention est « Insuffisant ».
Si la moyenne est comprise entre 0 et 4, la mention est « Nul ».
Il faut contrôler que les notes sont comprises entre 0 et 20 et que les coefficients sont compris
entre 1 et 20. (reprise de l’exercice 9 feuille niveau II pour utiliser des boucles)
'''

note1 = int(input("Veuillez entrer la note de français: "))
coef1 = int(input("Veuillez entrer le coefficient de la note de français: "))
note2 = int(input("Veuillez entrer la note de math: "))
coef2 = int(input("Veuillez entrer le coefficient de la note de Math: "))
note3 = int(input("Veuillez entrer la note de géometrie: "))
coef3 = int(input("Veuillez entrer le coefficient de la note de Géométrie: "))
note4 = int(input("Veuillez entrer la note de informatique: "))
coef4 = int(input("Veuillez entrer le coefficient de la note d'informatique: "))
if note1 / note2 / note3 / note4 <-1:
        print("Valeur non permise")
elif note1 / note2 / note3 / note4 > 20:
        print("Valeur non permise")
if coef1 / coef2 / coef3 / coef4 < 0:
    print("Le coef est uniquement de 1 a 10.")
elif coef1 / coef2 / coef3 / coef4 > 10 :
    print("Le coef est uniquement de 1 a 10.")
moyenne = coef1 + coef2 + coef3 + coef4

calc = ((note1 * coef1) + (note2 * coef2) + (note3 * coef3) + (note4 * coef4) ) / moyenne

if calc >= 16 and calc <=20 :
    print("Très bien",calc)
elif calc >= 12 and calc < 16:
    print("Bien", calc)
elif calc >= 8 and calc < 12 :
    print("Assez bien", calc)
elif calc >=4 and calc < 8 :
    print("Insuffisant", calc)
elif calc >= 0 and calc < 4 :
    print ("Nul", calc)