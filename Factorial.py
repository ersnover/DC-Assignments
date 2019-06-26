#returns the factorial of a number
def getnum():
    num = int(input("Enter a number to find its factorial: "))
    return num

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

def printfact(num, fact):
    print(f'{num}! = {fact}')

num = getnum()
fact = factorial(num)
printfact(num, fact)