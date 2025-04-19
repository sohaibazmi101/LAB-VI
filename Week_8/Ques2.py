list1 = [1,2,3,4,5,8]
list2 = [4,5,6,7,8]
union_list = list1[:]
for item in list2:
    if item not in union_list:
        union_list.append(item)
print("UNION_LIST : ",union_list)