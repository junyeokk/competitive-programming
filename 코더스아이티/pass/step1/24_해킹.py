stack = []
stack_t = []

s = input()

for t in s:
    if t == '<':
        if stack:
            stack_t.append(stack.pop())
    elif t == '>':
        if stack_t:
            stack.append(stack_t.pop())
    elif t == '-':
        if stack:
            stack.pop()
    else:
        stack.append(t)
        
while stack_t:
    stack.append(stack_t.pop())

for s in stack:
    print(s, end = '')