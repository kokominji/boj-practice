a, b = map(int,input().split())
c = int(input())

if (b + c >= 60):
    a += (b+c) // 60
    b = (b+c) % 60
else:
    b = b + c
a %= 24
print(a, b)