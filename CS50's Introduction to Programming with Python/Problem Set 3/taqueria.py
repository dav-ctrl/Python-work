menu = {"Baja Taco": 4.25, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00, "Quesadilla": 8.50,
    "Super Burrito": 8.50, "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00}

sum = round(float(0),2)
while True:
    try:
        item = input("Item: ")
        item = item.title()
        for meal in menu:
            if meal == item:
                sum += menu[meal]
                print(f"${sum:.2f}")
    except EOFError:
        break
    except KeyError:
        pass
