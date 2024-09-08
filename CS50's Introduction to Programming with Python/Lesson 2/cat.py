# Part 1

i = 3
while i != 0:
    print("meow")
    i = i-1

i = 1
while i <= 3:
    print("meow")
    i = i+1

i = 0
while i < 3:
    print("meow")
    i += 1

for i in range(3):
    print("meow")

print("meow\n" * 3, end="")

# Part 2

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
