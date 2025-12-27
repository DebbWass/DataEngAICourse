def isEven(num):
    if num%2 == 0:
        return 0
    else:
        return 1
    
print(f'{isEven(float(input('Insert number')))}')