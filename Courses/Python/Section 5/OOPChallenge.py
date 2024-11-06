class Account():

    def __init__(self,owner, balance=0):
        self.owner = owner
        self.balance = balance

    def Deposit(self,amount):
        self.balance = self.balance + amount
        pass

    def __str__(self):
            return f"Welcome {self.owner}, your balance is {self.balance}"


    def WithDraw(self, withdraw):
         if withdraw > self.balance:
              print(f"Insuficient funds")
         else:
              self.balance = self.balance - withdraw
              print(f"You succesfully withdrewed {withdraw} euros")



B = Account(owner= "Alex", balance= 300)

print(B)

B.Deposit(300)
print(B)

B.WithDraw(345)
print(B)