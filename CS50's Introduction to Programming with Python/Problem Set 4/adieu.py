import inflect

names = []
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break

p = inflect.engine()
list_names = p.join(names)

print("Adieu, adieu, to " + list_names)
