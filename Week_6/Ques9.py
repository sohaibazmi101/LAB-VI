num_list = [3,2,31,7,5,4,5,6,34,6,9,56,34,2,3,5]
count = 0
for i in range(len(num_list) - 1):
    if num_list[i]+1 == num_list[i+1]:
        count += 1
        print(f'Consecutive number found {num_list[i]} and {num_list[i+1]}')
if count == 0:
    print('No consecutive number in list')