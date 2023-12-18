


class BankAccount:

    def __init__(self, userName, userId):
        self.userName = userName
        self.userId = userId
        self.__balance = 0
    
    def deposit(self, depositAmount):
        self.__balance += depositAmount
    
    def withdrawal(self, withdrawAmount):
        if self.__balance > withdrawAmount:
            self.__balance -= withdrawAmount

    @property
    def balance(self):
        return self.__balance
    
    def displayBal(self):
        print("your current balance is {}".format(self.__balance))
    