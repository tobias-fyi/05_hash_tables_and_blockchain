"""
Hashtables :: Sprint challenge, Part 2
"""

from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_retrieve,
)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    # === Insert tickets into hashtable === #
    for ticket in tickets:
        # Source is the key, destination is the value
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # === Iterate form source -> dest === #
    # Start with source = "NONE", end with destination = "NONE"
    dest = hash_table_retrieve(hashtable, "NONE")
    counter = 0  # Use counter to index route array
    # Iterate by using each proceeding value as the next key
    while dest != "NONE":
        # Add current city to route
        route[counter] = dest
        # Move to next
        dest = hash_table_retrieve(hashtable, dest)
        # Increment route counter
        counter += 1

    return route


# === Short test === #
ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

expected = ["PDX", "DCA"]
result = reconstruct_trip(tickets, 3)
