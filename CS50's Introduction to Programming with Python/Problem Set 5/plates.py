def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        j, i = first_number(s)
        if s[0].isnumeric() or s[1].isnumeric() or j==0 or no_letters(s,i) == False or letters_numbers(s) == False:
            return False
        else:
            return True
    else:
        return False

def first_number(s):
    for i in range(len(s)):
        if s[i].isnumeric():
            j = int(s[i])
            return j, i

def letters_numbers(s):
    i = 0
    k = 1
    while i <= len(s)-1 and k != 0:
        if s[i].isnumeric() or s[i].isalpha() == True:
            i += 1
        else:
            k = 0
    if k == 0:
        return False
    else:
        return True

def no_letters(s,i):
    k = 1
    while i <= len(s)-1 and k != 0:
        if s[i].isnumeric():
            i += 1
        else:
            k = 0
    if k == 0:
        return False
    else:
        return True

if __name__ == "__main__":
    main()
