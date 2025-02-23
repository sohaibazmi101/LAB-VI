def find_recursion(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return find_recursion(number-1) + find_recursion(number-2)

number = int(input('Enter a number : '))
print('Series : ')
for i in range(number):
    print(find_recursion(i), end=',')
print('\n')