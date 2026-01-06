t = int(input())

for v in range(t):
    coffee = []
    price = []
    
    n, m, k = map(int, input().split())
    sum = 0
    
    for i in range(n):
        coffee.append(int(input()))
    
    for j in range(m):
        price.append(int(input()))
    
    for i in range(n):
        sum += price[coffee[i] - 1]
    
    if sum <= k:
        print("Y")
    else: 
        print("N")