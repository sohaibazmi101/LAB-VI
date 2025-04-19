def first_last_2_chars(s):
    if len(s) < 2:
        return ''
    return s[:2] + s[-2:]
print(first_last_2_chars("Python"))
print(first_last_2_chars("Py"))
print(first_last_2_chars("P"))