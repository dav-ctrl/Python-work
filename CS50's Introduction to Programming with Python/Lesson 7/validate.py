import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$",email):
    print("Valid")
else:
    print("Invalid")

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):
    print("Valid")
else:
    print("Invalid")

if re.search(r"^\w+@(\w+\.)?+\.(edu|com|es)$",email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

if re.search(r"^(\w|\.)+@(\w+\.)?+\.(edu|com|es)$",email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


