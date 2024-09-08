def main():
    word = input("")
    convert(word)

def convert(word):
    word = word.replace(":)", "🙂")
    word = word.replace(":(", "🙁")
    print(word)

main()
