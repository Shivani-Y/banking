"""
Test module for banking.py
"""
from banking import Transaction
#import pytest

class TestTransaction():
    """Testing trnasaction bound to self"""
    def test_transaction(self):
        test_my_transaction = Transaction(20)
        assert test_my_transaction.amount == 20
