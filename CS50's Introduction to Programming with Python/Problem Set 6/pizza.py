import sys
import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        name, extension = sys.argv[1].split(".")
        if extension != "csv":
            sys.exit("Not a CSV file")
        else:
            try:
                with open(sys.argv[1]) as file:
                    i = 0
                    table = []
                    for line in file:
                        if i == 0:
                            pizza, small, large = line.rstrip().split(",")
                            headers = [pizza,small,large]
                            i = 1
                        else:
                            pizza, small, large = line.rstrip().split(",")
                            table.append([pizza,small,large])
                    print(tabulate.tabulate(table, headers, tablefmt="grid"))
            except FileNotFoundError:
                sys.exit("File does not exist")
    except ValueError:
        sys.exit("Not a CSV file")

