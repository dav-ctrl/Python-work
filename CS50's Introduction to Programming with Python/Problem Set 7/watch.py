import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"^<iframe(?:.+)?src=\"((?:https?://)(?:www\.)?youtube\.com/embed/[a-zA-Z0-9]+)\"(?:.+)?></iframe>$",s)
    if matches:
        url = matches.group(1).replace("youtube","youtu.be")
        return url

if __name__ == "__main__":
    main()
