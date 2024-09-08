while True:
    try:
        fraction = input("Fraction: ")
        numbers = fraction.split("/")
        x = int(numbers[0])
        y = int(numbers[1])
        if x > y:
            pass
        elif x/y > 0.99:
            print("F")
            break
        elif x/y < 0.01:
            print("E")
            break
        else:
            per = int(x*100/y)
            print(f"{per}%")
            break
    except (ValueError,ZeroDivisionError):
        pass
