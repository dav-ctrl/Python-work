import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            pass
        else:
            number = random.randint(1, level)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess < 1:
                        pass
                    else:
                        if guess == number:
                            print("Just right!")
                            break
                        elif guess > number:
                            print("Too large!")
                        else:
                            print("Too small!")
                except ValueError:
                    pass
    except ValueError:
        pass
