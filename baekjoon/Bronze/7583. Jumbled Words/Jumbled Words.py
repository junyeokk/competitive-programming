while(True):
    s = list(map(str, input().split()))
    arr = []
    
    if s[0] == '#':
        break
    
    for word in s:
        if(len(word) == 1):
            arr.append(word[0])
        else:
            arr.append(word[0] + word[1:-1][::-1] + word[-1])
    
    print(*arr)