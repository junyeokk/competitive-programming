import sys
input = sys.stdin.readline

n, m, k = list(map(int, input().split()))
arr = []
res = 0
cnt = 0

arr = list(map(int, input().split()))
arr.sort()
print(arr)

# 가장 큰 수가 나오는 횟수를 계산
first = arr[n - 1]
second = arr[n - 2]

# ex, 8887 8887 88 이라고 치면
count = int(m / (k + 1)) * k # 8887 8887 -> 6개
count += m % (k + 1) # 88 -> 2개

res += first * count + second * (m - count)

print(res)