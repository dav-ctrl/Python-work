def main():
    time = input("What time is it? ")

    time = convert(time)

    if 7<=time<=8:
        print("Breakfast time")
    elif 12<=time<=13:
        print("Lunch time")
    elif 18<=time<=19:
        print("Dinner time")

def convert(t):
    hour, min = t.split(":")
    hour = float(hour)
    min = float(min)
    minute = round(float(min/60),2)
    rel = hour+minute
    return rel

if __name__ == "__main__":
    main()
