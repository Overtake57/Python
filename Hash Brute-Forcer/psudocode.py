from urllib.request import urlopen, hashlib

sha1hash = input("Veuillez inséré le hashage. \n>")

LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')


for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
    
    hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
    
    if hashedGuess == sha1hash:
        
        print ("Le mot de passe est", str(guess))
        quit()
    
    elif hashedGuess != sha1hash:
        print("Le mot de passe ",str(guess),"ne match pas, essais suivant...")
        
print("Le mot de passe n'est pas dans la database, on l'aura la prochaine fois.")