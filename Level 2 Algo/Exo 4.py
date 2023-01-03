# Paire contre impaire 
def paireImpaire():
   res = A + B 
   print("La somme de vos doigts est de:", res)

   if (res % 2) == 0:
      print("{0} est Paire le joueur A gagne".format(res))
   else:
      print("{0} est Impaire le joueur B gagne".format(res))

A = int(input("Nombre de doigts du joueur A: "))
B = int(input("Nombre de doigts du joueur B: "))

paireImpaire()




   


