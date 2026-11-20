import sys
sys.setrecursionlimit(10 ** 7 + 7)

def solution(n, costs):
    answer = 0
    
    p = list(range(n + 1))
    costs.sort(key=lambda x:x[2])

    def find(x):
        if x != p[x]:
            p[x] = find(p[x])
        return p[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        p[rx] = ry
    
    for a, b, w in costs:
        if find(a) != find(b):
            union(a, b)
            answer += w
    
    return answer