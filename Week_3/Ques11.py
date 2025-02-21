import math
num = int(input('Enter a number to chek : '))
x1 = 5 * num * num + 4
x2 = 5 * num * num - 4
sqrt_x1 = int(math.sqrt(x1))
sqrt_x2 = int(math.sqrt(x2))
if x1 == sqrt_x1 * sqrt_x1 or x2 == sqrt_x2 * sqrt_x2:
    print(f'{num} is a fibonacci number.')
else:
    print(f'{num} is not a fibonacci number.')