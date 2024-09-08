def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(percentage))

def convert(fraction):
    numbers = fraction.split("/")
    x = int(numbers[0])
    y = int(numbers[1])
    if x > y:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    else:
        return int(x*100/y)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    elif 1 < percentage < 99:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
