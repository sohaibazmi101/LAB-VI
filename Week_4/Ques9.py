def numberOfUpperAndLower(str):
    upper = 0
    lower = 0
    for c in str:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
    
    print(f"Upper Letter is : {upper}")
    print(f"Lower Letter is : {lower}")

str = input('Enter a string value : ')
numberOfUpperAndLower(str)