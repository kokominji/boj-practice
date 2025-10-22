n, m = map(int,input().split())
a = []
# 1. 바구니 만들기
for x in range(1,n+1):
    a.append(x)
for y in range(m):
    i, j = map(int,input().split())
    a[i-1:j] = reversed(a[i-1:j])
print(*a)