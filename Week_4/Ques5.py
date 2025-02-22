def sumOfDigits(number):
    remainder = 0;
    sum = 0
    while number:
        remainder = number % 10
        number = number // 10
        sum = sum + remainder
    return sum

number = int(input('Enter any digit of number : '))
print(f'Sum of digits of {number} is {sumOfDigits(number)}')