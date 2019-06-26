#Tells user whether or not a string is a palindrome
def getstring():
    stringOG = input("Enter a word or phrase: ")
    string = stringOG.replace(" ","")
    return string, stringOG

def decision(string, stringOG):
    pal = True
    for i in range(0,len(string)):
        if string[i] != string[len(string)-1-i]:
            print(f"{stringOG} is not a palindrome")
            pal = False
            break
    if pal == True:
        print(f"{stringOG} is a palindrome")
    
    
        

string, stringOG = getstring()
decision(string, stringOG)