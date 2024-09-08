def main():
    dol = dollars(input("How much was the meal? "))
    per = percentage(input("What percentage would you like to tip? "))
    tip = dol * per
    print(f"Leave ${tip:.2f}")

def dollars(d):
    d = d.replace("$", "")
    d = float(d)
    return d

def percentage(p):
    p = p.replace("%", "")
    p = float(p) / 100
    return p

main()
