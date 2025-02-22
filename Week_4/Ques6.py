def perfectNumber(number):
    if(number < 0):
        return
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum = sum + i
    return sum == number

number = int(input('Enter a positive integer : '))
print(f"{number} Is perfect ? {perfectNumber(number)}")
# for i in range(1,1000):
#     print(f"{i} Is perfect ? {perfectNumber(i)}")
