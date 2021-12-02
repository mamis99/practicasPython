def max(a,b):
    return a > b
"""    if a > b:
        return True
    else:
        return False"""
a = int(input("Type a first number: "))
b = int(input("Type a second number: "))
if max(a, b):
    print("First number is bigger than second")
elif not max(a, b):
    print("Second number is bigger than first")