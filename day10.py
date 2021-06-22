class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Welcome to the Deposit & Withdrawal Machine")
    def display(self):
        print("\n Available Balance=",self.balance)
class Deposit(Bank_Account): 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
class Withdraw(Bank_Account):   
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
s = Bank_Account()
p=Deposit()
p.deposit()
q=Withdraw()
q.withdraw()
s.display()