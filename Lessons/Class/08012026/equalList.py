import random

class EqualsList:
    def __init__(self):
        self.list1 = []
        self.list2 = []
        
    def setList(self):
        tempList = []
        for i in range(random.randint(5, 10)):
            tempList.append(random.randint(0,1000))
        return tempList
    
    def IsListsEqual(self):
        
        if len(self.list1) == len(self.list2):
            self.list1 = sorted(self.list1)
            self.list2 = sorted(self.list2)
            for item1,item2 in zip(self.list1,self.list2):
                if item1 != item2:
                    return False
            return True
        else:
            return False


if __name__ == '__main__':
    l1 = EqualsList()
    l1.list1 = l1.setList()
    l1.list2 = l1.setList()
    print(l1.list1)
    print(l1.list2)
    
    print(l1.IsListsEqual())
    
    l2 = EqualsList()
    l2.list1 = l2.list2 = l2.setList()
    #l1.list2 = l1.setList()
    print(l2.list1)
    print(l2.list2)
    
    print(l2.IsListsEqual())
    
    
    
    
    
    
    