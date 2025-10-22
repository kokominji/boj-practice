n = int(input())
a = list(map(int,input().split()))
v = int(input())
count = 0

for x in a:
    if x == v:
        count += 1
print(count)