"""
Hashtables :: Sprint challenge, Part 1
"""

from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_retrieve,
)


def get_indices_of_item_weights(weights, length, limit):
    """Given a package with a weight limit `limit` and a list `weights`
    of item weights, finds two items whose sum of weights equals the 
    weight limit `limit`.
    """
    ht = HashTable(16)

    # === Insert weights into hash table === #
    for index, weight in enumerate(weights):
        # Create pairs where weight is key, index is value
        hash_table_insert(ht, weight, index)

    # === Look for sum of limit === #
    for index, weight in enumerate(weights):
        # Calculate the other weight needed to sum to limit
        target = limit - weight
        # Attempt to retrieve the value at that key from hashtable
        match = hash_table_retrieve(ht, target)

        # If match, retrieve indices
        if match:
            # source = hash_table_retrieve(ht, weight)
            # return (source, match) if source > match else (match, source)
            return (match, index)

    # If no match, return None
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


# # === Example inputs === #
# weights = [4, 6, 10, 15, 16]
# length = 5
# limit = 21

# # Test out function with provided example inputs
# answer = get_indices_of_item_weights(weights, length, limit)
# print(answer)
# # Since these are the indices of weights 15 and 6 whose sum equals 21
# output = [3, 1]

# # === Tests failed with first pass === #
# weights_2 = [4, 4]
# answer_2 = get_indices_of_item_weights(weights_2, 2, 8)

# assert answer_2[0] == 1
# assert answer_2[1] == 0

# print(answer_2)

# weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# answer_4 = get_indices_of_item_weights(weights_4, 9, 7)

# assert answer_4[0] == 6
# assert answer_4[1] == 2

# print(answer_4)
