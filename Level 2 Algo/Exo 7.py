#TTC et remise

def ttcRemise():
    if a < 500 :
        print("Vous n'avez aucune remise")
    if a >= 500 and a < 1000 :
        print("vous avez une remise de 2 % votre montant est de:", (a*2) / 100-a)
    if a >=1000 and a < 2000 :
        print("vous avez une remise de 5 % votre montant est de:", (a*5) / 100-a)
    if a >= 2000 :
        print("vous avez une remise de 10 % votre montant est de:",(a*10) / 100-a)

a = int(input("Choissisez un montant: "))
ttcRemise()
