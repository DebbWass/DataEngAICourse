import random

class SortList:
    def __init__(self):
        self.list = []
        
    def setList(self):
        for i in range(random.randint(5, 10)):
            self.list.append(random.randint(0,1000))
        return self.list
            
    def sortList(self):
        for i in range(len(self.list) - 1):
            for j in range(i + 1 , len(self.list)):
                if self.list[i] > self.list[j]:
                    temp = self.list[i]
                    self.list[i] = self.list[j]
                    self.list[j] = temp
        return self.list
                
if __name__ == '__main__':
    l1 = SortList()
    list1  = l1.setList()
    print(list1)
    l1.sortList()
    print(list1)
            
                
                    