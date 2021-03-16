
# Besides the basic functions in 2.3 Example CreditCar,
# we add two functions:
## 1. if an attempted charge is rejected because it would have exceeded the credit limit,
### a $5 fee will be charged. 
## 2. there will be a mechanism for assessing a monthly interest charge
## on the outstanding balance, based upon an APR specified as a constructor parameter. 



class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees"""

    def __init__(self,customer,bank,acnt,limit,apr):

        super().__init__(customer,bank,acnt,limit)
        self._apr = apr 
    
    def charge(self,price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success
    
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1+self._apr,1/12)
            self._balance *= monthly_factor
    
