number_list = [3,1,7,6,3,0,6,45,34,12,13,89,54,89,89,89,13,13]
sorted(number_list)
length = len(number_list)
print(length)
print(number_list)

list.sort(number_list)
print(number_list)
for i in range(length-1, -1, -1):
    if number_list[length - 1] != number_list[i]:
        print(f'Second Largest : {number_list[i-1]}')
        break