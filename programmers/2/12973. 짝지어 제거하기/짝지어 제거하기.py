def solution(s):
    stk = []
    for ch in s:
        if stk and stk[-1] == ch:
            stk.pop()
        else:
            stk.append(ch)
    
    if not stk:
        return 1
    else:
        return 0