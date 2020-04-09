"""
Blockchain — Day 2 Project :: Wallet app

> MVP
* Allow the user to enter, save, or change the `user_id` used for the program
* Display the current balance for that user
* Display a list of all transactions for this user, including sender and recipient

> Stretch Goals
* Use styling to visually distinguish coins sent and coins received
* Paginate the list of transactions if there are more than ten
"""

# %%
import json
import sys

# from flask import Flask, jsonify, request
import requests


# %%
class User:
    def __init__(self, user_id: str = "007", url: str = "http://localhost:5000"):
        """Constructor for the user account management handler class."""
        self.user_id = user_id
        self.url = url

    @property
    def user_id(self) -> str:
        """User's account identifier."""
        return self._user_id

    @user_id.setter
    def user_id(self, new_id) -> None:
        """Setter function for user_id property."""
        self._user_id = new_id
        print(f"User ID: {new_id}")

    def post_transaction(self, recipient: str, amt: float) -> int:
        """Posts a new transaction from the user.
        Returns index of block into which transaction was posted."""
        # Construct the POST object
        post_data = {
            "sender": self.user_id,
            "recipient": recipient,
            "amount": amt,
        }
        # Post transaction to blockchain server
        r = requests.post(url=self.url + "/transactions/new", json=post_data)
        # Parse the response
        if r.status_code == 200:
            resp = r.json()
            print(resp.get("message"))
            return resp.get("index")
        else:
            print("Post failed.")

    # TODO: method that displays user's current balance
    # TODO: method that displays user's transactions


# %%
james_bond = User()
james_bond.user_id = "007"

# %%
jane_bond = User()
jane_bond.user_id = "008"


# %%
# Post a new transaction
james_bond.post_transaction("008", 1.8)
jane_bond.post_transaction("007", 0.7)

# %%
jane_bond.post_transaction("007", 1.7)
james_bond.post_transaction("008", 0.8)

# %%
if __name__ == "__main__":
    user = User()
