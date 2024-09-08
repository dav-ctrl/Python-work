def main():
    text = input("Input: ")
    text_mod = shorten(text)
    print(text_mod)

def shorten(word):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for c in word:
        if c in vowels:
           word = word.replace(c,"")
    return word

if __name__ == "__main__":
    main()
