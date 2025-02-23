number_list = []
odd_list = []
even_list = []
for i in range(1,10):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list,'\n', odd_list)

number_list = odd_list+even_list
print(number_list)
number_list.sort()
print('Sorted Array : ', number_list)