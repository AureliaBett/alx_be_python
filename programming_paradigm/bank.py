class BankAccount1:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.account_balance = 0
    def userDetails(self):
        userName = f"Name {self.name}\n"
        userID = f"ID {self.ID}"
        return userName,userID
    def read_account_Balance(self):
        print(f"Your bank account balance: {self.account_balance}")
    
    def deposit(self):
        amount = int(input(f"Deposit: "))
            
        self.account_balance += amount
        
    
    def withdraw(self):
        amount = int(input(f"Withdraw: "))
            
        self.account_balance -= amount
    def Option(self):
        while True:
            
            Option = input("Deposit or Withdraw: ")
            if Option == "Deposit":
                my_account.deposit()
                my_account.read_account_Balance()
                break
            elif Option == "Withdraw":
                my_account.withdraw()
                my_account.read_account_Balance()
                break
            else:
                print("Invald Input. Try Again")
        

my_account = BankAccount1("Aurelia", "351703" )
print(my_account.userDetails())
my_account.Option()





import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()