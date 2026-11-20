a, p = map(int, input().split())
arr = []
arr.append(a)
a = str(a)
flag = -1
cnt = 0

# 57 -> 74 (5^2 + 7^2) -> 65 (7^2 + 4^2) -> ...
# for t in range(20):
while True:
    sum = 0
    for i in a:
        temp_a = int(i)
        sum += temp_a ** p
    if sum not in arr:
        arr.append(sum)
    else:
        flag = sum
        break
    a = str(sum)

for i in arr:
    if i != flag:
        cnt += 1
    else:
        break

print(cnt)