class Account():
    
    def __init__(self,bank_num,bank_branch,account_num):
        self.bank_num = bank_num
        self.bank_branch = bank_branch
        self.account_num = account_num
        self.account_balance=0
        self.overdraft_limit = -1000
    
    def __repr__(self):
        return f"Account(Bank: {self.bank_num}, Branch: {self.bank_branch} , Acc_no: {self.account_num}, Balance: {self.account_balance})"

    #deposit money to account:
    def deposit(self,amount):
        self.account_balance+=amount
        return self.account_balance
    
    #withdraw money:
    def Withdraw(self,amount):
        if self.account_balance - amount >= self.overdraft_limit:
            self.account_balance-=amount
            return self.account_balance
        else:
            print("You have reached your overdraft's limit, you cannot withdraw money")
        