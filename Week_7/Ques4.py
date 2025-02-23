def factorial(number):
    if(number < 0):
        return
    elif number == 0:
        return 1
    fact = number
    fact = fact * factorial(number - 1)
    return fact

number = int(input('Enter a number : '))
print(f'Factorial of {number} is : {factorial(number)}')