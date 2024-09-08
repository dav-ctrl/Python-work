months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
    "October", "November", "December"]
while True:
    try:
        date = input("Date: ")
        if date.count("/") == 2:
            date = date.split("/")
            if 1 <= int(date[0]) <= 12 and 1 <= int(date[1]) <= 31:
                print(f"{int(date[2])}-{int(date[0]):02}-{int(date[1]):02}")
            else:
                pass
        elif date.count(",") == 1:
            date = date.split()
            if "," in date[1] and date[0] in months:
                date[1] = date[1].replace(",","")
                for i in range(len(months)):
                    if date[0] == months[i-1]:
                        date[0] = i
                    else:
                        pass
                if 1 <= int(date[1]) <= 31:
                    print(f"{int(date[2])}-{int(date[0]):02}-{int(date[1]):02}")
                else:
                    pass
            else:
                pass
        else:
            pass
    except EOFError:
        break

