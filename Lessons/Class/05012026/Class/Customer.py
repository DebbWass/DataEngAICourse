import Account

class Customer():
    def __init__(self,name,id):
        self.name= name
        self.id = id
        self.accounts=[]
        
    def CreateAccount(self,bank_num,bank_branch,account_num):
        ac =Account.Account(bank_num,bank_branch,account_num)
        self.accounts.append(ac)
    
    def PrintCust(self):
        print(f'{self.name} , {self.id}, {self.accounts}')
        
    def CloseAccount(self,bank_num,bank_branch,account_num):
        for ac in self.accounts:
            if (ac.bank_num == bank_num and 
                ac.bank_branch == bank_branch and 
                ac.account_num == account_num):
                
                self.accounts.remove(ac)
                print(f"Account {account_num} removed successfully.")
                return # Exit once the first match is found
            
    print("Account not found.")
        


if __name__ == '__main__':
    c1=Customer('dorit',12345)
    c1.CreateAccount(12,615,12345)
    c1.CreateAccount(18,456,2222)
    c1.PrintCust()
    c1.CloseAccount(18,456,2222)
    c1.PrintCust()