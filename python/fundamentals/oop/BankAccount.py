"""
Author: Michael Akinosho
Date: October 29, 2021
Test units are available below and are commmented out
class User is imported by Users_with_BankAccounts
"""
class BankAccount:
    int_rate = 0.0
    balance = 0.0
    currType = '$'
    bank_name = 'First National Dojo'
    overdraw_fee = 5.00
    all_accounts = []
    
    #class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    
    #class method to get balance of all accounts
    @classmethod
    def all_bankaccounts(cls):
        sum = 0
        #Using cls to refer to the class
        for account in cls.all_accounts:
            account.display_account_info()
    
    #static method to determine if has sufficient funds
    @staticmethod
    def pos_balance(balance,amount=0):
        if (balance - amount) < 0:
            return False
        else:
            return True
        
    def __init__(self,acct_type,int_rate,balance):
        self.acct_type = acct_type
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        
    def deposit(self,amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if self.pos_balance(self.balance,amount):
            self.balance -= amount
        else:
            self.display_account_info()
            print(("Insufficient funds, account has incurred a fee of ${:,.2f}, due to withdrawal of ${:,.2f}.").format(self.overdraw_fee,amount))
            self.balance -= (amount + self.overdraw_fee)
            self.display_account_info()
            print('\n')
        return self
        
    def display_account_info(self):
        print(("{} Account Balance: {}{:,.2f}").format(self.acct_type,self.currType,self.balance))
        return self
        
    def yield_interest(self):
        if self.pos_balance(self.balance):
            print(("Current yield on {} Account is: {}{:,.2f}.").format(self.acct_type,self.currType,self.balance*self.int_rate))
            self.balance = self.balance + round((self.balance * self.int_rate),2)
        else:
            print("Unfortunately no yield was earned, as account balance was below minimum.")
        return self

"""
CheckingAcct = BankAccount('Checking',0.10,75000)
SavingsAcct = BankAccount('Savings',0.01,2000)

CheckingAcct.deposit(150000).deposit(250000).deposit(0.23).display_account_info().yield_interest().display_account_info()
print('\n')
SavingsAcct.deposit(300).deposit(500).withdraw(10000).withdraw(900.50).display_account_info().yield_interest().display_account_info()
print('\n')
BankAccount.all_bankaccounts()
"""