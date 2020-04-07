"""
Hash tables :: Assignment

Linked List hash table key/value pair.
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
        self.count = 0  # TODO: load factor

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
        # Instantiate new LinkedPair instance
        new_pair = LinkedPair(key, value)
        # If value at index is None, replace
        if self.storage[index] is None:
            self.storage[index] = new_pair
        else:  # If there is already a value at index
            node = self.storage[index]
            while node:  # Loop through LinkedList
                # Compare each node's key
                if node.key == key:  # If key exists, overwrite value
                    node.value = value
                elif node.next is None:  # If node is tail
                    # Add new pair to next of current tail / as new tail
                    node.next = new_pair
                # Continue iteration into next node
                tail = tail.next

    def remove(self, key):
        """Remove the value stored with the given key.
        Print a warning if the key is not found.
        """
        # Hash the key, taking the modulo to get the bucket index
        index = self._hash_mod(key)
        # Look up that index in storage array
        if self.storage[index] is None:  # If index is empty, print warning
            print(f"Warning: key '{key}' does not exist.")
            return  # Stop function execution
        else:  # If a pair exists at index, check bucket for matching key
            # Start with first node as current node
            node = self.storage[index]
            # If key is found, node will be removed by setting
            # prev.next to node.next and setting node.next to None
            prev = None
            while node:  # Iterate through bucket's LinkedList
                if node.key == key:  # Look at current node's key for match
                    # If matched, remove references to node
                    if prev is not None:  # If not head of LinkedList
                        prev.next = node.next  # Remove by "skipping" current node
                    else:  # If match is head, set node.next to head
                        self.storage[index] = node.next
                    node.next = None  # Remove final reference to LinkedList
                    return  # Stop function execution
                # If not, move to next node
                prev = node
                node = node.next
            # Finally, if execution gets this far, no key was found, print warning
            print(f"Warning: key '{key}' does not exist.")

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
        else:  # If object exists, compare keys
            if key == self.storage[index].key:
                return self.storage[index].value
            else:
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
            # TODO: rehash the keys
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
