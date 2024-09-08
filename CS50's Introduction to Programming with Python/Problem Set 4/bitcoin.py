import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    n = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    price = o["bpi"]["USD"]["rate_float"]
    amount = price * n
    print(f"${amount:,.4f}")
except ValueError:
    sys.exit("Command-line is not an argument")
except requests.RequestException:
    pass
