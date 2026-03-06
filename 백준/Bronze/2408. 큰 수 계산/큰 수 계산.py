n = int(input())

nArr = []
kArr = []
newNums = []
newOps = []

for i in range(n):
    t = int(input())
    nArr.append(t)
    if i < n - 1:
        k = input()
        kArr.append(k)

cur = nArr[0]
for i in range(len(kArr)):
    if kArr[i] == '*':
        cur = cur * nArr[i + 1]
    elif kArr[i] == '/':
        cur = cur // nArr[i + 1]
    else:
        newNums.append(cur)
        newOps.append(kArr[i])
        cur = nArr[i + 1]

newNums.append(cur)

res = newNums[0]
for i in range(len(newOps)):
    if newOps[i] == '+':
        res += newNums[i + 1]
    elif newOps[i] == '-':
        res -= newNums[i + 1]

print(res)