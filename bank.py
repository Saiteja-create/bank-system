import random
import sys

class accounts:
    def __init__(self, owner, id, password, current_balance):
        self.owner = owner
        self.id = id
        self.password = password
        self.current_balance = int(current_balance)

    def withdraw(self, number):
        # The password check is now delegated to this reusable method
        if self.verify_password():
            if self.current_balance >= number: # FIX: Use >= to allow withdrawing full balance
                self.current_balance -= number
                print(f"Withdrawal successful. New balance: {self.current_balance}")
            else:
                print("Insufficient money.")

    def deposit(self, number):
        if number > 0:
            self.current_balance += number
            print(f"Deposit successful. New balance: {self.current_balance}")
        else:
            print("Number should be positive.")

    def verify_password(self):
        entered_password = input("For security, please re-enter your password: ")
        if entered_password == self.password:
            return True
        else:
            print("Incorrect password. Transaction cancelled.")
            return False

class bank:
    created_accounts = []

    def create_account(self):
        # This loop is more robust for finding a truly unique ID
        while True:
            account_id = random.randint(1000, 9999)
            id_is_unique = True
            for acc in bank.created_accounts:
                if acc.id == account_id:
                    id_is_unique = False
                    break
            if id_is_unique:
                break
        
        name = input("Enter your name: ")
        password = input("enter your password: ")
        account = accounts(name, account_id, password, 0)
        print(f"Account created successfully. Your account ID is {account_id}")
        bank.created_accounts.append(account)

    def login_account(self):
        not_found = True
        print("Enter 0 to go to the main page.")
        
        try:
            search = int(input("Enter your account ID: "))
        except ValueError:
            print("Invalid ID. Please enter numbers only.")
            return

        if search == 0:
            return

        for user in bank.created_accounts:
            if search == user.id:
                not_found = False
                if user.verify_password():
                    # Start the dedicated transaction loop
                    while True:
                        print("\n--- Transaction Menu ---")
                        print("1. Check balance")
                        print("2. Withdraw money")
                        print("3. Deposit money")
                        print("4. Logout")
                        
                        try:
                            opinion = int(input("Enter (1-4): "))
                        except ValueError:
                            print("Invalid option. Please enter a number.")
                            continue

                        if opinion == 1:
                            print(f"Your balance is: {user.current_balance}")
                        elif opinion == 2:
                            take = int(input("Enter the amount to withdraw: "))
                            user.withdraw(take)
                        elif opinion == 3:
                            add = int(input("Enter the amount to add: "))
                            user.deposit(add)
                        elif opinion == 4: # FIX: Specific exit condition
                            print("Logging out...")
                            break # Exit the transaction loop
                        else: # FIX: Handle invalid numbers
                            print("Invalid option. Please choose 1-4.")
                else:
                    print("Entered password is wrong.")
                break # Exit the search loop once the user is found and dealt with

        if not_found:
            print("Account not found.")

def main_page():
    my_bank = bank()
    while True:
        print("\n--- Welcome to our bank! ---")
        print("1. Create a New account")
        print("2. Login to your account")
        print("3. Exit")
        
        response = input("Enter (1-3): ")
        
        if response == "1":
            my_bank.create_account()
        elif response == "2":
            my_bank.login_account()
        elif response == "3":
            print("Thank you for using our bank.")
            break
        else: # SUGGESTION: Handle invalid main menu input
            print("Invalid option. Please choose 1, 2, or 3.")

# Run the main program
main_page()
    


         