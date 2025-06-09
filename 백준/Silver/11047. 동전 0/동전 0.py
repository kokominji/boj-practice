n, k = map(int, input().split())

coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)
    
coins.sort(reverse=True)

answer = 0
for coin in coins:
    if k >= coin:
        answer += k // coin
        k %= coin
        if k == 0:
            break
print(answer)