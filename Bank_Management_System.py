class Bank:
    account_list = []
    bank_balance = 0
    loan_balance = 0

    bankrupt = False
    loanOff = False
    

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type

        self.balance = 0
        self.account_number = self.account_type+ self.name + self.email

        self.transaction_history = []
        self.loan_opportunities = 2

        Bank.account_list.append(self)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            Bank.bank_balance += amount

            history = f"You have deposited {amount}"
            self.transaction_history.append(history)

            print(f"Deposit-> {amount} successful.")
            print(f"Your Balance: {self.balance}")

        else:
            print("Invalid Amount!")
    
    def withdraw(self, amount):
        if Bank.bankrupt == False:
            if amount >= 0 and amount <= self.balance:
                self.balance -= amount
                Bank.bank_balance -= amount

                history = f"You have withdrawn {amount}"
                self.transaction_history.append(history)

                print(f"Withdraw-> {amount} successful")
                print(f"Your Balance: {self.balance}")
            
            else :
                print("Withdrawal amount exceeded")

        else:
            print("The bank is bankrupt")

    def loan(self, amount):
        if Bank.loanOff == False:
            if self.loan_opportunities != 0:
                self.loan_opportunities -= 1
                if amount > 0:
                    self.balance += amount
                    Bank.loan_balance += amount

                    history = f"Loan amount-> {amount}"
                    self.transaction_history.append(history)
            else:
                print("Loan opportunity is not availabale for you!")
        
        else:
            print("Loan opportunity is currently unavailable for all!")

    def trasnfer_amount(self, name, email, account_type, amount):
        temp_account = account_type + name + email

        found = False
        for account in Bank.account_list:
            if temp_account == account.account_number:
                if amount >= 0 and amount <= self.balance:
                    self.balance -= amount
                    account.balance += amount
                    print("Transfer Successful")
                    history = f"Your have transffered {amount} to account: {temp_account}"
                    self.transaction_history.append(history)
                else:
                    print("You have not enough balance to transfer money!")
                found = True
                break
        
        if found == False:
            print("Account does not exist")
                

    
    def check_balance(self):
        print(f"Your balance: {self.balance}")
    
    def check_transaction_history(self):
        print("\nTransaction History: \n")
        for history in self.transaction_history:
            print(history)


class User_Account(Bank):
    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address, account_type)


class Admin_Account:
    
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def delete_account(self, name, email, account_type):
        temp_account = account_type + name + email
        found = False
        for account in Bank.account_list:
            if temp_account == account.account_number:
                Bank.account_list.remove(account)
                found = True
                print("Account is deleted.")
                break
        if found == False:
            print("Account does not exist")
        
    def see_all_account(self):
        for account in Bank.account_list:
            print(f"Name: {account.name} Email: {account.email} Address: {account.address} Account Type {account.account_type} Balance: {account.balance}")
    
    def total_bank_balance(self):
        print(f"Total bank balance is: {Bank.bank_balance}")
    
    def total_loan_amount(self):
        print(f"Total loan amount is: {Bank.loan_balance}")
    
    def loan_switch(self, switch):
        if switch == "off":
            Bank.loanOff = True
        elif switch == "on":
            Bank.loanOff = False

    def bankrupt_switch(self, switch):
        if switch == "off":
            Bank.bankrupt = True
        elif switch == "on":
            Bank.bankrupt = False
    


current_user = None
admin = Admin_Account("admin", "@1234")

while(True):
    if current_user == None:
        option = input("\n1. ADMIN\n2. USER\n3. EXIT\nEnter your choice: ")
        if option == "1":
            print(f"ADMIN ID: {admin.name}, ADMIN PASSWORD: {admin.password}")
            id = input("Enter id: ")
            password = input("Enter password: ")
            if id == admin.name and password == admin.password:
                current_user = admin
            else:
                print("Wrong id or password")

        elif option == "2":
            ch = input("Log in or Registration? (L/R)")
            
            if ch == "R":
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                address = input("Enter your address: ")
                accountType = input("Enter your account type (Write 'Savings'): ")

                current_user = User_Account(name, email, address, accountType)

            elif ch == "L":
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                accountType = input("Enter your account type (Write 'Savings'): ")
                temp_account = accountType + name + email

                found = False
                for account in Bank.account_list:
                    if temp_account == account.account_number:
                        current_user = account
                        found = True
                        break
                
                if found == False:
                    print("This user is not available.")
        
        elif option == "3":
            current_user = None
            break

    else:
        if current_user == admin:
            print(f"\nWelcome {current_user.name}\n")
            print("0. Create Account")
            print("1. Delete Account")
            print("2. See All User Account Lists")
            print("3. Total Available Balance of the Bank")
            print("4. Total Available Loan Amount of the Bank")
            print("5. Control Loan Option")
            print("6. Control 'Bankrupt'")
            print("7. Logout")
            op = input("Choose Option: ")
            if op == "0":
                name = input("Enter user's name: ")
                email = input("Enter user's email: ")
                address = input("Enter user's address: ")
                accountType = input("Enter user's account type (Write 'Savings'): ")
                User_Account(name, email, address, accountType)

            elif op == "1":
                name = input("Enter account name: ")
                email = input("Enter account email: ")
                accountType = input("Enter account type (Write 'Savings'): ")

                current_user.delete_account(name, email, accountType)

            elif op == "2":
                current_user.see_all_account()

            elif op == "3":
                current_user.total_bank_balance()

            elif op == "4":
                current_user.total_loan_amount()

            elif op == "5":
                switch = input("on or off: ")
                current_user.loan_switch(switch)

            elif op == "6":
                switch = input("on or off: ")
                current_user.bankrupt_switch(switch)

            elif op == "7":
                current_user = None


        elif current_user.account_type == "Savings":
            print(f"\nWelcome {current_user.name}\n")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Check Transaction History")
            print("5. Take loan")
            print("6. Transfer amount to another account")
            print("7. Logout")
            op = input("Choose Option: ")
            if op == "1":
                amount = int(input("Enter amount: "))
                current_user.deposit(amount)

            elif op == "2":
                amount = int(input("Enter amount: "))
                current_user.withdraw(amount)
            
            elif op == "3":
                current_user.check_balance()

            elif op == "4":
                current_user.check_transaction_history()

            elif op == "5":
                amount = int(input("Enter loan amount: "))
                current_user.loan(amount)

            elif op == "6":
                name = input("Enter account name: ")
                email = input("Enter account email: ")
                accountType = input("Enter account type (Write 'Savings'): ")
                amount = int(input("Enter amount: "))
                current_user.trasnfer_amount(name, email, accountType, amount)

            elif op == "7":
                current_user = None


        