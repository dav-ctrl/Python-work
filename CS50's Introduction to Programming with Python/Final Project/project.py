import sys
import re
from currency_converter import CurrencyConverter
import inflect

def main():
    try:
        nbm = get_name_bank()
        currencies = ["USD", "EUR", "JPY", "GBP", "AUD"]
        p = inflect.engine()
        list = p.join(currencies)
        print(f"Available currencies: {list}")
        money = None
        currency1 = get_currency(money, currencies)
        money = int(input(f"How many {currency1}? "))
        if money < 0:
            sys.exit("Not a valid number")
        list = p.join(currencies)
        print(f"Available currencies: {list}")
        currency2 = get_currency(money, currencies)
        money = convertion(money, currency1, currency2)
        nbm.append(money)
        nbm.append(currency2)
        print(final(*nbm))
    except ValueError:
        sys.exit("Not an integer")

def get_name_bank():
    while True:
        try:
            name, bank = input("Especify your name and bank separated by a comma: ").split(",")
            bank = bank.lstrip()
            if validate_name(name):
                break
            else:
                print("Not a valid name")
                raise ValueError
        except ValueError:
            print("Not a valid input")
    return [name, bank]

def validate_name(name):
    matches = re.search(r"^([a-zA-Z]+) ([a-zA-Z]+)$", name)
    if matches:
        return True
    else:
        return False

def get_currency(money, currencies):
    if money == None:
        while True:
            currency = input("Initial currency: ")
            if currency in currencies:
                return currency
    else:
        while True:
            currency = input("Currency to convert the money: ")
            if currency in currencies:
                return currency

def convertion(money, currency1, currency2):
    c = CurrencyConverter()
    new_money = c.convert(money, currency1, currency2)
    return new_money

def final(name, bank, money, currency2):
    name = name.upper()
    bank = bank.upper()
    return f"{name} has {money} {currency2} in bank {bank}"

if __name__ == "__main__":
    main()
