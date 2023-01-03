"""
Écrire un programme qui permet d'afficher l'index d'un prénom saisi par l'utilisateur dans un tableau :
"""

def find_in_list(target,list):
    
  target_indices = []
  
  for i in range(len(name)):
      
    if name[i] == target:
        
      target_indices.append(i)  
      
  if target_indices == []:
      
    print("Eleve non présent!")
    
  else:
      
    print(f"{target} Eleve présent! {target_indices}")
    
    
name = ['Hugo', 'Flora', 'JP', 'Céline']

target = input("Ecrire le prénom de l'eleve: ")

find_in_list(target,name)
    
    
    
    
    
    



















                                                            # Other
# trouver l'index de Hugo dans le tableau "student

'''
def search(list, student):
    
    for i in range(len(list)):
        
        if list[i] == student:
            
            return True
        
    return False



name = ['Hugo', 'Flora', 'JP', 'Céline']

student = input("Ecrire le prénom de l'eleve: ")

if search(name, student):
    
    print(f"{name} est présent {name}")
    
else:
'''  
  
    
'''
import os

student = []

menu = ["Quitter","Afficher tous les prénoms"]

numberStudent = int(input("Combien d'étudiant souhaitez-vous ajouter ? "))

for i in range(0, numberStudent):

    student += [input("Saisir le prénom: ").lower()]

choice = 1

while choice != 0:

    for (index,menuItem) in enumerate(menu):

        print(f"{index}. {menuItem}")

    choice = int(input("Votre choix : "))

    if choice == 1:

        os.system("cls")

        res = ""

        for student in student:

            res += f"{student}\n"

        print(res)
'''