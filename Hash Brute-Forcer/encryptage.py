alphabet = ["a","b","c","d","e","é","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

alphabet = alphabet + [" "] + [letter.upper() for letter in alphabet] + [str(i) for i in range(0,10)]

def getWordLettersRankIntoList(word: str) -> list:
    res = []
    # On parcours chaque lettre dans word
    for letter in word:
        # On recherche l'index de la lettre dans l'alphabet
        for index,value in enumerate(alphabet):
            if value == letter:
                res += [index]
                break
    return res

def calculateCode(letterIndex: int, key: int):
    code = letterIndex + key
    if code > len(alphabet) - 1:
        code = code - len(alphabet)

    if code < 0:
        code = code + len(alphabet)
    
    return code

def crypt(word: str, key: int):
    wordIndexes = getWordLettersRankIntoList(word)
    wordCyptedIndexes = []
    res = ""
    for index in wordIndexes:
        wordCyptedIndexes += [calculateCode(index,key)]
    
    for index in wordCyptedIndexes:
        res += alphabet[index]

    return res

def decrypt(cryptedWord: str, key: int):
    return crypt(cryptedWord,-key)