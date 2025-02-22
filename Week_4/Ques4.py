def factorial(number):
    fact = 1
    if number < 0:
        print('Negative number not allowed')
        return
    for i in range(2, number+1):
        fact = fact * i
    return fact

number = int(input('Enter a umber : '))
print(f'Factorial is : {factorial(number)}')