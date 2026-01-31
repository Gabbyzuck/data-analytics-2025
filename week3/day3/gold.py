# =========================
# Part I: BankAccount
# =========================

class BankAccount:
    def __init__(self, balance, username, password):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            return True
        return False

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated")

        if amount <= 0:
            raise Exception("Deposit amount must be positive")

        self.balance += amount

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated")

        if amount <= 0:
            raise Exception("Withdrawal amount must be positive")

        self.balance -= amount


# =========================
# Part II: MinimumBalanceAccount
# =========================

class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, username, password, minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated")

        if amount <= 0:
            raise Exception("Withdrawal amount must be positive")

        if self.balance - amount < self.minimum_balance:
            raise Exception("Cannot withdraw: minimum balance would be breached")

        self.balance -= amount


# =========================
# Part IV: BONUS ATM Class
# =========================

class ATM:
    def __init__(self, account_list, try_limit):
        # Validate account_list
        if not all(isinstance(acc, BankAccount) for acc in account_list):
            raise Exception("account_list must contain only BankAccount objects")

        self.account_list = account_list

        # Validate try_limit
        if not isinstance(try_limit, int) or try_limit <= 0:
            print("Invalid try_limit provided. Defaulting to 2.")
            self.try_limit = 2
        else:
            self.try_limit = try_limit

        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n--- ATM MAIN MENU ---")
            print("1. Log in")
            print("2. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")

    def log_in(self, username, password):
        for account in self.account_list:
            if account.authenticate(username, password):
                print("Login successful!")
                self.show_account_menu(account)
                return

        self.current_tries += 1
        print("Invalid credentials.")

        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down.")
            exit()

    def show_account_menu(self, account):
        while True:
            print("\n--- ACCOUNT MENU ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")

            choice = input("Select an option: ")

            try:
                if choice == "1":
                    amount = int(input("Enter deposit amount: "))
                    account.deposit(amount)
                    print(f"New balance: {account.balance}")

                elif choice == "2":
                    amount = int(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                    print(f"New balance: {account.balance}")

                elif choice == "3":
                    print("Logging out.")
                    break

                else:
                    print("Invalid option.")

            except Exception as e:
                print(f"Error: {e}")


# =========================
# Example usage (optional)
# =========================

if __name__ == "__main__":
    acc1 = BankAccount(500, "alice", "1234")
    acc2 = MinimumBalanceAccount(1000, "bob", "abcd", minimum_balance=300)

    atm = ATM([acc1, acc2], try_limit=3)
