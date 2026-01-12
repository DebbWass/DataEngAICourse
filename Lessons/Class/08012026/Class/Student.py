from child import Child

#student class

class Student(Child):
    def __init__(self, name, age,school):
        super().__init__(name, age)
        self.school = school
    
    def who_am_i(self):
        print(f'I am {self.name}, I am {self.age}, I am studying at {self.school}')
        
        


if __name__ == "__main__":
    Yossie = Student("Yossie", 25, 'Huji')
    Yossie.who_am_i()
    
    


    