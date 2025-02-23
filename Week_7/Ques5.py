number = int(input('Enter a number : '))
a = 0
b = 1
if number <= 0:
    print('Number Not allowed')
    exit()
for i in range(number):
    print(a, end=',')
    a, b = b, a+b
print('\n')