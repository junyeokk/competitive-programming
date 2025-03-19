import sys
input = sys.stdin.readline

n, m, k = list(map(int, input().split()))
arr = []
res = 0
cnt = 0

arr = list(map(int, input().split()))
arr.sort()
print(arr)

for i in range(m):
  if cnt != k :
    res += arr[len(arr) - 1]
    cnt += 1
  else:
    res += arr[len(arr) - 2]
    cnt = 0

print(res)