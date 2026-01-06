stack = []
match = {')': '(', '}': '{', ']': '['}

s = input()

for p in s:
    if p in '{([':
        stack.append(p)
    else:
        if not stack or stack[-1] != match[p]:
            print("NO")
            break
        stack.pop()
else: print("YES" if not stack else "NO")