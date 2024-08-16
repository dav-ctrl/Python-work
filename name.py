# Ask the user's name
name = input("What's your name? ").strip().title()

# Remove whitespaces and capitalize user's name
name = name.strip().title()

# First and last name
first, last = name.split(" ")

# Say hello to the user
print(f"hello, {first}")