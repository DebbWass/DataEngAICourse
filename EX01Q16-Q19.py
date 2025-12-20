#Q16

def vat_value(cost):
    return cost - cost/1.17


#cost = float(input("Insert cost: "))

#print(round(vat_value(cost),2))

#Q17

def total_price(cost):
    return cost * 1.17

#cost = float(input("Insert cost: "))

#print(round(total_price(cost),2))

#Q18 + Q19

cost = float(input("Insert cost: "))

print("price no vat: " + str(round(cost - vat_value(cost),2)) + "\n" + "vat_value: " + str(round(vat_value(cost),2)))
