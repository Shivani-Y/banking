"""
Test module for banking.py
"""
from banking import Transaction
import datetime as dt
#import pytest

class TestTransaction():
    """Testing trnasaction bound to self"""
    def test_transaction(self):
        """Testing for amount"""
        test_my_transaction = Transaction(20)
        assert test_my_transaction.amount == 20

    def test_none_transaction(self):
        """testing for date none """
        test_my_transaction = Transaction(20, None)
        assert test_my_transaction.timestamp != None

    def test_date_transaction(self):
        """testing for date now"""
        test_my_transaction = Transaction(20)
        assert test_my_transaction.timestamp == dt.datetime.now().strftime("%Y-%m-%d %I:%M %p")
