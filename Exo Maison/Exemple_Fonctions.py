def isGgood (moy:float):
    if moy >= 16:
        return True
    else:
        return False

'''
# On crée la fonction
def get_vowels_numbers(word):
    # Créer un compteur de voyelles
    nb_vowels = 0

    # Boucle "for" pour chaque lettre du mot vous verifiez s'il s'agit d'un voyelle
    for letter in word:
        # Voyelle
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            # On ajoute un au compteur
            nb_vowels += 1

    # à la fin de la fonction, vous allez renvoyer le compteur
    return nb_vowels


word = input("Entrer un mot : ")
vowels_count = get_vowels_numbers(word)
print("Il y a", vowels_count, "voyelles dans le mot", word)
'''