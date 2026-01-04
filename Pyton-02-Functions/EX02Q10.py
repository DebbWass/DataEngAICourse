def isBuysAlot(val)->bool:
    if val>8000:
        return True
    return False

def isPayingOnTime(payOnTime)-> bool:
    if payOnTime.upper() == 'Y':
        return True
    return False

def isOldCust(yers) -> bool:
    if yers>5:
        return True
    return False

def isVIPCust(bigSpender, payOnTime, oldCust ) -> bool:
    if payOnTime or (bigSpender and (payOnTime or oldCust)) or (payOnTime and oldCust):
        return True
    return False

def printVip(custNum,isVip):
    if isVip:
        print(f'Give customer {custNum} special treatment')

custId = int(input("Insert cusstomer Id number"))
goodsValue = float(input("Insert the goods value of last year"))
payOnTime = str(input("Does client pay on time? insert (Y/N)"))
duration = int(input("How many years the client buys books from the company?"))

printVip(custId , isVIPCust(isBuysAlot(goodsValue), isPayingOnTime(payOnTime), isOldCust(duration)))
    
