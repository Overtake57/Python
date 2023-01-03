
def poser_question(question, r1, r2, r3, r4, choix_bonne_reponse):
    print(question)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print()
    reponse = input("Votre réponse : ")
    if reponse == choix_bonne_reponse:
        print("Bonne réponse")
    else:
        print("Mauvaise réponse")

    poser_question("Question : Quelle est la capitale de la France? ", "(a) Marseille", "(b) Nice", "(c) Paris", "(d) Nante", "c")