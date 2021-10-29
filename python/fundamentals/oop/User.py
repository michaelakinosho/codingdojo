"""
Author: Michael Akinosho
Date: October 29, 2021
Test units are available below and are commmented out
class User is imported by Users_with_BankAccounts
"""
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
    
    #including a withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(("User: {}, Balance: {}{:,.2f}").format(self.name,self.currType,self.account_balance))
    
    def transfer_money(self,other_user,amount):
        print("Respective balances before transfer:")
        self.display_user_balance(), other_user.display_user_balance()
        print('\n')
        self.account_balance, other_user.account_balance = self.account_balance - amount, other_user.account_balance + amount
        print("Respective balances after transfer:")
        self.display_user_balance(), other_user.display_user_balance()

#Please remove block comments to run as standalone file
#Thanks!!
"""
#Creating three instances of user        
mj = User("Michael Jordan","mj@mj.com")
kb = User("Kobe Bryant","kb@kb.com")
magic = User("Earvin Johnson","magic@magic.com")

#Performing user1's transactions
mj.make_deposit(15000.23)
mj.make_deposit(25000.45)
mj.make_deposit(30000.23)
mj.make_withdrawal(100.45)
mj.display_user_balance()

#Performing user2's transactions
kb.make_deposit(1000000)
kb.make_deposit(300.24)
kb.make_withdrawal(600.12)
kb.make_withdrawal(600.99)
kb.display_user_balance()

#Performing user3's transactions
magic.make_deposit(35.35)
magic.make_withdrawal(50.00)
magic.make_withdrawal(50.00)
magic.make_withdrawal(50.00)
magic.display_user_balance()
print("\n")

transfered_amt = 50000
transferor = kb
transferee = magic
print(("{} is transferring {}{:,.2f} to {}").format(transferor.name,transferor.currType,transfered_amt,transferee.name))
transferor.transfer_money(transferee,transfered_amt)
"""
