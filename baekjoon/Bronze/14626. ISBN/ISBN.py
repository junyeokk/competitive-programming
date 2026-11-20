s = list(input())

ls = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
idx = -1
sum = 0

for i in range(13):
    if s[i] in '1234567890':
        sum += ls[i] * int(s[i])
    else:
        idx = i

for d in range(10):
    if (sum + ls[idx] * d) % 10 == 0:
        print(d)
        break