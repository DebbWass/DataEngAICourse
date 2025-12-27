def digitCount(num):
    digCounter = 0
    
    while num>1:
        digCounter+=1
        num = num//10
    
    return digCounter

num = float(input('Insert number'))

while num!=-999:
    
    print(f'number of digits in {num} : {digitCount(num)}')
    num = float(input('Insert number'))