
from random import shuffle

# Générateur de phrases
# demander en console une chaine de la forme "mot1/mot2/mot3/mot4"
chained_words = input("Entrer une chaine de la forme mot1/mot2/mot3/mot4")

# transformer cette chaine en liste
words = chained_words.split("/")

# la melanger
shuffle(words)

# recuperer le nombre d'elements
words_len = len(words)

# si le nombre d'élements de cette liste est inferieur à 10
if words_len < 10:
    # afficher les deux premiers mots
    print(words[0], words[1])

# si le nombre d'éements est superieur ou égal à 10
else:
    # afficher les 3 derniers
    print(words[words_len - 1], words[words_len - 2], words[words_len - 3])