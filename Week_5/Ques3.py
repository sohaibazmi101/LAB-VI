def removeOfChar(strings):
    temp = ""
    for char in strings:
        if char % 2 == 0:
            temp = temp + strings[char]
    return temp

strings = input('Enter a String : ')
print(f'Original {strings} : Removed of Odd Char {removeOfChar(strings)}')