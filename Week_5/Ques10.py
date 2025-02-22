def count_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    vowel_list = []

    for char in text:
        if char in vowels:
            vowel_count += 1
            vowel_list.append(char)

    return vowel_count, vowel_list
text = input("Enter a text: ")
count, vowels = count_vowels(text)

print(f"Total Vowels: {count}")
print(f"Vowels Found: {' '.join(vowels)}")
