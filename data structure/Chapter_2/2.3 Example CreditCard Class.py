






class CreditCard:
    """A consumer credit card."""

    def __init__(self,customer,bank,acnt,limit):
        """
        The initial balance is zero 

        customer    the name of customer 
        bank        the name of bank 
        acnt        the acount identifier (e.g., `5391 0375 9387 5309`)
        limit       credit limit (in dollars)


        """
        # _secret with a single leading underscore are intended to suggest that they are only for "internal"
        # use to a class or module, and not part of a public interface. 
        self._customer = customer
        self._bank = bank 
        self._acnt = acnt 
        self._limit = limit 
        self._balance = 0 
    
    def get_customer(self):
        """Return name of the customer"""
        return self._customer
    
    def get_bank(self):
        """Return the bank's name"""
        return self._bank 

    def get_account(self):
        """Return the card identifying number """
        return self._acnt 

    def get_limit(self):
        """Return the card limit in dollars """
        return self._limit 

    def get_balance(self):
        """Return the card balance  """
        return self._balance
    
    def charge(self,price):
        """
        Charge given price to the card, assuming sufficient credit limit 
        Return True if charge was processed. False if charge was denied.

        """

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self,amount):
        """Process customer payment that reduces balance"""
        return self._balance -= amount


