n = int(input())

stk = []

for i in range(n):
    s = input()
    
    if "push" in s:
        q, x = s.split()
        stk.append(int(x))
    
    elif "pop" in s:
        if stk:
            print(stk.pop())
        else:
            print(-1)
    
    elif "size" in s:
        print(len(stk))
    
    elif "empty" in s:
        print(0 if stk else 1)
    
    elif "top" in s:
        if stk:
            print(stk[-1])
        else:
            print(-1)
    