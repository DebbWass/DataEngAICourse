import math

def check_det_a(a) -> bool:
    if a>0:
        return True
    return False

def calc_quadratic(a,b,c):
    if check_det_a(a) == True:
        discriminant = b**2 - 4*a*c
        
        if discriminant<0:
            print('There is no real solution, the discriminant is negative')
            return None
        else:
            x1 = round((-b + math.sqrt(discriminant))/2*a,2)
            x2 = round((-b - math.sqrt(discriminant))/2*a,2)
            
            if discriminant == 0:
                print(f'the only solutuin is: {x1}')
            else:
                print(f'the solution is: ')
                print(f'x1= {x1}')
                print(f'x2= {x2}')
                return(x1,x2)
 
    else:
        print('a must be larger than 0')
        return None
    

print("\n" + "="*50)
print("הזן מקדמים למשוואה שלך:")
try:
    a = float(input("הכנס את a: "))
    b = float(input("הכנס את b: "))
    c = float(input("הכנס את c: "))
    print("\n" + "="*50)
    calc_quadratic(a, b, c)
except ValueError:
    print("שגיאה: יש להזין מספרים בלבד")   