#1
numbers = list(range(1, 31))

for _ in range(28):
    x = int(input())
    numbers.remove(x)
print(min(numbers))
print(max(numbers))


#2
student = [1] * 31
for i in range(28):
    x = int(input())
    student[x] = 0
for j in range(1, 31):
    if student[j] == 1:
        print(j)