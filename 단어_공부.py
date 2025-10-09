# 하나씩 순회하면서 같은 문자열을 카운트
# 거기서 max값인 문자열을 upper로 반환
world = str(input())
count = 0

for i in world:
    if (i == world):
        count += 1
    print(max(count))
        