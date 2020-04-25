"""
BankAccount Class where we can store information for each
bank account. Stores customer's first name, last name, and bank balance. Default
values for names is 'none' and for balance is 0. Methods should include deposit(amount)
withdraw(amount) and getBalance() and should read input from a file.
use input file format

---inputfile.txt---
New Some body1 0 
D 1500 
W 1000
D 2000
2000
D 9000
W 3500
New Some body2 0
D 9000
W 5000
D 11000
W 5000
"""

#!/usr/bin/env python3
import re

class BankAccount:
    def __init__(self, first_name = 'none', last_name = 'none', balance = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdrawal(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
            return self.balance
        else:
            return 'Withdraw amount ${} exceeds the amount you have in your account'.format(amount)

    def getBalance(self):
        return self.balance

#driver code
new_file = open('/path/to/outputfile.txt', 'a')
with open('/path/to/inputfile.txt', 'r') as file:
    while True:
        lines = file.readline()
        if len(lines) == 0:
            break
        if lines[0] == 'N':
            num = re.findall(r"[0-9]+", lines)
            amount = int(num[0])
            strings = re.findall(r"[A-Z][a-z]+\s", lines)
            first_name = strings[1]
            last_name = strings[2]
            s = BankAccount(first_name, last_name, amount)
            num_string = str("has ${:0.1f}".format(amount))
            output = first_name + " " + last_name + " " + num_string + "\n"
            new_file.write(output)
        elif lines[0] == 'D':
            num = re.findall(r"[0-9]+", lines)
            amount = int(num[0])
            deposit = s.deposit(amount)
            num_string = str("has ${:0.1f}".format(deposit))
            output = first_name + " " + last_name + " " + num_string + "\n"
            new_file.write(output)
        elif lines[0] == 'W':
            num = re.findall(r"[0-9]+", lines)
            amount = int(num[0])
            withdrawal = s.withdrawal(amount)
            num_string = str("has ${:0.1f}".format(withdrawal))
            output = first_name + " " + last_name + " " + num_string + "\n"
            new_file.write(output)
new_file.close()

