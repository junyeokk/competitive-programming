s = list(input())

arr = [[1, 2], [3, 4]]

for i in range(len(s)):
    if s[i] == 'H':
        arr[0][0], arr[1][0] = arr[1][0], arr[0][0]
        arr[0][1], arr[1][1] = arr[1][1], arr[0][1]
    elif s[i] == 'V':
        arr[0][0], arr[0][1] = arr[0][1], arr[0][0]
        arr[1][0], arr[1][1] = arr[1][1], arr[1][0]
        
for row in arr:
    print(*row)