expression = input("Expression: ")

x, y, z = expression.split()

x = float(x)
z = float(z)

if y=="+":
    print(round(float(x + z),1))
elif y=="-":
    print(round(float(x-z),1))
elif y=="*":
    print(round(float(x*z),1))
elif y=="/" and z!=0:
    print(round(float(x/z),1))
else:
    print("Not valid")
