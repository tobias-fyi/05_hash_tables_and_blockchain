"""
Hash tables :: Day 2 notes - Hash tables

* Hash tables have an underlying Array structure
    * This is why they are as hast at accessing elements as arrays
    * The main difference is that hash tables are indexed using a hash function
    in an unordered fashion, whereas arrays are indexed via contiguous ordered indices
* HashTable code is fairly similar to DynamicArray code
"""

# %%
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"<'{self.key}': '{self.value}'>"

    def __repr__(self):
        return f"<'{self.key}': '{self.value}'>"


# %%
class HashTable:
    """A hash table with `capacity` number of buckets.
    Also accepts string keys.
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

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
        # Run key through hash function to get integer
        # Take the mod of hashed key to get bucket index
        index = self._hash_mod(key)
        # Get value at bucket index
        pair = self.storage[index]
        if pair is not None:
            # If so, overwrite and print warning
            if pair.key != key:
                print("Warning: value was overwritten.")
                pair.key = key
            pair.value = value
        else:  # If not, add new LinkedPair to bucket
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        """Remove the value stored with the given key.
        Print a warning if the key is not found.
        """
        # Hash the key, taking the modulo to get the bucket index
        index = self._hash_mod(key)
        # Look up that index in storage array
        val = self.storage[index]
        # If a pair exists at the index / in bucket with matching key
        if val is not None and val.key == key:
            self.storage[index] = None  # If so, remove / set index to None
        else:  # If value at index is None, print warning
            print(f"Warning: Key does not exist.")

    def retrieve(self, key):
        """Retrieve the value stored with the given key.
        Returns None if the key is not found.
        """
        # Take modulo of hash of key to get bucket index
        index = self._hash_mod(key)
        val = self.storage[index]
        # Check if pair exists in bucket with matching keys
        if val is not None and val.key == key:
            return val.value  # If so, return the value
        else:  # If not, return None
            return None

    def resize(self):
        """Doubles the capacity of the hash table and
        rehash all key/value pairs.
        """
        # Double the capacity
        self.capacity *= 2
        # Allocate new storage array with new capacity
        new_storage = [None] * self.capacity
        # Copy elements from previous storage to new
        for i in range(len(self.storage)):
            new_storage[i] = self.storage[i]
        # Assign new array as current storage
        self.storage = new_storage


# %%
ht = HashTable(8)

ht.insert("key-0", "val-0")
ht.insert("key-1", "val-1")
ht.insert("key-2", "val-2")
ht.insert("key-3", "val-3")
ht.insert("key-4", "val-4")
ht.insert("key-5", "val-5")
ht.insert("key-6", "val-6")
ht.insert("key-7", "val-7")
ht.insert("key-8", "val-8")
ht.insert("key-9", "val-9")

# %%
return_value = ht.retrieve("key-0")

return_value = ht.retrieve("key-1")
return_value = ht.retrieve("key-2")
return_value = ht.retrieve("key-3")
return_value = ht.retrieve("key-4")
return_value = ht.retrieve("key-5")
return_value = ht.retrieve("key-6")
return_value = ht.retrieve("key-7")
return_value = ht.retrieve("key-8")
return_value = ht.retrieve("key-9")


# %%
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

# %%
# Test if data intact after resizing
print(ht.retrieve("line_1"))
print(ht.retrieve("line_2"))
print(ht.retrieve("line_3"))

print("")


# %%
# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")
