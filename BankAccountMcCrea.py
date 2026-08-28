class account:
    def __init__(self, ownerName, balance):
        self.ownerName = ownerName
        self.balance = balance
        self.amount = 0
        
    def deposit(self, amount):
        if amount <= 0:
            print('Not valid input')
        else:
            self.balance += amount
                
    def withdraw(self, amount):
        if self.balance <=0:
            print('Insufficient funds')
        else:
            self.balance -= amount
                
    def getBalance(self):
        return self.balance
        
def main():
    a = account('Frank', 1000)
    account.deposit(a, 100)
    print(a.getBalance())
    account.withdraw(a, 1100)
    print(a.getBalance())
    account.withdraw(a, 500)
    print(a.getBalance())
    
    
main()