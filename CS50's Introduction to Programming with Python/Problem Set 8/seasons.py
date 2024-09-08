from datetime import date
from datetime import timedelta
import sys
import re
import inflect

def main():
    birth = input("Date of birth: ")
    if validate(birth):
        minutes = get_minutes(birth)
        p = inflect.engine()
        print(f"{p.number_to_words(minutes, andword="").capitalize()} minutes")
    else:
        sys.exit("Invalid date")

def validate(s):
    matches = re.search(r"^([0-9]+)-([0-9]+)-([0-9]+)$", s)
    if matches:
        return True
    else:
        return False

def get_minutes(birth):
    try:
        y, m, d = birth.split("-")
        difference = date.today() - date(int(y),int(m),int(d))
        seconds = difference.total_seconds()
        minutes = int(seconds/60)
        return minutes
    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
