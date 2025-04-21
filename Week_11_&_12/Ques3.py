text = input("Enter a String : ")
histogram = {}

for char in text:
    if char.isalpha(): 
        char = char.lower()
        histogram[char] = histogram.get(char, 0) + 1

print("\nLetter Frequency Histogram:")
for letter in sorted(histogram.keys()):
    print(f"{letter}: {histogram[letter]}")