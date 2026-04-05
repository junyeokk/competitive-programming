import heapq

n = int(input())

h = []
# heapq.heappush(h, x)
# heapq.heappop(h)
# heapq.heappushpop(h, x)
# h[0]

for i in range(n):
    s = list(map(int, input().split()))
    for x in s:
        heapq.heappush(h, x)
        if len(h) > n:
            heapq.heappop(h)

print(heapq.heappop(h))