# ATM
Simple ATM Controller for coderbyte

In the code I added these test files:

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

I created bank with cardNum and PIN with 1234 and $1000.
Then created an ATM with $5000.
First I entered the atm with wrong PIN and cardNum.
Then tried to access ATM but was not able to.

Then I entered correct information.
And was able to access the ATM.
