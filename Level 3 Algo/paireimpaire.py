def isEven(n:float) ->bool:
    """
    Vérifie si un nombre est paire.
    """
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input("Saisir un nombre: " ))

if isEven(n):
    print(f"Le nombre {n} est paire.")

else:
    print(f"Le nombre {n} est impaire.")