d = {}
while True:
    try:
        item = input().upper()
        if item in d:
            d[item] = d[item] + 1
        else:
            d[item] = 1
    except EOFError:
        break

d = dict(sorted(d.items()))

for item in d:
    print(d[item], item)
