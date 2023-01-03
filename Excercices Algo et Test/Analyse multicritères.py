#Analyse multicritères*

mam = "mamifere"
ovi = "ovipare"
plum = "plume"
eca = "écaille"
no = "non"
yes = "oui"
water = "eau"
grass = "terre"
cat = "miaou"
dog = "wouah"

Q1 = input("L'animal est-il mammifère ou ovipare? ")
if Q1 == ovi :
    Q2 = input("s’il est ovipare, est-il à plume ou à écaille ?: ")
    if Q2 == plum :
        print("s’il est à plume, c’est un oiseau ! ")
        exit()
    elif eca :
        input("s’il est à écaille, vit-il dans l’eau ?: ")
        if no :
            print("s’il vit sur terre, c’est un reptile !")
            exit()
        elif yes :
            print("s'il vit dans l'eau, c'est un poisson !")
            exit()
if Q1 == mam :
    Q3 = input("si c’est un mammifère, vit-il dans l’eau ou sur terre ?: ")
    if Q3 == water :
        print("s’il vit dans l’eau, c’est un cétacé!")
        exit()
    if Q3 == grass :
        Q4 = input("s’il vit sur terre, fait-il « miaou » ou « wouah-wouah » ?: ")
        if Q4 == cat : 
            print("s’il fait « miaou », c’est un chat !")
            exit()
        elif Q4 == dog :
            print("s’il fait « miaou », c’est un chien !")
            exit()
    
    