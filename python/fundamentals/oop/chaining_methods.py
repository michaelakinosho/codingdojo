class User:
    #class attribute defined at the class level
    bank_name = 'First National Dojo'
    currType = '$'
    
    def __init__(self,name,email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0
    
    #including a deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    #including a withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(("User: {}, Balance: {}{:,.2f}").format(self.name,self.currType,self.account_balance))
        return self
    
    def transfer_money(self,other_user,amount):
        print("Respective balances before transfer:")
        self.display_user_balance(), other_user.display_user_balance()
        print('\n')
        self.account_balance, other_user.account_balance = self.account_balance - amount, other_user.account_balance + amount
        print("Respective balances after transfer:")
        self.display_user_balance(), other_user.display_user_balance()
        return self

#Creating three instances of user        
mj = User("Michael Jordan","mj@mj.com")
kb = User("Kobe Bryant","kb@kb.com")
magic = User("Earvin Johnson","magic@magic.com")

#Performing user1's transactions
mj.make_deposit(15000.23).make_deposit(25000.45).make_deposit(30000.23).make_withdrawal(100.45).display_user_balance()

#Performing user2's transactions
kb.make_deposit(1000000).make_deposit(300.24).make_withdrawal(600.12).make_withdrawal(600.99).display_user_balance()

#Performing user3's transactions
magic.make_deposit(35.35).make_withdrawal(50.00).make_withdrawal(50.00).make_withdrawal(50.00).display_user_balance()
print("\n")

transfered_amt = 50000
transferor = kb
transferee = magic
print(("{} is transferring {}{:,.2f} to {}").format(transferor.name,transferor.currType,transfered_amt,transferee.name))
transferor.transfer_money(transferee,transfered_amt)


