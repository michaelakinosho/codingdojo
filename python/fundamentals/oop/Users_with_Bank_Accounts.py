"""
Author: Michael Akinosho
Date: October 29, 2021
"""
#Ensure User.py and BankAccount.py are saved to the same folder as the current file
from User import User
from BankAccount import BankAccount

class Users_with_Bank_Accounts:
    #instantiates based on instances of its two super classes: User and BankAccount
    def __init__(self,user,bankaccount):
        self.user = user
        self.bankaccount = bankaccount
    
    #calls the Bank Account method
    def deposit(self, amount):
        self.bankaccount.deposit(amount)
        return self
    
    #calls the Bank Account method
    def withdraw(self, amount):
        if self.bankaccount.balance - amount < 0:
            print(self.user.name)
        self.bankaccount.withdraw(amount)
        return self
    
    #method is modified from Bank Account version
    #it accommodates the name on the account and account type 
    def display_account_info(self):
        print(("{} your {} account balance is: {}{:,.2f}.").format(self.user.name,self.bankaccount.acct_type,self.bankaccount.currType,self.bankaccount.balance))
        return self
    
    #also calls the bank account method
    def yield_interest(self):
        self.bankaccount.yield_interest()
        return self
    
    #new implementation of transfer money method
    #since account balance resides with bank account and not user
    #need to utilize attributes from bank account instance
    def transfer_money(self,other_user,amount):
        if self.bankaccount.pos_balance(self.bankaccount.balance,amount):
            print('{} unable to complete transfer, amount is higher than available.'.format(self.user.name))
            return self
        
        print("Respective balances before transfer:")
        self.display_account_info(), other_user.display_account_info()
        print('Amount transferred is {:,.2f}.\n'.format(amount))
        self.bankaccount.balance, other_user.bankaccount.balance = self.bankaccount.balance - amount, other_user.bankaccount.balance + amount
        print('Respective balance after transfer:')
        self.display_account_info(), other_user.display_account_info()
        return self

if __name__ == "__main__":
    #case one the superclasses are instantiated then passed to Users with Bank Accounts
    username = User('Michael Jordan','mj@mj.com')
    accounttype = BankAccount('Checking',0.10,75000)
    User1 = Users_with_Bank_Accounts(username,accounttype)
    User1.deposit(5000).withdraw(100000).display_account_info().yield_interest().display_account_info()

    #case the two superclasses are passed as parameters
    User2 = Users_with_Bank_Accounts(User('Kobe Bryant','kb@kb.com'),BankAccount('Savings',0.50,1750000))
    User2.deposit(5000).withdraw(100000).display_account_info().yield_interest().display_account_info()
    print('\n')
    User2.transfer_money(User1,2000000)