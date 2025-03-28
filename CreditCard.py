class CreditCard:
    """consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.
        
           The initial balance is zero.

           customer the name of the customer (e.g. 'John Bowman')
           bank     the name of the bank (e.g. 'California Savings')
           acnt     the acount identifier (e.g. '5391 0375 9387 5309')
           limit    credit limit (measured in dollars) 
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name"""
        return self._bank
    
    def get_account(self):
        """Return the card identifying number (typically stored as a string)"""
        return self._account
    
    def get_limit(self):
        """Return the current credit limit"""
        return self._limit
    
    def get_balance(self):
        """Return current balance"""
        return self._balance