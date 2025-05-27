dice = list(map(int, input().split()))
a, b, c = dice[0], dice[1], dice[2]

if a==b==c:
    print(10000+(a*1000))
elif a==b or a==c:
    print(1000+(a*100))
elif b==c:
    print(1000+(b*100))
else:
    print(max(dice)*100)