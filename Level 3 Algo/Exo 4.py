'''
Exercice 4 :
Réalisez un compteur qui affiche toutes les valeurs comprises entre une borne de départ et une
borne d’arrivée en tenant compte d’un pas d’incrément.
'''
start = input("Bornne de départ : ")
while start.isnumeric() == False :
    start = input("Valeur inccorect !")
start = int(start)

end = input("Bornne de d'arrivé : ")
while end.isnumeric() == False :
    end = input("Valeur inccorect !")
end = int(end)

foot = input("Nombre de pas d'incrément : ")
while foot.isnumeric() == False :
    foot = input("Valeur inccorect")
foot = int(foot)

#boucle
var = 0
res = ""
if start < end :
    for var in range(start,end+ 1,foot):
        res += str(var)+" "
    print(res)