n, m = map(int, input().split())
selected = []

def func(start):
    if len(selected) == m:
        print(*selected)
        return
    for i in range(start, n + 1):
        selected.append(i)
        func(i + 1)
        selected.pop()

func(1)
