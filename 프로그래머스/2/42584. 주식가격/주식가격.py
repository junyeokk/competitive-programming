def solution(prices):
    answer = [0] * len(prices)
    
    stk = []
    for i, p in enumerate(prices):
        while stk and prices[stk[-1]] > p:
            idx = stk.pop()
            answer[idx] = i - idx
        stk.append(i)

    for idx in stk:
        answer[idx] = (len(prices) - 1) - idx
    
    return answer