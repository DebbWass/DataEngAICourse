import Account

class Customer():
    def __init__(self,name,id):
        self.name= name
        self.id = id
        self.accounts=[]
        self.account_balance = 0
        
    
    def __repr__(self):
        return f"Customer(Name: {self.name}, ID: {self.id}, Acc: {self.accounts})"
    
    #create account   
    def CreateAccount(self,account):
        #ac =Account.Account(bank_num,bank_branch,account_num)
        self.accounts.append(account)
    
    #close account   
    def CloseAccount(self,bank_num,bank_branch,account_num):
        for ac in self.accounts:
            if (ac.bank_num == bank_num and 
                ac.bank_branch == bank_branch and 
                ac.account_num == account_num):
                
                self.accounts.remove(ac)
                print(f"Account {account_num} removed successfully.")
                return # Exit once the first match is found
            
        print("Account not found.")
        
    #find account
    def FindAcc(self,bank,branch,acc_id):
        account = next((acc for acc in self.accounts if (acc.bank_num == bank and acc.bank_branch == branch and acc.account_num == acc_id)), None)
        
        if account:
            print(f"Found: {account}")
        else:
            print("Account not found.")
    
    #calculate customer balance:
    def CalcCustBalance(self):
        cust_total_balance = 0
        for acc in self.accounts:
            cust_total_balance+=acc.account_balance
        return cust_total_balance
        


# if __name__ == '__main__':
#     c1=Customer('dorit',12345)
#     c1.CreateAccount(12,615,12345)
#     c1.CreateAccount(18,456,2222)
#     c1.PrintCust()
#     c1.CloseAccount(18,456,2222)
#     c1.PrintCust()