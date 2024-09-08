def main():
    student = get_student()
    print(f"{student[0]} is from {student[1]}")

# Tuples are immutable
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()
