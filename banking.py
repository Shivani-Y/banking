"""
Using the object-oriented programming paradigm to model a bank account
"""
import datetime as dt

class Transaction():
    """Storing and Formating a transaction instance"""

    def __init__(self, amount, timestamp=None):
        self.amount = amount
        self.timestamp = timestamp
        if self.timestamp is None:
            self.timestamp = dt.datetime.now().strftime("%Y-%m-%d %I:%M %p")

    def __repr__(self):
        'Transaction(amount={}, timestamp={})'.format(
            repr(self.amount),
            repr(self.timestamp)
        )

    def __str__(self):
        return f"""Transaction Time: {self.timestamp},
Amount: ${self.amount:.2f}"""

class Account(Transaction):
    "Performs account trnsactions"

    def __init__(self, amount=0, timestamp=None):
        super().__init__(amount, timestamp=None)
        self.my_transactions = []
        self.my_timestamp = []
        self.calculated_balance = sum(self.my_transactions)
        self.transaction_dictionary = {}

    def deposit(self, amount):
        """accepts amount for deposit"""
        #self.balance += amount
        if not isinstance(amount, (int, float)):
            raise ValueError("Transactions can only be numerical")
        self.my_transactions.append(+amount)
        self.my_timestamp.append(self.timestamp)
        self.calculated_balance = sum(self.my_transactions)
        self.transaction_dictionary = dict(zip(self.my_transactions, self.my_timestamp))
        return self.calculated_balance

    def withdraw(self, amount):
        """withdraws amount"""
        if not isinstance(amount, (int, float)):
            raise ValueError("Transactions can only be numerical")
        if self.calculated_balance - amount >= 0:
            self.calculated_balance -= amount
            self.my_transactions.append(-amount)
            self.my_timestamp.append(self.timestamp)
            self.calculated_balance = sum(self.my_transactions)
            self.transaction_dictionary = dict(zip(self.my_transactions, self.my_timestamp))
        else:
            raise ValueError(f"""Your current balance is {self.calculated_balance}
             and you tried to withdraw {amount}. Your withdrawal limit is
             {self.calculated_balance}""")
        return self.calculated_balance

    def get_balance(self):
        """gives account balance"""
        return self.calculated_balance

    def __str__(self):
        return f"""Account Balance is: ${self.calculated_balance:.2f}"""
