'''

This is a Banking class that does the following:
  Tracks an initial account balance
  Tracks deposits in the account
  Tracks withdrawals to the account
  Prints out a current balance
  Prints an error message if someone tries to withdraw more money than what is currently in the account

'''

#!usr/bin/env python3

#Creating a Banking class
class Banking:

    def __init__(self, name, initial_bal):
        self.name = name
        self.balance = initial_bal

    #current bank balance
    def current_bal(self):
        print("{}'s current bank balance is ${}".format(self.name, self.balance))

    #bank balance after deposit
    def deposit(self, additional_money):
        self.balance += additional_money
        print("{}'s bank balance after the deposit is ${}".format(self.name, self.balance))

    # bank balance after withdraw
    def withdraw(self, withdraw_amount):
        if self.balance < withdraw_amount:
            print("Sorry, {}, you do not have enough money to withdraw ${}".format(self.name, withdraw_amount))
        else:
            self.balance -= withdraw_amount
            print("{}'s bank balance after the withdrawal is ${}".format(self.name, self.balance))


