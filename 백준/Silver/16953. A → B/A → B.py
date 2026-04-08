a, b = map(int, input().split())

cnt = 0
while True:
    if a == b:
        print(cnt + 1)
        break
    
    if a > b:
        print(-1)
        break

    if b % 2 == 0:
        b //= 2    
    elif b % 10 == 1:
        b //= 10
    else:
        print(-1)
        break

    cnt += 1