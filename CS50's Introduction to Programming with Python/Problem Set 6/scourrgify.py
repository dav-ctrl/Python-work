import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    name, extension = sys.argv[1].split(".")
    if extension != "csv":
        sys.exit("Not a CSV file")
    else:
            students = []
            try:
                with open(sys.argv[1]) as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        try:
                            last, first = row["name"].split(",")
                            first = first.lstrip()
                            students.append({"first": first, "last": last, "house": row["house"]})
                        except ValueError:
                            pass
                with open(sys.argv[2], "w") as file:
                    writer = csv.DictWriter(file, fieldnames=["first","last","house"])
                    writer.writeheader()
                    for student in students:
                        writer.writerow({"first": student['first'], "last": student['last'], "house": student['house']})
            except FileNotFoundError:
                print(f"Could not read {sys.argv[1]}")

