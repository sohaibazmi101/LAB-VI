data = "Pyhton rules!"
split_word = data.split()
uppercase_data = data.upper()
position = data.find("rules")
char_pos = data.find('o')
replaced = data.replace('!', '?')

print("List of Words : ", split_word)
print("Upper case data : ", uppercase_data)
print("Position of rules : ",position)
print("Position of char 'o' : ",char_pos)
print("Replaced Data : ", replaced)