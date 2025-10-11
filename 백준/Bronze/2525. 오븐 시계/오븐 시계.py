import sys
input = sys.stdin.readline

A, B = map(int,input().split())
C = int(input())

if B + C < 60:
    B = B+C
else:
    A = A+(B+C) // 60
    B = (B+C) %60
A = A % 24
print(A,B)