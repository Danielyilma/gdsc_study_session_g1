import unittest
from bank_account import BankAccount


class testBankAccount(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.bank1 = BankAccount("abel", 12311)
    
    def test_deposit(self):
        self.bank1.deposit(1000)
        self.assertEqual(self.bank1.balance, 1000)
    
    def test_withdraw(self):
        self.bank1.withdrawal(500)
        self.assertEqual(self.bank1.balance, 500)
    

if __name__ == "__main__":
    unittest.main()