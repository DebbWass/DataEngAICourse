class Account():
    
    def __init__(self,bank_num,bank_branch,account_num):
        self.bank_num = bank_num
        self.bank_branch = bank_branch
        self.account_num = account_num
        self.account_balanc=0
    
    def __repr__(self):
        return f"Account(No: {self.account_num}, Branch: {self.bank_branch} , Acc_no: {self.account_num}, Balance: {self.account_balanc})"
    
    
        