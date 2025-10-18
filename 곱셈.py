a = int(input())
b = input()

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))

c = a * int(b[2])
d = a * int(b[1]) * 10
e = a * int(b[0]) * 100
print (c + d + e)