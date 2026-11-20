n = int(input())

queens = []
count = 0

def is_safe(row, col):
    for r in range(row):
        c = queens[r]
        if col == c:
            return False
        if abs(row - r) == abs(col - c):
            return False
    return True


def solve(row):
    global count
    if row == n:
        count += 1
        return
    for col in range(n):
        if is_safe(row, col):
            queens.append(col)
            solve(row + 1)
            queens.pop()

solve(0)
print(count)