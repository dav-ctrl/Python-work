import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pm=["1","13","2","14","3","15","4","16","5","17","6","18","7","19","8","20","9","21","10","22","11","23","12","12"]
    matches = re.search(r"([0-9]+(?:\:[0-9]+)? (?:AM|PM)) to ([0-9]+(?:\:[0-9]+)? (?:AM|PM))", s)
    if matches:
        hour1, time1 = matches.group(1).split()
        hour2, time2 = matches.group(2).split()
        if time1 == "PM":
            if ":" in hour1:
                h1, min1 = hour1.split(":")
                if 0 <= int(min1) <= 59:
                    i = pm.index(h1)
                    h1 = pm[i+1]
                    result = f"{h1}:{min1} to "
                else:
                    raise ValueError("Not a valid hour")
            else:
                i = pm.index(hour1)
                hour1 = pm[i+1]
                result = f"{hour1}:00 to "
        else:
            if ":" in hour1:
                h1, min1 = hour1.split(":")
                if 0 <= int(min1) <= 59:
                    if h1 != 12:
                        result = f"{h1}:{min1} to "
                    else:
                        result = f"00:{min1} to "
                else:
                    raise ValueError("Not a valid hour")
            else:
                if hour1 != 12:
                    result = f"{hour1}:00 to "
                else:
                    result = f"00:00 to "
        if time2 == "PM":
            if ":" in hour2:
                h2, min2 = hour2.split(":")
                if 0 <= int(min2) <= 59:
                    i = pm.index(h2)
                    h2 = pm[i+1]
                    result = result + f"{h2}:{min2}"
                else:
                    raise ValueError("Not a valid hour")
            else:
                i = pm.index(hour2)
                hour2 = pm[i+1]
                result = result + f"{hour2}:00"
        else:
            if ":" in hour2:
                h2, min2 = hour1.split(":")
                if 0 <= int(min2) <= 59:
                    if h2 != 12:
                        result = result + f"{h2}:{min2}"
                    else:
                        result = result + f"00:{min2}"
                else:
                    raise ValueError("Not a valid hour")
            else:
                if hour2 != 12:
                    result = result + f"{hour2}:00"
                else:
                    result = result + f"00:00"
    else:
        raise ValueError("Not a valid format")
    return result

if __name__ == "__main__":
    main()

