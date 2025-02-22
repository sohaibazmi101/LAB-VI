import math

def volumeOfSphere(radius):
    return 4/3 * math.pi * (radius ** 3)

radius = float(input('Enter the radius of sphere : '))
print(f'Volume is : {volumeOfSphere(radius)}')
print(f'Volume of sphere when radius is 5 is {volumeOfSphere(5)}')