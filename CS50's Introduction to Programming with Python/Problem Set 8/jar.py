class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        if self.size == 1:
            return f"1 cookie"
        else:
            return f"{self.size} cookies"

    def deposit(self, n):
         if self.size + n <= self.capacity:
            self._size = self.size + n
         else:
            raise ValueError("Number of cookies exceeds capacity")

    def withdraw(self, n):
        if self.size - n >= 0:
            self._size = self.size - n
        else:
            raise ValueError("Not so many cookies available")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        if type(capacity) != int or capacity <= 0:
                raise ValueError("Not a valid capacity")
        self._capacity = capacity

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Not so much capacity")
        self._size = size

def main():
    jar=Jar()
    print(jar.capacity)
    print(jar.size)
    jar.deposit(1)
    print(jar.size)

if __name__ == "__main__":
    main()
