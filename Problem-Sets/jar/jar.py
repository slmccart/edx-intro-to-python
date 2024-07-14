class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Deposit exceeds jar capacity")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Withdrawal exceeds jar size")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

def main():
    capacity = int(input("Capacity: "))
    jar = Jar(capacity)
    print(jar)

if __name__ == "__main__":
    main()
