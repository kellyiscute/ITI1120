class BankAccount(object):
    def __init__(self, name='Dupont', balance=1000):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'The solde of the Bank account of {self.name} is {self.balance} dollars.'

    def __eq__(self, other: 'BankAccount'):
        return self.name == other.name and self.balance == other.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display(self):
        print(f'The solde of the Bank account of {self.name} is {self.balance} dollars.')


class AccountSaving(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest_rate = 0.3

    def change_rate(self, value):
        self.interest_rate = value

    def capitalisation(self, numberMonth):
        print(f'Capitalisation on {numberMonth} months at the monthly rate of {self.interest_rate} %')
        self.deposit(12 * (self.interest_rate / 100) * self.balance)
