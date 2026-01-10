class  Prime:
    def __init__(self, num):
        self.num = num
        
    def IsPrime(self):
        if self.num > 3 :
            if self.num%2 == 0:
                return False
            else:
                for i in range(3,self.num//2):
                    if self.num%i == 0:
                        return False
        return True
    

if __name__ == '__main__':
    p1 = Prime(18)
    p2 = Prime(7)
    p3 = Prime(15)
    p4 = Prime(23)
    
    print(p1.IsPrime())
    print(p2.IsPrime())
    print(p3.IsPrime())
    print(p4.IsPrime())