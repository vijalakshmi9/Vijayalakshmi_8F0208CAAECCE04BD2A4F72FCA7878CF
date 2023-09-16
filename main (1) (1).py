class BankAccount:
    def __init__(self, acc_number, acc_holder_name, initial_balance=0):
        self.__account_number = acc_number
        self.__account_holder_name = acc_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        return f"Account Balance: ${self.__account_balance}"

# Create an instance of BankAccount
account1 = BankAccount("12345", "John Doe", 1000)

# Test deposit and withdrawal functionality
account1.deposit(500)
account1.withdraw(200)

# Display account balance
print(account1.display_balance()