month = int(input('Enter month number : '))
if month < 0 or month > 12:
    print('Invalid Month Input')
    exit()
if (month % 2 != 0 and month < 8) or (month % 2 == 0 and month > 7):
    print(f'{month} have 31 days')
elif (month % 2 == 0 and month < 8 and month != 2) or (month % 2 != 0 and month > 7 and month != 2):
    print(f'{month} have 30 Days')
elif month == 2:
    print(f'{month} have 28 or 29 days')