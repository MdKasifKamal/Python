class Account:
    def __init__(self, acc, bal):
        self.acc = acc
        self.bal = bal
  #debit method
    def debit(self, amt):
        self.bal -= amt
        print("Rs",amt,"debited from your account")
        print("Your current balance is:",self.get_balance())
  #credit method
    def credit(self, amt):
        self.bal += amt
        print("Rs",amt,"credited to your account")
        print("Your current balance is:",self.get_balance())
    def get_balance(self):
        return self.bal

acc1 = Account(1234, 10000)
print("Account number:", acc1.acc)
print("Account balance:", acc1.bal)
acc1.debit(2000)
acc1.credit(5000)
