amount = 50
while amount > 0:
    coin = 0
    while coin != 25 and coin != 10 and coin != 5:
        print(f"Amount due: {amount}")
        coin = int(input("Insert coin: "))
    amount = amount - coin
if amount == 0:
    print("Change owed: 0")
else:
    amount = -amount
    print(f"Change owed: {amount}")
