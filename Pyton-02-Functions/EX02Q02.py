from statistics import mean

def avg(n):
    nums = []
    
    for i in range(n):
        nums.append(int(input('Insert a number')))
    
    return mean(nums)

print(f'{avg(int(input('insert a numver')))}')