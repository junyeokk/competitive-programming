n, b = input().split()

sum = 0

for i in range(len(n)):
    # print(len(n) - i)
    # print(ord(n[i]) - 55, len(n) - 1 - i)
    if n[i].isdigit():
        sum += int(n[i]) * pow(int(b), len(n) - 1 - i)
    else:
        sum += (ord(n[i]) - 55) * pow(int(b), len(n) - 1 - i)

print(sum)