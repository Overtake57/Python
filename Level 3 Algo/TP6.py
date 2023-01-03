
# Input Utilisateur
inp1 = input("Votre premier mot: ").lower().replace(" ", "")
inp2 = input("Votre second mot: ").lower().replace(" ", "")
print("\n")
user_list1 = inp1.split()
user_list2 = inp2.split()
print('list: ', user_list1)
print('list: ', user_list2)
 
# Mixeur 
x = [inp1[i] for i in range(0,len(inp1))]
x.sort()
y = [inp2[i] for i in range(0,len(inp2))]
y.sort()
 
# Output Utilisateur
if (x == y):print("Ce sont des anagrammes")
else: print("Ce ne sont pas des anagrammes")