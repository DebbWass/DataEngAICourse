def square(num):
    return num * num


def ans_table ():

    innerStr = ""

    num = float(input("insert number"))
    innerStr = innerStr + f"{num:>10} | {square(num):>10}"

    return innerStr


ansStr = ""
ansStr = "\n" + "-" * 30
ansStr = ansStr + "\n" + f"{'num':>10} | {'num^2':>10}"
ansStr = ansStr + "\n" + "-" * 30

for i in range(3):
    ansStr = ansStr + "\n" + ans_table()


ansStr = ansStr + "\n" + "-" * 30

print(ansStr)