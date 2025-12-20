import statistics

def avarage(sum,length):
    return sum/length

score = []

for i in range(5):
    score.append(int(input("Enter score: ")))

print(avarage(sum(score),len(score)))


#### Option 2 :

print(statistics.mean(score))