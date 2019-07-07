####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.




class Account():
    def __init__(self,name,amount):
        self.owner=name
        self.amount=amount

    def deposit(self,amount):
        self.amount+=amount
    
    def withdraw(self,withdraw):
        if(withdraw > self.amount):
            return "Insufficent Balance"
        else:
            self.amount -= withdraw
            return self.amount

    def __repr__(self):
        return f"The account name is {self.owner} and his balance is {self.amount}"


#1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)




# 3. Show the account owner attribute
acct1.owner




# 4. Show the account balance attribute
acct1.amount




# 5. Make a series of deposits and withdrawals
acct1.deposit(50)




acct1.withdraw(75)




# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)



# ## Good job!
print(acct1)
