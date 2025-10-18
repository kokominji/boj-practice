t = int(input())

for _ in range(t):
    a = input()
    score = 0
    count = 0
    for ch in a:
        if ch == "O":
            count += 1
            score += count
        else:
            count = 0
    print(score)