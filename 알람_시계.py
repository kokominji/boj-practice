H, M = map(int,input().split())


if (M  < 45):
    m = 60 - (45 - M)
    if (H == 0):
        h = 23
    else:
        h = H - 1
        
        
    print(h, m)
    
else:
    m = M - 45
    print(H, m)