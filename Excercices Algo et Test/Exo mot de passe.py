"""Écrire un algorithme qui permet de vérifier le mot de passe saisi au clavier. L’utilisateur a
droit à 3 chances pour que la machine lui affiche le succès de l’authentification sinon un
message de compte bloqué sera affiché.

Dans le cas où il veut encore retenter l’accès au compte une nouvelle chance lui est proposée
sous forme de question secrète à laquelle il devra répondre. Si la réponse est incorrecte l’accès
lui est définitivement refusé pour l’exécution en cours.
"""
# Note : le mot de passe correct est 'Bonjour' et la réponse correcte à la question secrète est
#'Minou'

# Mot de passe
password = input("Entrer votre mot de passe: ")
count = 0
while count != 2:
    if password == 'Bonjour':
        print ("Bienvenue dans votre session")
        break
    else:
        print ("Mot de passe incorrect")
        count += 1
    password = input("Entrer votre mot de passe: ")
if count == 2:
    print("Désolé il y a eu trop de tentatives de connexion. séssion bloqué" )
# Question 
qs = input("Voulez vous passer à votre dernière chance d'acceder à la session : Oui ou Non ")
if qs == "Oui":
    rep = input("Quel est le nom de votre chat : ")
    if rep == "Minou": 
        print("Bienvenue dans votre session vous avez répondu juste")
elif qs == "Non": 
    print("Session terminé")
    print("Accès définitivement refusé pour l'éxécution en cours")
else : 
    print("Accès définitivement refusé pour l'éxécution en cours")

    


           
