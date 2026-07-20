import math

def solution(n):
    answer = 0
    sieve = [1] * (n + 1)
    sieve[0] = 0
    sieve[1] = 0
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    
    answer = sum(sieve)
    
    return answer