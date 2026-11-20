n = int(input())

stack = []
log = []
cnt = 1

for i in range(n):
    t = int(input())
    
    if stack:
        if stack[-1] > t:
            log.clear()
            print("-_-")
            break
        
        elif stack[-1] == t:
            stack.pop()
            log.append("pop")
            continue
    
    while cnt <= t:
        stack.append(cnt)
        log.append("push")
        cnt += 1
        
    stack.pop()
    log.append("pop")

if log:
    for s in log:
        print(s)