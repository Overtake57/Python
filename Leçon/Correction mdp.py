#                                              Verification mot de passe

# attempt == 0 or userPassword == password >> Stop 
# attempt != 0 and userPassword != password
# f = format string

password = "Bonjour"
attemptCount = 3
userPassword = ""

while attemptCount != 0 and userPassword != password:
    userPassword = input(f"Veuillez saisir votre mot de passe {attemptCount} essai.s restant ")
    attemptCount = attemptCount - 1

# Içi on est sorti de la boucle si mot de passe est valide ou nombre d'essais épuisé   
# Soit attemptCount == 0
# Soit userPassword == password
if attemptCount == 0:
    print("Vous n'avez plus d'essais disponnibles, votre compte est désormais bloqué.")
    isUserAnswerYes = input("Voulez vous répondre à votre question secrète ? (oui/non) : ").lower() == "oui"
    if isUserAnswerYes:
        isTheGoodAnswer = input("Quel est le nom de votre chat ? : ").lower() == "minou"
        if isTheGoodAnswer:
            print("Accès autorisé.")
        else:
            print("Votre compte est bloqué.")
    else:
        print("Votre compte est bloqué.")
else:
    print("Accès autorisé.")