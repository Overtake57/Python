'''
from random import *
# Tableau pour encadré un texte # 
def printHeader(title: str, char: str = "#", count: int = 1):
    tab = ["#","⚄","-","*","~","+"]
    if char == "":
        char = choice
    l = len(title)
    d = (l + count * 2 + 2) * char
    c = char * count
    print(d)
    print(f"{c} {title} {c}")
    print(d)
    '''
    