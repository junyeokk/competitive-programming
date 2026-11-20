n = int(input())

print("int a;")
print("int *ptr = &a;")

for i in range(2, n + 1):
    prev = 'ptr' if i == 2 else f'ptr{i-1}'
    print(f"int {'*' * i}ptr{i} = &{prev};")