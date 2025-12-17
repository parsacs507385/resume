class Jar:
    def __init__(self, capacity=12):
        size = 0
        if capacity < 0:
            raise ValueError("Capacity Must Not Be Negative")
        else:
            self.capacity = capacity
            self.size = size

    def __str__(self):
        return (self.size*"🍪")

    def deposit(self, n):
        if n <= self.capacity:
            self.size += n
            self.capacity -= n
            return self.size, self.capacity
        else:
            raise ValueError("Overflow!")

    def withdraw(self, n):
        if n <= self.size:
            self.capacity += n
            self.size -= n
            return self.size, self.capacity
        else:
            raise ValueError("Too Poor!")

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        if 0 <= capacity:
            self.__capacity = capacity
        else:
            raise ValueError("Capacity Must Not Be Negative")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

