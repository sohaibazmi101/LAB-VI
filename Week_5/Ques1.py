import math

def largestNumber(n1, n2, n3):
    if n1 == n2 == n3:
        print(f"{n1}, {n2} and {n3} are equals.")
        return
    elif n1 > n2 and n1 > n3:
        return n1
    elif n1 < n2 and n1 > n3:
        return n2
    else:
        return n3

def volumeOfCylinder(radius, height):
    return math.pi * radius *radius * height

def volumeOfCube(side):
    return side**3

def volumeOfRectBox(length, breadth, height):
    return length * breadth * height

def areaOfRectangle(length, breadth):
    return length * breadth

def circumferenceOfCircle(radius):
    return 2 * math.pi * radius

def exchangeTheValue(var1, var2):
    temp = var1
    var1 = var2
    var2 = temp
    return var1, var2

def distanceBetweenTwoPoints(point1, point2):
    return math.dist(point1, point2)

while True:
    print('1. Largest of Three numbers')
    print('2. Volume of Cylinder')
    print('3. Volume of Cube')
    print('4. Volume of Rectangular Box')
    print('5. Area of Rectangle')
    print('6. Circumference of Circle')
    print('7. exchange the variable')
    print('8. Distance between Two points')
    print('9. Exit')
    choice = int(input('Enter YOUR CHOICE : '))
    if choice == 1:
        n1 = float(input('enter first number : '))
        n2 = float(input("enter first number : "))
        n3 = float(input('enter first number : '))
        print(f'Largest number is : {largestNumber(n1, n2, n3)}')
    elif choice == 2:
        radius = float(input('Enter the radius of cylinder'))
        height = float(input('Enter the height of cylinder'))
        print(f'Volume of cylinder is {volumeOfCylinder(radius, height)}')
    elif choice == 3:
        side = float(input('Enter the side of cube : '))
        print(f'Volume of Cube is {volumeOfCube(side)}')
    elif choice == 4:
        length = float(input('Enter the legth of box : '))
        breadth = float(input('Enter the breadth of box : '))
        height = float(input('Enter the height of box'))
        print(f'Volume of box is {volumeOfRectBox(length, breadth, height)}')
    elif choice == 5:
        leng = float(input('Enter the length of Rectangle : '))
        bread = float(input('Enter the breadth of Rectangle : '))
        print(f'Area of Rectangle is {areaOfRectangle(leng, bread)}')
    elif choice == 6:
        rad = float(input('Enter the Radius of circle : '))
        print(f'Circumference of circle is {circumferenceOfCircle(rad)}')
    elif choice == 7:
        var1 = input('Enter the value of variable 1 : ')
        var2 = input('Enter the value of variable 2 : ')
        print(f'Variable {var1} is exchange to variable {var2} : {exchangeTheValue(var1, var2)}')
    elif choice == 8:
        x1 = float(input('Enter the value of X1 : '))
        y1 = float(input('Enter the value of Y1 : '))
        x2 = float(input('Enter the value of X2 : '))
        y2 = float(input('Enter the value of Y2 : '))
        point1 = (x1, y1)
        point2 = (x2, y2)
        print(f"Distance between point {point1} and point {point2} is : {distanceBetweenTwoPoints(point1, point2)}")
    elif choice == 9:
        break
    else:
        print('Inavlid Choice! Please enter correct Choice')