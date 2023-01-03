import hashlib
# Type de hashage de mot de passe entre SHA1 et MD5 
password = input("Ecrire le mot de passe à crypté\n>")

# Hashage SHA11
print("\nSHA1:\n")
for i in range(3):
    setpass = bytes(password, 'utf-8')
    hash_object = hashlib.sha1(setpass)
    guess_pw = hash_object.hexdigest()
    print(guess_pw)

# Hashage MD5 
print("\nMD5:\n")
for i in range(3):
    setpass = bytes(password, 'utf-8')
    hash_object = hashlib.md5(setpass)
    guess_pw = hash_object.hexdigest()
    print(guess_pw)
    
    # Pas accés a l'import Bcrypt  :(
#print("\nBCRYPT:\n")
#for i in range(3):
#   hashed = bcrypt.hashpw(setpass, bcrypt.gensalt(10))