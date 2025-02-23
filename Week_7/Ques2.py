number = int(input('Enter a number : '))
if number < 0:
    print('Negative value is not allowed')
    exit()
fact = 1;
for i in range(2, number + 1):
    fact *= i
print(f'Factorial of number is : {fact}')