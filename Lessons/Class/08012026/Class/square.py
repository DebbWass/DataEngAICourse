from shape import Shape

class Square(Shape): 
    def __init__(self, edges, nodes):
       
        super().__init__(edges, nodes)
        self.edge_length = 0
    
    def set_edge_length(self, length):
        self.edge_length = length
        
    def CalcParimeter(self,length):
        print(f"Perimeter: {4 * self.edge_length}")
        return 4 * self.edge_length
        
    def CalcArea(self,length):
        area = self.edge_length ** 2
        print(f"Area: {area}")
        return area



if __name__ == '__main__':
    s1 = Square(4, 4)
    s1.set_edge_length(3) 
    s1.CalcArea()         
    s1.CalcParimeter()