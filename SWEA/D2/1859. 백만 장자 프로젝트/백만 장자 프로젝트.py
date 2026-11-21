def solve(tc):
    profit = 0
    n = int(input())
    prices = list(map(int, input().split()))

    max_price = 0
    profit = 0

    for p in reversed(prices):
        if p > max_price:
            max_price = p
        else: 
            profit += max_price - p
    print(f"#{tc} {profit}")

T = int(input())
for i in range(T):
    solve(i + 1)