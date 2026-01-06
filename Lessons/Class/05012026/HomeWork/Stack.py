class Stack():
    def __init__(self):
        self.stak = []
        
    #print stack items
    def __repr__(self):
        print(self.stak)
        
    #add item to stack
    def AddItem(self, item):
        self.stak.append(item)
    
    #remove item
    def RemoveItem(self):
        self.stak.pop()
        
    #Empty stack
    def EmptyStack(self):
        self.stak.clear()
    
    #Count items:
    def CountItems(self):
        return len(self.stak)
    
    #count Item in list:
    def CountItem(self,item):
        return self.stak.count(item)
    
    #peek top item
    def PeekItem(self):
        print(self.stak[-1])
    
    def SearchItem(self,item):
        if item in self.stak:
            return True
        return False
        
        
        
        
if __name__ == '__main__':
    s1 = Stack()
    
    s1.__repr__()
    s1.AddItem('book')
    s1.__repr__()
    s1.AddItem('shoes')
    s1.__repr__()
    s1.RemoveItem()
    s1.__repr__()
    s1.AddItem('apples')
    s1.AddItem('13213')
    s1.AddItem('s5546s')
    s1.__repr__()
    print(f'count: {s1.CountItems()}')
    print(f'count : {s1.CountItem('apples')}')
    print(s1.SearchItem('apples'))
    print(s1.SearchItem('app1231les'))
    s1.PeekItem()
    s1.EmptyStack()
    s1.__repr__()