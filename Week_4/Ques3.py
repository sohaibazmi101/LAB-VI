import math

def areaOfCircle(radius):
    return math.pi * (radius ** 2)
radius = float(input('Enter the radius of circle : '))
print(f'Area is : {areaOfCircle(radius)}')