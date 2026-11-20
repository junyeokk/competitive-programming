n = int(input())

arr = list(map(int, input().split()))

s = set(arr)
arr = list(s)
arr.sort(reverse = True)

print(*arr)