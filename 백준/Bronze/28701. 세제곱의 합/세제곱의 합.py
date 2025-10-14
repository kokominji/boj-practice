n = int(input())
A = 0
B = 0
C = 0

for i in range(1,n+1):
    A += i
    B += i
    C += (i*i*i)
print(A)
print(B * B)
print(C)