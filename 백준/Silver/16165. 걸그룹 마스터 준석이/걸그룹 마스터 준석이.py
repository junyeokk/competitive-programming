n, m = map(int, input().split())

dict0 = {}
dict1 = {}

# 초기화
for i in range(n):
    tn = input()
    cnt = int(input())
    dict0[tn] = []
    for j in range(cnt):
        member = input()
        dict0[tn].append(member)
        dict1[member] = tn

# 퀴즈
for i in range(m):
    q1 = input()
    q2 = int(input())
    
    if q2 == 0:
        tmp = sorted(dict0[q1])
        for t in tmp:
            print(t)
    else:
        print(dict1[q1])