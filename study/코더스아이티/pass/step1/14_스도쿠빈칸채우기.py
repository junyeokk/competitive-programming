t = '123456789'

for i in range(9):
    s = input()
    if '?' in s:
        for c in t:
            if c not in s:
                print(c)