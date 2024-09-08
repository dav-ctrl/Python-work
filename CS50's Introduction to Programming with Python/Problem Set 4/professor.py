import random

def main():
    level = get_level()
    correct = 0
    for i in range(10):
        x,y = generate_integer(level)
        j = 1
        while j <= 3:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == x+y:
                    correct += 1
                    break
                else:
                    print("EEE")
                    j += 1
            except ValueError:
                print("EEE")
                j += 1
        if j == 4:
            integer = x+y
            print(f"{x} + {y} = {integer}")
    print(f"Score: {correct}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
            else:
                pass
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(1,9)
        y = random.randint(1,9)
    elif level == 2:
        x = random.randint(10, 99 )
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError
    return x,y

if __name__ == "__main__":
    main()
