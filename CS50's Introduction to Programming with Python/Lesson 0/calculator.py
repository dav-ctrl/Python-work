# Integer
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)

# Float
x = float(input("What's x? "))
y = float(input("What's y? "))
print(x + y)

# Round
x = float(input("What's x? "))
y = float(input("What's y? "))
print(round(x,2))
print(round(y,2))
print(round(x,2)+round(y,2))
print(round(x+y,2))

# Commas
x = float(input("What's x? "))
y = float(input("What's y? "))
z=round(x+y)
print(f"{z:,}")

# Division
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x/y,2)
print(z)
z = x / y
print(f"{z:.2f}")
