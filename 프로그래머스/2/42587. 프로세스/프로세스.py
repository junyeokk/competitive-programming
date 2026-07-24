from collections import deque

def solution(priorities, location):
    dq = deque(enumerate(priorities))
    order = 0
    
    while dq:
        current = dq.popleft()

        if any(b > current[1] for a, b in dq):
            dq.append(current)
        else:
            order += 1
            if current[0] == location:
                return order