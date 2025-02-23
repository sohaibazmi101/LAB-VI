year = int(input(f'Enter year in four digit : '))
if year < 1000:
    print('Enter year in four digit')
    exit()
if year % 4 == 0 and year > 999:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')