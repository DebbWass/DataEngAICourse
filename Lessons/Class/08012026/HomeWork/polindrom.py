class Polindrome:
    def __init__(self, string):
        self.string = str(string)
        
    def check_polindrome(self):
        for i in range(len(self.string) // 2):
            if self.string[i] != self.string[len(self.string) - 1 - i]:
                return False
        return True
    
    

if __name__ == '__main__':
    p1 = Polindrome('123321')
    p2 = Polindrome('fndajfh')
    p3 = Polindrome('madam')
    
    print(p1.string[-1])
    print(p1.check_polindrome()) 
    print(p2.check_polindrome())
    print(p3.check_polindrome())