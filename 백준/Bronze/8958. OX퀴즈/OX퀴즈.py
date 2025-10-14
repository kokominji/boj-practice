# 만약 O라면 count 누적,socre에 더하기 
# X면 count 초기화 
t = int(input())

for i in range(t):
    result = input()
    score = 0
    count = 0
    for a in result:
        if (a == "O"):
            count += 1
            score += count
        else:
            count = 0
    print(score)
             