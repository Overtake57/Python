# TVA 
def tvaTable():
  print("1 = 5.5 %, de TVA")
  print("2 = 19.6 %, de TVA")
  print("3 = 33 %, de TVA")
  
def tvaCalc():
  if b == 1:
    tva = 5.5
  if b == 2:
    tva = 19.6
  if b == 3:
    tva = 33
  print("Le prix HT est de", a, "€," "la tva est de", tva,"% et le prix TTC est de", (a * tva)/100 + a)
  
a = int(input("Saisir le prix HT : "))

tvaTable()

b = int(input("Choisir le taux de TVA : "))

tvaCalc()

