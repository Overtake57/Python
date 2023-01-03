'''
Exercice 2 :
Demandez à saisir une date de la forme AAAA/MM/JJ (par exemple 2011/10/17) et afficher « Le
17 octobre 2011 est un lundi. » Pour connaitre le nom du jour, on part de la date avec :
• A = année complète (dans l’exemple 2011),
• M = numéro du mois (dans l’exemple 10),
• J = numéro du jour (dans l’exemple 17).
Si MM vaut 1 ou 2, il faut :
• retrancher 1 à A,
• ajouter 12 à M.
Avec ces valeurs, on calcule un nombre N
• N = J + ENT((13 * M + 3) / 5) + ENT(5 * A / 4) — ENT(A / 100) + ENT(A / 400)
• N = MOD(N ; 7)
N donne le nom du jour avec : 0 pour lundi, 1 pour mardi, ..., 6 pour dimanche
'''

date = input("saisir une date au format AAAA/MM/JJ : ")

cpt = 0
A = ""
M = ""
J = ""
for c in date:
    cpt += 1
    if cpt < 5 :
        A += c
    if cpt > 5 and cpt < 8:
        M += c
    if cpt > 8:
        J += c

monthNumber = int(M)
year = int(A)

A = int(A)
M = int(M)
J = int(J)

if M == 1 or M == 2:
    A = A - 1
    M = M + 12

N = J + int((13 * M + 3) / 5) + int(5 * A / 4) - int(A / 100) + int(A / 400) 
N = N%7

day = ""
if N == 0:
    day = "Lundi"
elif N == 1:
    day = "Mardi"
elif N == 2:
    day = "Mercredi"
elif N == 3:
    day = "Jeudi"
elif N == 4:
    day = "Vendredi"
elif N == 5:
    day = "Samedi"
elif N == 6:
    day = "Dimanche"

month = ""
if monthNumber == 1:
    month = "janvier"
elif monthNumber == 2:
    month = "février"
elif monthNumber == 3:
    month = "mars"
elif monthNumber == 4:
    month = "avril"
elif monthNumber == 5:
    month = "mai"
elif monthNumber == 6:
    month = "juin"
elif monthNumber == 7:
    month = "juillet"
elif monthNumber == 8:
    month = "août"
elif monthNumber == 9:
    month = "septembre"
elif monthNumber == 10:
    month = "octobre"
elif monthNumber == 11:
    month = "novembre"
elif monthNumber == 12:
    month = "décembre"

print(f"Le {J} {month} {year} est un {day}")