num = int(input('Enter a number to find the factorial : '))
if num < 0:
    print('Negative value is not allowed!!')
    exit()
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f'Factorial of {num} is : {fact}')