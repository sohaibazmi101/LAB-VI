number_list = []
for i in range(20):
    number_list.append(i+1)
print("Original List : ",number_list)
even = []
odd = []
for i in range(len(number_list)):
    if number_list[i] % 2 == 0:
        even.append(number_list[i])
    else:
        odd.append(number_list[i])
print("Odd List : ",odd)
print("Even List",even)