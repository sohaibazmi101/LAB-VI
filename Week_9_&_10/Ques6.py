numbers = [10, 20, 30, 40, 50]

search_element = int(input("Enter the number to search: "))

if search_element in numbers:
    index = numbers.index(search_element)
    print(f"{search_element} found at index {index}")
else:
    print(f"{search_element} not found in the list.")

