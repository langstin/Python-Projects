class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def show_balance(self):
        print(f"{self.owner}: {self.balance}")

s1 = BankAccount("langstin", 1000)
s2 = BankAccount("drake", 2500)

s1.show_balance()
s1.deposit(500)
s1.show_balance()
s1.withdraw(100)
s1.show_balance()

s2.show_balance()
s2.deposit(1000)
s2.show_balance()
s2.withdraw(800)
s2.show_balance()
s2.withdraw(100000)
