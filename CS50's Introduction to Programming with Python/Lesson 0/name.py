# Ask the user's name
name = input("What's your name? ").strip().title()

# Remove whitespaces and capitalize user's name
name = name.strip().title()

# First and last name
first, last = name.split(" ")

# Say hello to the user
print("hello,", end=" ")
print(first)
print("hello,", first)
print("hello, " + first )
print(f"hello, {first}")
