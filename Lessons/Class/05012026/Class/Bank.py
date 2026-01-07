import Customer as Cust
import Account as Acc

#this is class Bank
class Bank():
    
    #constructor:
    def __init__(self,bank_num,branch_num,address):
        self.bank_num = bank_num
        self.branch_num = branch_num
        self.address = address
        self.customers = []
        self.number_of_clients = 0
        
    
    #add cust to bank:
    def register_client(self,cust):
        self.customers.append(cust)
        self.number_of_clients+=1
    
    def __repr__(self):
        return f"Bank(No: {self.bank_num}, Branch: {self.branch_num} ,Address: {self.address})"
    
    def PrintCustList(self):
        return self.customers
    
    #find customer
    def FindCust(self,cust_id):
        customer = next((c for c in self.customers if c.id == cust_id), None)
        
        if customer:
            print(f"Found: {customer}")
        else:
            print("Customer not found.")

    #find accont:
    def FindAccount(self,bank,branch,acc_id):
        
        customer = next((c for c in self.customers if any(
        a.bank_num == bank and a.bank_branch == branch and a.account_num == acc_id 
        for a in c.accounts
        )), None)
        
        if customer:
            print(f"Found: {customer}")
        else:
            print("account not found.")
            
    #bank total balance
    def CalcBankBalance(self):
        bank_total_balance = 0
        for c in self.customers:
            bank_total_balance+=c.CalcCustBalance()
        return bank_total_balance
    
       
      
if __name__== '__main__':
    b1=Bank(12,615,'Herzl 185 Rehovot')
    print(b1)
    cust1 = Cust.Customer('Dorit',123456)
    cust1.CreateAccount(Acc.Account(b1.bank_num,b1.branch_num,123115))
    print(cust1)
    b1.register_client(cust1)
    print(f'total custs in Bank : {b1.number_of_clients}')
    
    #deposit to account
    Acc.Account.deposit(cust1.accounts[0],500)
    print(b1.PrintCustList())
    #withdraw:
    Acc.Account.Withdraw(cust1.accounts[0],200)
    print(b1.PrintCustList())
    Acc.Account.Withdraw(cust1.accounts[0],2000)
    print(b1.PrintCustList())
    b1.FindCust(123456)
    cust1.FindAcc(12,615,123115)
    b1.FindAccount(12,615,123115)
    
    #add anothe account for cust1:
    cust1.CreateAccount(Acc.Account(b1.bank_num,b1.branch_num,123180))
    Acc.Account.deposit(cust1.accounts[1],500)
    print(cust1)
    print(cust1.CalcCustBalance())
    
    #register new cust:
    cust2 = Cust.Customer('Jack',112585)
    cust2.CreateAccount(Acc.Account(b1.bank_num,b1.branch_num,125854))
    b1.register_client(cust2)
    Acc.Account.deposit(cust2.accounts[0],1500)
    print(f'total custs in Bank : {b1.number_of_clients}')
    print(b1.PrintCustList())
    print(b1.CalcBankBalance())