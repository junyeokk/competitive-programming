def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ': 
            continue
        base = ord('A') if s[i].isupper() else ord('a') # ord
        s[i] = chr((ord(s[i]) - base + n) % 26 + base)   # chr
    return ''.join(s)