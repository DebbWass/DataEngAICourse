import Customer
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
    def register_client(self,cust_name,cust_id):
        self.customers.append(Customer.Customer("Jack",112336))
    #    self.customers[cust_name].append(cust_name)
    #    self.customers[cust_balance].append(cust_balance)
    #    self.customers[cust_id].append(cust_id)
        self.number_of_clients+=1
    
    def __repr__(self):
        return f"Bank(No: {self.bank_num}, Branch: {self.branch_num} ,Address: {self.address})"
    '''
    #Deposit money:   
    def deposit(self, amount, cust_name, cust_id):
       self.customers["cust_balance"][cust_id]+=amount
   
   #withdraw money
    def withdraw(self,cust_id,cust_balance,amount):
        if self.customers["cust_balance"][cust_id]>amount:
            self.customers["cust_balance"][cust_id]-=amount
        else:
            print('Not enough money in the account for this withdraw... find a job!!!')
            
    def IsExistsCust(self,cust_id):
        if cust_id in self.customers["cust_id"]:
            return True
        return False
    '''  
      
if __name__=='__main__':
    b1=Bank(12,615,'Herzl 185 Rehovot')
    b1.__repr__()