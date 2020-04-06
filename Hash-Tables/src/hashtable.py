"""
Hash tables :: Assignment

Linked List hash table key/value pair.
"""


class IndexExistsError(Exception):
    """Exception raised for case when hash key exists in table."""

    def __init__(self, index):
        self.index = index

    def __str__(self):
        return f"'{self.index}' already contains a value."


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"<{self.key}: {self.value}>"


class HashTable:
    """A hash table with `capacity` number of buckets.
    Also accepts string keys.
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        """Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return hash(key)

    def _hash_djb2(self, key):
        """Hash an arbitrary key using DJB2 hash.
        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """Store the value with the given key.

        Part 1: Hash collisions should be handled with an error warning. 
        (Think about and investigate the impact this will have on the tests)

        Part 2: Change this so that hash collisions are handled with
        Linked List Chaining.
        """
        # Check if HT has enough capacity
        if self.count >= len(self.storage):
            self.resize()  # If not, create more room
        # Run key through hash function to get integer
        # Take the mod of hashed key to get bucket index
        index = self._hash_mod(key)
        # Instantiate new LinkedPair instance
        pair = LinkedPair(key, value)
        # If value at index is None, replace
        if self.storage[index] is None:
            self.storage[index] = pair
            self.count += 1  # Increment count if one was added
        else:  # If there is already a value at index, throw a warning
            # raise IndexExistsError(index)
            existing = self.storage[index]
            print(f"Warning: index [{index}] ({key}) contains '{existing}'.")
            print(f"  That value will be overwritten by '{pair}'.")
            # Overwrite the previous pair
            self.storage[index] = pair
            # Do not increment count if a pair was replaced

    def remove(self, key):
        """Remove the value stored with the given key.
        Print a warning if the key is not found.
        """
        # Hash the key, taking the modulo to get the bucket index
        index = self._hash_mod(key)
        # Look up that index in storage array
        # If value at index is None, print warning
        if self.storage[index] is None:
            print(f"Key does not exist in hash table.")
        # If a pair exists at the index, return the value
        else:
            value = self.storage[index].value

    def retrieve(self, key):
        """Retrieve the value stored with the given key.
        Returns None if the key is not found.
        """
        # Take modulo of hash of key to get bucket index
        index = self._hash_mod(key)
        # Look up and return the value at that index
        if self.storage[index] is None:
            # If no object exists, return None
            return None
        else:
            # If object exists, return the value
            return self.storage[index].value

    def resize(self):
        """Doubles the capacity of the hash table and
        rehash all key/value pairs.
        """
        # Double the capacity
        self.capacity *= 2
        # Allocate new storage array with new capacity
        new_storage = [None] * self.capacity
        # Copy elements from previous storage to new
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        # Assign new array as current storage
        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
