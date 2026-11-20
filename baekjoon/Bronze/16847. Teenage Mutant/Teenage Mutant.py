t = int(input())
idx = 1

def solve():
    global idx
    n, k = map(int, input().split())
    ancestor = input()
    cnt = 0
    mutant = [1 for i in range(k)]
    
    for i in range(n):
        s = input()
        for j in range(len(s)):
            if mutant[j] == 1 and ancestor[j] == s[j]:
                mutant[j] = 0
                cnt += 1
        
    print(f'Data Set {idx}:\n{k - cnt}/{k}\n')
    idx += 1

for _ in range(t):
    solve()