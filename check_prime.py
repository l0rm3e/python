import math
number = int(input("Number to be checked: "))

def is_prime(num):
    if num <= 1:
        return false
    elif num == 2:
        return true
    for i in range(3,int(math.sqrt(num))):
        if(num % i == 0):
            return false
        else:
            return true

if is_prime(number):
    print(str(number) + " is prime")
else:
    print(str(number) + " is not prime")
