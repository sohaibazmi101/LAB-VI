my_dict = {'apple': 10, 'banana': 5, 'cherry': 15, 'date': 7}

ascending_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("Ascending order by value:")
print(ascending_sorted)

descending_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("\nDescending order by value:")
print(descending_sorted)
