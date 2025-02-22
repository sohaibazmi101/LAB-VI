num1 = int(input('Enter first number : '))
num2 = int(input('Enter Second number : '))

a = num1
b = num2
while num2:
    num1, num2 = num2, num1 % num2

print(f"GCD of {a} and {b} is {num1}")
