s = input()
a = [-1] * 26
for num, char in enumerate(s):
    if a[ord(char) - ord('a')] == -1:
        a[ord(char) - ord('a')] = num

print(*a)