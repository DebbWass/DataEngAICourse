
    
"""This is the child class that inherets from parent"""
from parent import Parent
# import parent
 
 
class Child(Parent):
 
    def __init__(self, name, age):
        super().__init__(name, age)
   
 
if __name__ == "__main__":
    name = input("Insert input")
    claus = Parent(name, 200)
    claus.who_am_i()
    