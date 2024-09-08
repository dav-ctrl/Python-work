word = input("Greeting: ")

if word.startswith("hello") or word.startswith("Hello"):
    print("$0")
elif word.startswith("h") or word.startswith("H"):
    print("$20")
else:
    print("$100")
