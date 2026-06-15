class BankAccount:
    def __init__(self,bal=0):
        if bal <0:
            raise ValueError("Wrong Balance!")
        self._bal = bal

    @property
    def bal(self):
        return self._bal
    
    def deposit(self,amt):
        if amt<=0:
            raise ValueError("Deposit amt must be positive")
        self._bal += amt

    def withdraw(self,amt):
        if amt<=0:
            raise ValueError("Withdraw amt must be positive")
        if self.bal < amt:
            raise ValueError("Insufficient Funds")
        self._bal -= amt
    