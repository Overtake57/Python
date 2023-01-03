'''
Exercice 7 :
Écrivez l’algorithme qui affiche à l’écran les lignes suivantes :
10 11 12 13 14 15
20 21 22 23 24 25
30 31 32 33 34 35
40 41 42 43 44 45
50 51 52 53 54 55
'''
'''
res = ""
if 10 < 15 :
    for var in range(10,15+1):
        res += str(var)+" "
    print(res)
res = ""
if 20 < 25 :
    for var in range(20,25+1):
        res += str(var)+" "
    print(res)
res = ""
if 30 < 35 :
    for var in range(30,35+1):
        res += str(var)+" "
    print(res)
res = ""
if 40 < 45 :
    for var in range(40,45+1):
        res += str(var)+" "
    print(res)
res = ""
if 50 < 55 :
    for var in range(50,55+1):
        res += str(var)+" "
    print(res)
'''
def tablooooPasBo():
    for j in range(10, 60, 10):
        print()
        for i in range (j, j+6):
            print(i,end=' ')

tablooooPasBo()
