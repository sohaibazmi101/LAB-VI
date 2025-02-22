num = int(input('Enter a number: '))

count = 0

# Check for prime
for i in range(2, num):
    if num % i == 0:
        count += 1

if count == 0:
    print('Number is prime.')
else:
    print('Not a prime number.')
    print("First Factor is:")
    for i in range(2, num):
        if num % i == 0:
            print(i)
            break
