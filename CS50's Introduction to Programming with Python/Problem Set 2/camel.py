camel = input("camelCase: ")
print("snake_case: ", end="")
for c in camel:
    if c.isupper():
        c = c.lower()
        print("_" + c, end="")
    else:
        print(c, end="")
