import random

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = random.randint(1000, 9999)
        self.balance = 0
        self.loan_limit = 2
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"deposited {amount}")
            return f"deposited {amount} successfully"
        else:
            return "invalid deposit amount"
        

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew {amount}")
                return f"withdrew {amount} successfully."
            else:
                return "withdrawal amount exceeded"
        else:
            return "Invalid withdrawal amount"
        

    def check_balance(self):
        return f"available balance: {self.balance}"

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_limit > 0 and amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Took a loan of {amount}")
            self.loan_limit -= 1
            return f"Loan of {amount} taken successfully"
        else:
            return "Unable to take a loan"
        



    def transfer(self, other_user, amount):
        if amount > 0 and self.balance >= amount:
            if other_user is not None:
                other_user.balance += amount
                self.balance -= amount
                self.transaction_history.append(f"Transfer {amount} to Account {other_user.account_number}")
                other_user.transaction_history.append(f"received {amount} from Account {self.account_number}")
                return f"Transferred {amount} to Account {other_user.account_number} successfully"
            else:
                return "account does not exist"
        else:
            return "Insufficient for the transfer"

class Admin:
    def __init__(self):
        self.user_accounts = []

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.user_accounts.append(user)
        return f"Account created successfully Account number: {user.account_number}"

    def delete_account(self, account_number):
        for user in self.user_accounts:
            if user.account_number == account_number:
                self.user_accounts.remove(user)
                return f"Account {account_number} deleted successfully"
        return "Account not found"

    def list_user_accounts(self):
        accounts = [f"Account {user.account_number}: {user.name}" for user in self.user_accounts]
        return "\n".join(accounts)

    def total_balance(self):
        total = sum(user.balance for user in self.user_accounts)
        return f"Total available balance in the bank: {total}"

    def total_loan_amount(self):
        total_loan = sum(2 - user.loan_limit for user in self.user_accounts)
        return f"Total loan amount in the bank: {total_loan}"

    def toggle_loan_feature(self, enable):
        for user in self.user_accounts:
            if enable:
                user.loan_limit = 2
            else:
                user.loan_limit = 0
        return "Loan feature is now enabled" if enable else "Loan feature is now disabled"

# banking system:
admin = Admin()

print(" Create User Account")
account1 = admin.create_account("sajal", "sajal@gmail.com", "chicago", "Savings")
account2 = admin.create_account("rafe", "rafe@gmail.com", "newyourk", "Current")

print(account1)
print(account2)

user1 = admin.user_accounts[0]
user2 = admin.user_accounts[1]
# deposit

print("\n Deposit and Withdraw")
print(user1.deposit(1000))
print(user1.withdraw(500))
print(user1.check_balance())
print(user1.withdraw(600)) 

# loan

print("\n Loan")
print(user1.take_loan(200))
print(user1.take_loan(300))  

# transfer
print("\n Transfer")
print(user1.transfer(user2, 200))
print(user1.transfer(None, 100))  
print(user1.transfer(user2, 1000))  

print("\nList User Accounts")
print(admin.list_user_accounts())

print("\n Total Balance & Loan Amount")
print(admin.total_balance())
print(admin.total_loan_amount())

print("\n Loan Feature")
print(admin.toggle_loan_feature(True))
print(user1.take_loan(300))  

print(admin.toggle_loan_feature(False))
print(user1.take_loan(200))  

print("\n Transaction")
print(user1.check_transaction_history())

def main():
    admin = Admin()
    
    while True:
        print("\nBanking Management System")
        print("1. User Operations")
        print("2. Admin Operations")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            user_menu(admin)
        elif choice == '2':
            admin_menu(admin)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def user_menu(admin):
    print("\nUser Operations")
    account_number = int(input("Enter your account number: "))
    
    user = find_user(admin, account_number)
    
    if user is None:
        print("Account not found.")
        return
    
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Take a Loan")
        print("6. Transfer Money")
        print("7. Back to Main Menu")
        
        choice = input("Enter your choice (1/2/3/4/5/6/7): ")
        
        if choice == '1':
            amount = float(input("Enter the deposit amount: "))
            print(user.deposit(amount))
        elif choice == '2':
            amount = float(input("Enter the withdrawal amount: "))
            print(user.withdraw(amount))
        elif choice == '3':
            print(user.check_balance())
        elif choice == '4':
            print("Transaction History:")
            for transaction in user.check_transaction_history():
                print(transaction)
        elif choice == '5':
            amount = float(input("Enter the loan amount: "))
            print(user.take_loan(amount))
        elif choice == '6':
            target_account_number = int(input("Enter the target account number: "))
            target_user = find_user(admin, target_account_number)
            if target_user:
                amount = float(input("Enter the transfer amount: "))
                print(user.transfer(target_user, amount))
            else:
                print("Account does not exist.")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.")

def admin_menu(admin):
    print("\nAdmin Operations")
    while True:
        print("\n1. Create User Account")
        print("2. Delete User Account")
        print("3. List User Accounts")
        print("4. Total Available Balance")
        print("5. Total Loan Amount")
        print("6. Toggle Loan Feature")
        print("7. Back to Main Menu")
        
        choice = input("Enter your choice (1/2/3/4/5/6/7): ")
        
        if choice == '1':
            name = input("Enter user's name: ")
            email = input("Enter user's email: ")
            address = input("Enter user's address: ")
            account_type = input("Enter user's account type (Savings/Current): ")
            print(admin.create_account(name, email, address, account_type))
        elif choice == '2':
            account_number = int(input("Enter the account number to delete: "))
            print(admin.delete_account(account_number))
        elif choice == '3':
            print("List of User Accounts:")
            print(admin.list_user_accounts())
        elif choice == '4':
            print(admin.total_balance())
        elif choice == '5':
            print(admin.total_loan_amount())
        elif choice == '6':
            enable_loan = input("Enable loan feature? (y/n): ").lower()
            if enable_loan == 'y':
                print(admin.toggle_loan_feature(True))
            elif enable_loan == 'n':
                print(admin.toggle_loan_feature(False))
            else:
                print("Invalid choice. Please enter 'y' or 'n")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7")

def find_user(admin, account_number):
    for user in admin.user_accounts:
        if user.account_number == account_number:
            return user
    return None

if __name__ == "__main__":
    main()
