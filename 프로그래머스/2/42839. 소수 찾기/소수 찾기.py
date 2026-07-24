from itertools import permutations

INF = 9999999
is_prime = [True for _ in range(INF)]

def eratos():
    for i in range(2, INF):
        if is_prime[i]:
            for j in range(i * 2, INF, i):
                is_prime[j] = False

def solution(numbers):
    answer = 0
    nums = set()
    
    is_prime[0] = False
    is_prime[1] = False
    
    eratos()
    
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            nums.add(int(''.join(p)))
    
    for n in nums:
        if is_prime[n]:
            answer += 1
    
    return answer