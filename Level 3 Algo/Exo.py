# Palindrome

def isPalindrome(str):
    
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
yourWord = input("Votre mot: ")
answer = isPalindrome(yourWord)
 
if (answer):
    print("Oui c'est un palindrome")
else:
    print("Non ce n'est pas un palindrome")