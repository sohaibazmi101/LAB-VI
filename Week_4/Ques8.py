import math
def checkPrime(number):
    count = 0
    if number < 0:
        print('Negative not allowed')
        return
    elif number == 1:
        return False
    elif number == 0:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if(number % i == 0):
            count = count + 1
    if count == 0:
        return True
    else:
        return False
    
nmber = int(input('Enter a positive integer : '))
print(f'Is {nmber} Prime ? {checkPrime(nmber)}')