arr = [False for _ in range(101)]

n = int(input())

for i in range(n):
    temp = int(input())
    arr[temp] = True

for i in range(1, 101):
    if arr[i] == False:
        print(i)
    