mirror = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p', 'i': 'i', 'o': 'o', 'v': 'v', 'w': 'w', 'x': 'x'}

while True:
    s = input()
    if s == '#':
        break
    tstr = []
    flag = True
    for i in range(0, len(s)):
        val = s[len(s) - i - 1]
        if val in mirror:
            tstr.append(mirror[val])
        else:
            flag = False
    
    if flag:
        print(''.join(tstr))
    else:
        print("INVALID")
