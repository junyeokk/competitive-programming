from collections import defaultdict

n = int(input())

for i in range(n):
    d = defaultdict(int)
    s = list(map(int, input().split()))
    
    for t in s:
        d[t] += 1
    
    c = sorted(d.values())

    if c == [1, 1, 1, 1, 1, 1]:
        print("single")
    elif c == [1, 1, 1, 1, 2]:
        print("one pair")
    elif c == [1, 1, 2, 2]:
        print("two pairs")
    elif c == [2, 2, 2]:
        print("three pairs")
    elif c == [1, 1, 1, 3]:
        print("one triple")
    elif c == [3, 3]:
        print("two triples")
    elif c == [1, 1, 4]:
        print("tiki")
    elif c == [2, 4]:
        print("tiki pair")
    elif c == [1, 2, 3]:
        print("full house")