import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

t = int(input())

def solve():
    count = defaultdict(int)
    mih = [] # min_heap
    mah = [] # max_heap
    total = 0

    k = int(input())

    for i in range(k):
        q, v = input().split()
        v = int(v)
        if q == 'I':
            heapq.heappush(mih, v)
            heapq.heappush(mah, -v)
            count[v] += 1
            total += 1
        elif q == 'D':
            if total == 0:
                continue
            if v == 1: # 최댓값
                while mah and count[-mah[0]] == 0:
                    heapq.heappop(mah)
                if mah:
                    val = -heapq.heappop(mah)
                    count[val] -= 1
                    total -= 1
            elif v == -1: # 최솟값
                while mih and count[mih[0]] == 0:
                    heapq.heappop(mih)
                if mih:
                    val = heapq.heappop(mih)
                    count[val] -= 1
                    total -= 1
    
    while mih and count[mih[0]] == 0:
        heapq.heappop(mih)
    while mah and count[-mah[0]] == 0:
        heapq.heappop(mah)
    
    if not mih or not mah:
        print("EMPTY")
    else:
        print(-mah[0], mih[0])


for i in range(t):
    solve()