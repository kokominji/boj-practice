t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)
    a = []
    for q in s:
        for i in range(r):
            a.append(q)
    print(*a, sep='')
    