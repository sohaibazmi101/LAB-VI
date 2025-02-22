def avg():
    n1 = int(input('Enter first number : '))
    n2 = int(input('Enter second number : '))
    n3 = int(input('Enter third number : '))
    n4 = int(input('Enter fourth number : '))
    n5 = int(input('Enter fifth number : '))

    return (n1 + n2 + n3 + n4 + n5) / 5

def convert_cel():
    value = float(input('Enter value of temparature in celcius : '))
    return (value * 9/5) + 32

def perimeter():
    length = float(input('Enter the length of Rectangle : '))
    breadth = float(input('Enter the breadth of rectangle : '))
    return 2 *(length + breadth)

while True:
    print('1. Average for five integers : ')
    print('2. Temparature conversion : ')
    print('3. Perimeter of rectangle : ')
    print('4. Exit')
    choice = int(input('Enter your Choice : '))

    if choice == 1:
        print(avg())
    elif choice == 2:
        print(convert_cel())
    elif choice == 3:
        print(perimeter())
    elif choice == 4:
        break
    else:
        print("Enter correct Choice")