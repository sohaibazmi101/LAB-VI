number = int(input('Enter any digit of Integer : '))
remainder = 0
sum = 0
count = 0
temp = number
num = number
while temp != 0:
    remainder = temp % 10
    temp = temp // 10
    count += 1
while number != 0:
    remainder = number % 10
    number = number // 10
    sum = sum + (remainder**count)
if(sum == num):
    print(f'{num} is Armstrong')
else:
    print(f'{num} is not Armstrong')