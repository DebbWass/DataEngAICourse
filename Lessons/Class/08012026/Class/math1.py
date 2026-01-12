"""This is the class math, it runs some arithmetic
calculations like addition, substraction, multiplication, and division"""

class Math:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def sdd(self):
        return self.x + self.y
    
    def sub(self):
        return self.x - self.y
    
    def mul(self):
        return self.x * self.y
    
    def div(self):
        if self.y != 0:
            return self.x / self.y
        return None
    