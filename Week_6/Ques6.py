import math
a = float(input('Enter the first side of Triangle : '))
b = float(input('Enter the second side of Triangle : '))
c = float(input('Enter the third side of Triangle : '))

if a == b == c:
    print('Equilateral Triangle')
elif a != b and b != c and c != a:
    print('Scalene Triangle')
else:
    print('Isosceles Triangle')
s = (a + b + c) / 2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(f'Area of triangle is {area}')