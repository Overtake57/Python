#Systeme immorale pour un eleve
def noteCalc():
    if calc >= 16 and calc <=20 :
        print("Très bien",calc)
    if calc >= 12 and calc < 16:
        print("Bien", calc)
    if calc >= 8 and calc < 12 :
        print("Assez bien", calc)
    if calc >=4 and calc < 8 :
        print("Insuffisant", calc)
    if calc >= 0 and calc < 4 :
        print ("Nul", calc)
        
note1 = int(input("Veuillez entrer la note de français: "))
note2 = int(input("Veuillez entrer la note de math: "))
note3 = int(input("Veuillez entrer la note de géometrie: "))
note4 = int(input("Veuillez entrer la note de informatique: "))

calc = (note1 + note2 + note3 + note4) / 4
noteCalc()



