"""
Blockchain :: Sprint challenge
"""

import hashlib
import random
from timeit import default_timer as timer
from uuid import uuid4
import sys

import requests


def proof_of_work(last_proof):
    """Multi-Ouroboros Proof of Work Algorithm.
    - Find a number p' such that the last five digits of hash(p) are equal
    to the first five digits of hash(p')
    - IE:  last_hash: ...AE912345, new hash 12345888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()

    print("Searching for next proof")
    proof = 1
    # Find last_hash by hashing last proof
    last_bytes = str(last_proof).encode()
    last_hash = hashlib.sha256(last_bytes).hexdigest()

    while not valid_proof(last_hash, proof):
        # TODO: Find better method of iterating through proofs
        proof += 1

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    """Validates the Proof.
    Multi-ouroborus:  Do the last five characters of the hash of the last
    proof match the first five characters of the hash of the new proof?

    IE:  last_hash: ...AE912345, new hash 12345E88...
    """
    guess = str(proof).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    if guess_hash[:5] == last_hash[-5:]:
        print("last:", last_hash, last_hash[:5])
        print("guess:", guess_hash, guess_hash[-5:])
    return guess_hash[:5] == last_hash[-5:]


if __name__ == "__main__":
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    with open("my_id.txt", "r") as f:
        id = f.read().strip()
        print(f"Good morning, {id}")

    if id == "NONAME":
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        print("\nRequesting last proof from server...")
        r = requests.get(url=node + "/last_proof")
        # Parse the response to get last proof
        data = r.json()
        last_proof = data.get("proof")

        # The Emperor's New Proof!
        print(f"Starting proof of work using last_proof: {last_proof}")
        new_proof = proof_of_work(last_proof)

        print(f"\nNew proof {new_proof} found!")
        print("Sending to server...")
        post_data = {"proof": new_proof, "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get("message") == "New Block Forged":
            print(f"{data.get('message')}!")
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(f"Error: {data.get('message')}")
