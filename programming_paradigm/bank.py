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