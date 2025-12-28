import math

def calcBiggestDivider(a,b) -> int:
    return math.gcd(a,b)

def calcSmallestDivider(a,b) -> int:
    limit = min(abs(a), abs(b))
    for i in range(2, limit + 1):
        if a % i == 0 and b % i == 0:
            return i
    return 1  # they are coprime

def calcPower(a,b) -> int:
    return math.pow(a,b)

def sqrtDelta(a,b):
    return math.sqrt(a) - math.sqrt(b) 
   
def runLogic():
    options={'a':'the biggest devider',
         'b':'the smallest divider',
         'c':'the result of pow(a,b)',
         'd':'the result of sqrt(a)-sqrt(b)',
         'e':'exit'}

    a = int(input('Insert a number'))
    b = int(input('Insert a number'))

    print("\n" + "="*50)
    print(f"{'choice':20} {'Description':30}")
    print("="*50)
    for choice, description in options.items():
        print(f"{choice:<20} {description:<30}")
    print("="*50)
    
    action = input('Please make your choice')
    
    match action:
        case "a":
            print(f"the biggest divider is : {calcBiggestDivider(a,b)}")
        case "b":
            print(f"the smallest divider is : {calcSmallestDivider(a,b)}")
        
        case "c":
            print(f"the power is: {calcPower(a,b)}")            
        case "d":
            print(f"the result is: {sqrtDelta(a,b)}")
        case "e":
            exit()

runLogic()

