data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30
}

value = input("Enter a value to search for: ")

try:
    value = int(value)
except ValueError:
    print("Please enter a valid number.")
    exit()

found_keys = [key for key, val in data.items() if val == value]

if found_keys:
    print(f"Keys with value {value}: {found_keys}")
else:
    print(f"No keys found with value {value}.")
