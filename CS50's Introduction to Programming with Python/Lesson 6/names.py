name = input("What's your name? ")

# Write
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

#
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# Read
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())

#
with open("names.txt", "r") as file:
    for line in file
    print("hello,", line.rstrip())

# Sorted

names = []

with open("names.txt", "r") as file:
    for line in file
        names.append(line.rstrip())

for name in sorted(names)
    print("hello,", name)

#

with open("names.txt", "r") as file:
    for line in sorted(file)
        print("hello,", line.rstrip())
