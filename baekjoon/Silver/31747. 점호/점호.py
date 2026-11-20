from collections import deque

n, k = map(int, input().split())

arr = list(map(int, input().split()))
ptr = 0
time = 0

q1 = deque()
q2 = deque()

while q1 or q2 or ptr < n:
    while len(q1) + len(q2) < k and ptr < n:
        if arr[ptr] == 1:
            q1.append(ptr)
        else:
            q2.append(ptr)
        ptr += 1

    if q1: q1.popleft()
    if q2: q2.popleft()
    time += 1

print(time)