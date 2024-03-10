
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    # Function to deposit amount
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Amount {amount} deposited successfully. New balance: {self.balance}')
        else:
            print('Invalid deposit amount. Please enter a positive value.')

    # Function to withdraw amount
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'Amount {amount} withdrawn successfully. Remaining balance: {self.balance}')
        elif amount > self.balance:
            print('Insufficient balance for withdrawal.')
        else:
            print('Invalid withdrawal amount. Please enter a positive value.')

    # Function to check the remaining balance
    def check_balance(self):
        print(f'Current balance: {self.balance}')


def main():
    account = BankAccount()

    while True:
        print("\nWelcome to the Banking Management System")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 3:
            account.check_balance()
        elif choice == 4:
            print("Thank you for using our Banking Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()