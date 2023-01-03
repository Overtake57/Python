import random
import os
# movies = []
# years = []

# for i in range(0,4):
#     movies += [input("Saisir le titre d'un film : ")]
#     years += [input(f"Saisir l'année de sortie de \"{movies[i]}\" : ")]

movies = ["Titanic","LOL","Star wars VI","300","Avatar"]
years = [1990,2008,1976,2010,2005]

# movies = ["Ant Bully, The","Can't Help Singing","Fire Down Below","Ryan","Angels & Demons","The Nativity","Mephisto","Howards End","Coquette","Nixon","Faithless (Trolösa)","Beyond Hypothermia (Sip si 32 doe)","Crocodile Dundee in Los Angeles","Secret Sunshine (Milyang)","Leprechaun 2","Mad Adventures of Rabbi Jacob, the (Les Aventures de Rabbi Jacob)","Employee of the Month","If I Were You (Se Eu Fosse Você)","Chill Out! (Descongélate!)","Lilian's Story","Circus of Horrors","Enforcer, The","Midsummer Night's Dream, A","Grim Reaper","I Can't Think Straight","Our Man Flint","Fear Me Not (Den du frygter)","Scusa ma ti chiamo amore","Bombshell","99 River Street","Miehen tie","Blood of Redemption","Welcome to the Space Show (Uchû shô e yôkoso)","Toronto Stories","Boo to You Too! Winnie the Pooh","Separate Tables","Just Like Heaven","New Wave, A","Black Cauldron, The","Studentfesten","Guest from the Future (Gostya iz buduschego)","Omar Killed Me (Omar m'a tuer)","State Property","Imagine That","Blue","Godzilla vs. Megaguirus (Gojira tai Megagirasu: Jî shômetsu sakusen)","Round Up, The (La Rafle)","51","Touchback","First Time, The","Jesus Camp","Wrestling for Jesus: The Tale of T-Money","Piece of the Action, A","Devil and Max Devlin, The","Wog Boy, The","Year of the Horse","Medicine Man","Dance Party, USA","Brothers Bloom, The","Shut Up & Sing","At Play in the Fields of the Lord","Pornographers, The (Erogotoshi-tachi yori: Jinruigaku nyûmon)","Fool for Love","Back to Bataan","Culture High, The","It Started in Naples","Art and Craft","Rurouni Kenshin (Rurôni Kenshin: Meiji kenkaku roman tan)","Man with a Cloak, The","Advantageous","Management","Love Song for Bobby Long, A","Me and you (io e te)","Centenarian Who Climbed Out the Window and Vanished, The (Hundraåringen som klev ut genom fönstret och försvann)","Young Lions, The","Bloody Child, The","To Do List, The","Searchers, The","Tyler Perry's Daddy's Little Girls","Mary and Martha","Killing Machine, The (Icarus)","Service (Serbis)","Inquisitor, The (a.k.a. Under Suspicion) (Garde à vue)","Babysitting","Drive","He Ran All the Way","Man from Nowhere, The (Ajeossi)","Vincent: A Life in Color","Boys Life 4: Four Play","Diary of a Wimpy Kid: Dog Days","Charlie Chan in the Secret Service","We Bought a Zoo","Futurama: Bender's Game","Winter Break","Duchess of Langeais, The (a.k.a. Don't Touch the Axe) (Ne touchez pas la hache)","Far and Away","At Any Price","Patience (After Sebald)","Lady Vengeance (Sympathy for Lady Vengeance) (Chinjeolhan geumjassi)","Road Warrior, The (Mad Max 2)"]
# years = [2005,2006,2003,1992,1993,2012,2007,1982,2001,1993,1994,2008,2008,1992,2003,1997,2009,2006,2009,2011,1999,1989,2003,1990,2013,2009,2000,1993,1993,2007,2007,2012,1993,1985,2007,2007,2002,2000,2009,1984,2004,2010,2002,1986,2008,1995,2010,2009,2011,1996,2001,2011,2011,1998,1992,1997,2012,1991,2011,1997,1996,2008,1985,1985,2001,1973,2011,2005,2010,1998,2004,2007,1995,2011,2008,1994,1985,2004,2004,1994,1999,1998,2003,1995,2007,2004,2010,2010,2011,1992,2007,2007,1991,2007,2008,2011,1997,1995,2001,2012]

menu = ["Quitter","Afficher tous les films"] + [f"Afficher l'année de sortie du film {movie}" for movie in movies] + ["Lancer le Quizz"]

choice = 1
while choice != 0:
    for (index,menuItem) in enumerate(menu):
        print(f"{index}. {menuItem}")
    choice = int(input("Votre choix : "))
    if choice == 1:
        os.system("cls")
        res = ""
        for movie in movies:
            res += f"{movie}\n"
        print(res)
    elif choice >= 2 and choice < len(menu) - 1:
        os.system("cls")
        print("\n-------------------------------------------------------------")
        print(f"Le film {movies[choice-2]} est sorti en {years[choice-2]}.")
        print("-------------------------------------------------------------\n")
    elif choice == len(menu) - 1: # Quizz
        score = 0
        movieIndexesKnown = []
        for i in range(0,len(movies)):
            # Tirage d'un film au hasard
            randomMovieIndex = random.randint(0, len(movies) - 1)
            while randomMovieIndex in movieIndexesKnown:
                randomMovieIndex = random.randint(0, len(movies) - 1)
            movieIndexesKnown += [randomMovieIndex]

            # On stock la bonne réponse (la bonne année)
            goodAnswer = years[randomMovieIndex]

            # On genère 3 choix d'année aléatoire
            randomYears = []
            for i in range(0,3):
                randomYear = random.randint(1870,2022)
                while randomYear in randomYears:
                    randomYear = random.randint(1870,2022)
                randomYears += [randomYear]

            # On ajoute ces 3 années au tableau de réponses possibles
            choices = [goodAnswer] + randomYears

            # On affiche la question et les choix
            print(f"En quelle année est sortie le film {movies[randomMovieIndex]} ?")
            letters = ["A","B","C","D"]
            random.shuffle(choices)
            for j in range(0, len(choices)):
                print(f"{letters[j]}. {choices[j]}")

            # On analyse la réponse
            answer = "Z"
            while answer not in letters:
                answer = input("Votre réponse : ").upper()

            # On traite le score
            if choices[letters.index(answer)] == goodAnswer:
                score += 1
        os.system("cls")
        print(f"Votre score est de {score}/{len(movies)}")
        
    
