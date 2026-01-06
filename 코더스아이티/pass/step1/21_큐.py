from collections import deque

n = int(input())
q = deque()

for i in range(n):
    s = input()
    if "push" in s:
        _, v = s.split()
        q.append(int(v))
        
    elif "pop" in s:
        if q:
            print(q.popleft())
        else:
            print(-1)
        
    elif "size" in s:
        print(len(q))
        
    elif "empty" in s:
        print(0 if q else 1)
        
    elif "front" in s:
        if q:
            print(q[0])
        else:
            print(-1)
            
    elif "back" in s:
        if q:
            print(q[-1])
        else:
            print(-1)