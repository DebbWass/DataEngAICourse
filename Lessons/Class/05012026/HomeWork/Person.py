from datetime import datetime, date

class Person():
    #constructor:
    def __init__(self, name, country, birth_date):
        self.name = name
        self.country = country
        self.birth_date = birth_date
    
    def CalcPersonAge(self):
        age = date.today().year - datetime.strptime(self.birth_date, "%d/%m/%Y").date().year
        if (date.today().month) < (datetime.strptime(self.birth_date, "%d/%m/%Y").date().month):
            age -= 1
        return age    
    
if __name__ == '__main__':
    p1 = Person('Dorit','Israel','02/05/1982')
    print(f'The age of {p1.name} from {p1.country} is: {p1.CalcPersonAge()}')
