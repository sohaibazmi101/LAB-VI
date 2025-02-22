def reverseString(strings):
    temp = ""
    for char in strings:
        temp = char + temp
    return temp

strings = input('Enter a strins : ')
print(f'Original {strings} : after reversal {reverseString(strings)}')