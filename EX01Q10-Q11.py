#Q10
"""
a= int(input("insert a number"))
b = int(input("insert a number"))
c = int(input("insert a number"))
d= int(input("insert a number"))
e= int(input("insert a number"))

print((a+b-c)*d/e)
"""
#Q11
i= 0
ans=0

while i<5:
    match i:
        case 0:
            ans = ans + float(input("insert a number"))
        case 1:
            ans = ans + float(input("insert a number"))
        case 2:
             ans= ans - float(input("insert a number"))
        case 3:
            ans = ans * float(input("insert a number"))
        case 4:
            ans = ans / float(input("insert a number"))

    i = i + 1

print(ans)
