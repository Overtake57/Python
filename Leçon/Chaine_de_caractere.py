#                   CHAINE DE CARACTERE
# Ceci est une chaine de caractère
A="Chaine de caractère"
# Une chaine de caractère est non modifiable
# On peux utiliser [:] Pour séparer la chaine de caractère
# Dans ma chaine de caractère, chaque lettre correspond à un numéro et commence à 0
# A=input("Chaine de caractère")
#          0123456789111111111
#                    012345678
# Si on veux garder seulement Chaine de la variable il me suffit de faire:
B=A[ :6]
print("B=A[ :6] donne :",B)
# A[ :6] va d'inclure la chaine de caractère depuis le début jusqu'à la 6ème caractère exclu
C=A[10: ]
print("A[10: ] donne :",C)
# A[10: ] va inclure la chaine de caractère à partir de 10 jusqu'à la fin 
D=A[7:9]
print("D=A[7:9] donne :",D)
# D=A[7:9] va inclure la 7ème chaine de caractère jusqu'à la 9ème exclu
E=A[14]
print("E=A[14] donne :",E)
# E=A[14] permet de sélectionner seulement un caractère de la chaine 
