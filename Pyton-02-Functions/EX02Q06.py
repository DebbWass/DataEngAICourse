def discount(price,dicount):
    return price-(price*dicount/100)

def calcDiscount(price):
    if price>1000:
        print(f'Price after discount: {discount(price,int(input('Insert discount value')))}')
    else:
        print(f'Price after discount: {price*.9}')


price = int(input('Insert item price'))
calcDiscount(price)