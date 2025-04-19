list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
int_list = []
for item in list2:
    if item in list1:
        int_list.append(item)
print("Intersection List : ", int_list)