n = int(input())
max_k = 0
animals = []

for i in range(n):
    l = input().split()
    name = l[0]
    k = int(l[1])
    traits = l[2:]
    animals.append(traits)

res = 0
for i in range(n):
    k = len(animals[i])
    b = 0
    for j in range(n):
        if i == j:
            continue
        com = len(set(animals[i]) & set(animals[j]))
        b = max(b, com + 1)
    res = max(res, min(k, b))

print(res)