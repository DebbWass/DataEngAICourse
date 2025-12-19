a = int(input("insert first number "))
b= int(input("insert second number "))

c= a+b
d= a-b
e= a*b
f= a//b
"""
print("c =", int(c))
print ("d =", int(d))
print ("e =", int(e))
print ("f =", int(f))
"""
"""
# הדפסת טבלה
print("\n-----------------------------")
print(" פעולה |   תוצאה")
print("-----------------------------")
print(f" a + b |   {c}")
print(f" a - b |   {d}")
print(f" a * b |   {e}")
print(f" a // b |  {f}")
print("-----------------------------")
"""

print("-" * 60)
print(f"{'a':>5} | {'b':>5} | {'c=a+b':>5} | {'d=a-b':>5} | {'e=a*b':>5} | {'f=a//b':>5}")
print("-" * 60)
print(f"{a:>5} | {b:>5} | {c:>5} | {d:>5} | {e:>5} | {f:>5}")
print("-" * 60)



