from collections import Counter
n, k = map(int, input().split())
d = {}
res = []

items = list(map(str, input().split()))
item_count = Counter(items)
categories = list(map(str, input().split()))

for i in range(k):
    s = list(map(str, input().split())) # s[0]: category name, s[1]: count
    category = s[0]
    item_list = s[2:]
    d[category] = item_list

for c in categories:
    for item in d[c]:
        if item in item_count:
            for i in range(item_count[item]):
                res.append(item)        

print(*res)