def solution(s):
    stk = []
    
    for ch in s:
        if ch == '(':
            stk.append(ch)
        else:
            if not stk:
                return False
            stk.pop()
    return len(stk) == 0