import sys

if len(sys.argv) == 2:
    try:
        name, extension = sys.argv[1].split(".")
        if extension != "py":
            print("Not a Python file")
        else:
            try:
                with open(sys.argv[1]) as file:
                    i = 0
                    for line in file:
                        line = line.lstrip()
                        if line.startswith("#") or line == "":
                            pass
                        else:
                            i += 1
                    print(i)
            except FileNotFoundError:
                print("File does not exist")
    except ValueError:
        print("Not a Python file")
elif len(sys.argv) < 2:
    print("Too few command-line arguments")
else:
    print("Too many command-line arguments")
