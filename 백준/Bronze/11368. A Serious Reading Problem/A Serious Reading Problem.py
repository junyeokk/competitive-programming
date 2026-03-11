while True:
    s = list(map(int, input().split()))
    if s[0] + s[1] + s[2] + s[3] == 0:
        break
    print(s[0] ** (s[1] * s[2] * s[3]))