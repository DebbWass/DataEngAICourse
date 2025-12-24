print("This program solves a system of two linear equations")

a1, b1, c1 = map(int, input("Enter the coefficients of the first equation (a1, b1, c1): ").split())

a2, b2, c2 = map(int, input("Enter the coefficients of the second equation (a2, b2, c2): ").split())

denominator = a1*b2-a2*b1

x= (c1*b2-c2*b1)/denominator
y = (a1*c2-a2*c1)/denominator
print(f'x = {x} , y = {y}')
