n = int(input())
m = list(map(int,input().split()))
score = []
result = 0
a = max(m) 
for num in m:
    score.append((num / a) * 100)
for x in score:
    result += x
print(result / n)