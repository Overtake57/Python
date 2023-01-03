                                                                # Brute Force du pauvre #
# Import random
from random import *
from time import time 
def get_word_lettres_indexes():
    
    # Liste de lettre
    password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
                'w', 'x', 'y', 'z',]
    
    #password = password + [" "] + [letter.upper () for letter in password]
    
    # Empty string
    guess = ""
 
    # Utilise loop while pour generer plusieur passwords jusqu'à
    # Match user_pass
    while (guess != user_pass):
        guess = ""
        
    # Mauvais mot de passe         
        # Génère un random passwords par une loop for
        for letter in range(len(user_pass)):
            guess_letter = password[randint(0, 25)]
            guess = str(guess_letter) + str(guess)
            
            
        # Le mot de passe par la boucle for
        print(guess)
        # Le mot de passe qui match la boucle for / résultat
    print("Votre mot de passe est :", guess)    

# L'utilisateur entre son mot de passe
user_pass = input("Etrer votre mot de passe :")
get_word_lettres_indexes()






