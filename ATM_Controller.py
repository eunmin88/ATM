class Bank:
    def __init__(self):
        self.users = {}
        
    def addUser(self, cardNum, pin, account, balance):
        if cardNum and pin and account and balance:
            self.users[cardNum] = {"account":account, "pin":pin, "balance":balance}
            return True
        return False
    
    def update(self, amt, cardNum):
        if cardNum in self.users:
            self.users[cardNum]["balance"] = amt
            return True
        return False
    
    def checkPin(self, pin, cardNum):
        if cardNum in self.users and self.users[cardNum]["pin"] == pin:
            return self.users[cardNum]["balance"]
        return None

class ATM:
    def __init__(self, bank, amt):
        self.Bank = bank
        self.balance = None
        self.amt = amt
        
    def enter(self, card_num, pin):
        self.balance = self.Bank.checkPin(card_num, pin)
        if self.balance is None:
            print("Wrong Pin!")
            print("\n")
            return 0
            
        else:
            print("Welcome to the ATM!")
            print("\n")
            return 1
            
        

    def check(self, cardNum):
        
        if self.balance is None or cardNum not in self.Bank.users:
            print("Please enter the correct Card Num and Pin before trying to check your balance")
        else:
            print("Current Balance: " + str(self.Bank.users[cardNum]["balance"]))
            
        print("\n")

    def withdraw(self, money, cardNum):
        
        if self.balance is None or cardNum not in self.Bank.users:
            print("Please enter the correct Card Num and Pin before trying to Withdraw")
            
        elif self.balance > money and money < self.amt:
            print("Successfully withdrawed: " + str(money))
            print("Old Balance: " + str(self.balance))
            
            self.balance -= money
            self.amt -= money
            self.Bank.update(self.balance, cardNum)
            
            print("New Balance: "+ str(self.Bank.users[cardNum]["balance"]))

        elif self.balance < money:
            print("Not enough Balance to withdraw")
            print("Withdrawable amount: " + str(self.balance))

        else:
            print("ATM does not have enough money to withdraw")
            print("Withdrawable amount: " + str(self.amt))
            
        print("\n")
        
    def deposit(self, money, cardNum):
        
        if self.balance is None or cardNum not in self.Bank.users:
            print("Please enter the correct Card Num and Pin before trying to Deposit")
        else:
            print("Successfully deposited: " + str(money))
            print("Old Balance: " + str(self.balance))
            
            self.balance += money
            self.amt += money
            self.Bank.update(self.balance, cardNum)
            
            print("New Balance: "+ str(self.Bank.users[cardNum]["balance"]))
        print("\n")
        
    def curAmt(self):
        print("ATM currently has " + str(self.amt))

        
            

bank = Bank()
bank.addUser(1234, 1234, "Checking", 1000)

atm = ATM(bank, 5000)
atm.enter(0, 0)
atm.withdraw(111, 1234)
atm.check(1234)
atm.deposit(1154235, 1234)
atm.check(1234)

atm.enter(1234, 1234)

atm.withdraw(1111111, 1234)
atm.withdraw(111, 1234)
atm.withdraw(111, 1235)

atm.check(1234)
atm.deposit(1135, 1234)
atm.deposit(1135, 1235)

atm.check(1235)
atm.curAmt()


