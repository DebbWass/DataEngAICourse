

amount = int(input('Insert the change amount'))

changeMethod(amount)



def changeMethod(amount):
    
    while amount > 0:
        
        if amount>=100:
            print(f'In 100 : {amount//100}')
            amount = amount%100
        elif amount>=50:
            print(f'In 50 : {amount//50}')
            amount = amount%50
        elif amount>=20:
            print(f'In 20 : {amount//20}')
            amount = amount%20
        elif amount>=10:
            print(f'In 10 : {amount//10}')
            amount = amount%10
        elif amount>=5:
            print(f'In 5 : {amount//5}')
            amount = amount%5
        elif amount>=2:
            print(f'In 2 : {amount//2}')
            amount = amount%2
        else:
            print(f'In 1 : {amount//1}')
            amount = amount%1