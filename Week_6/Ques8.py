random_list = [1, 3, 'a', 'n', 10, 12, 'c', 11, 14, 'y', 3.2, 9.01, 'q']
sumOfNum = sum(num for num in random_list if isinstance(num, (int, float)))
print(f'Sum is {sumOfNum}')