n = int(input())
s = input()

if n <= 25:
    print(s)
else:
    center = s[11:n-11]
    flag = False
    for i in range(len(center) - 1):
        if center[i] == ".":
            flag = True
            break
    if flag:
        t = s[:9] + "......" + s[-10:] 
    else:
        t = s[:11] + "..." + s[-11:]
    print(t)