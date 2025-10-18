x, y, w, h = map(int,input().split())

W = w - x
H = h - y

print (min(x, y, W, H))
