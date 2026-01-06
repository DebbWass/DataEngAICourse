class Calculator():
    #constructor:
    def __init__(self):
        pass
    
    def ValidNum(self,num)->bool:
        try:
            val = float(num)
            return True
        except ValueError:
            print("That is not a valid number.")
            return False
    #sum
    def Add(self,a,b):
        
        if self.ValidNum(a) and self.ValidNum(b):
            return a+b
        return None
    
    #subtract
    def Subtract(self,a,b):
        if self.ValidNum(a) and self.ValidNum(b):
            return a-b
        return None
    
    #multiply
    def Multiply(self,a,b):
        if self.ValidNum(a) and self.ValidNum(b):
            return a*b
        return None
    
    #divide
    def Divide(self,a,b):
        if self.ValidNum(a) and self.ValidNum(b):
            if b==0:
                print('You cannot divide by 0')
            else:
                return a/b
        return None
    
if __name__ == '__main__':
    calc = Calculator()
    
    #chack if number validation works: 
    print(f'Add: {calc.Add('dsd','sdas')}')
    #check aithmetics:
    print(f'Add: {calc.Add(2,5)}')
    print(f'Sub: {calc.Subtract(10,8)}')
    print(f'Mul: {calc.Multiply(5,8)}')
    print(f'Div: {calc.Divide(9,3)}')
    #divide by 0:
    print(f'Div: {calc.Divide(5,0)}')
    