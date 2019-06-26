#will check whether a number is prime

def getnum():
    num = int(input("Enter a number: "))
    return num

def decideprime(num):
    isprime = False
    if num >=2:
        if num == 2:
            isprime = True
        else:
            for i in range(2,int(num/2)):
                if num % i == 0:
                    break
            else: isprime = True
    return num, isprime

def PrintDec(num, isprime):
    if isprime == True:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

number = getnum()
num, isprime = decideprime(number)
PrintDec(num, isprime)