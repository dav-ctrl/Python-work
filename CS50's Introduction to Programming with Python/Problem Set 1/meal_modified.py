def main():
    time = input("What time is it? ")

    tiempo = time.replace("a.m.","")
    tiempo = tiempo.replace("p.m.","")
    t = convert(tiempo)

    if (7<=t<=8) and ("a.m." in time):
        print("Breakfast time")
    elif t>=12 and ("p.m." in time):
        print("Lunch time")
    elif t==1 and ("p.m." in time):
        print("Lunch time")
    elif 6<=t<=7 and ("p.m." in time):
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
