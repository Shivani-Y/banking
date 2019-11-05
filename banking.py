"""
Using the object-oriented programming paradigm to model a bank account
"""
import datetime as dt

class Transaction():
    """Storing and Formating a transaction instance"""

    def __init__(self, amount, timestamp=None):
        self.amount = amount
        self.timestamp = timestamp
