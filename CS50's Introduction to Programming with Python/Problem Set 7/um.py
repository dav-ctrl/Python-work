import re

def main():
    print(count(input("Text: ")))

def count(s):
    matches = re.findall(r"(Um\b|\bum\b)",s)
    return(len(matches))

if __name__ == "__main__":
    main()
