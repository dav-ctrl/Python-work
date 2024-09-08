word = input("Input: ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]
print("Output: ", end="")

for c in word:
    if c not in vowels:
        print(c, end="")
