import math

class Circle():
    #constructor
    def __init__(self, radius):
        self.radius = radius
        
    #perimeter:
    def CalcPerimeter(self) ->float:
        return self.radius*math.pi*2
    
    #area:
    def CalcArea(self)->float:
        return math.pi*self.radius**2
    
    
if __name__ == '__main__':
    
    c1=Circle(5)
    print(f'the perimeter: {round(c1.CalcPerimeter(),2)}')
    print(f'the area: {round(c1.CalcArea(),2)}')
    