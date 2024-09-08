from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid usage")

try:
    if sys.argv[1] != "-f" and sys.argv[1]!= "--font":
        sys.exit("Invalid usage")
except IndexError:
    pass

if len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    text = input("Input: ")
    print("Output:")
    print(figlet.renderText(text))

if len(sys.argv) == 3 and sys.argv[2] in figlet.getFonts():
    figlet.setFont(font=sys.argv[2])
    text = input("Input: ")
    print("Output:")
    print(figlet.renderText(text))
elif len(sys.argv) == 3 and sys.argv[2] not in figlet.getFonts():
    print("Invalid usage")
