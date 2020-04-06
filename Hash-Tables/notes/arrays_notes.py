"""
Hash tables :: Day 1 Notes: Arrays

An array:
* Stores a sequence of elements
* Each element must be the same data type
* Occupies a contiguous block of memory
* Can access data in constant time with this equation:

`memory_address = starting_address + index * data_size`

"""


class DynamicArray:
    def __init__(self, capacity=1):
        self.count = 0  # Number of elements in the array
        self.capacity = capacity  # Total amount of storage in array
        self.storage = [None] * capacity

    def insert(self, index, value):
        """Inserts a value into list at index.
        Complexity: O(n)"""
        # Check if we have enough capacity
        if self.count >= self.capacity:
            # If not, make more room
            self.resize()
        # Shift every item after index to right by 1
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]
        # Add new value at the index
        self.storage[index] = value
        # Increment count
        self.count += 1

    def append(self, value):
        """Appends a value to the end of array.
        Complexity: O(1)"""
        # Check if array has enough capacity
        if self.count >= self.capacity:
            # If not, resize up
            self.resize()
        # Add value to the index of count
        self.storage[self.count] = value
        # Increment count
        self.count += 1

    def resize(self):
        """Doubles the capacity of array."""
        self.capacity *= 2
        # Allocate a new storage array with double capacity
        new_storage = [None] * self.capacity
        # Copy all ements from old storage to new
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage


a = DynamicArray(2)
a.insert(0, 19)
a.insert(0, 14)
print(a.storage)

a.append(9)
a.append(8)
print(a.storage)
a.append(7)
print(a.storage)
