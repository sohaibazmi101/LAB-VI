num = int(input('Enter a number : '))
count = 0;
for i in range(2, num -1):
    if num % i:
        count += 1
if count == 0:
    print('Number is prime.')
else:
    print('Not  prime number.')
    print("Factors Are : ")
    for i in range(2,num):
        if num % i == 0:
            print(f"{i} ")