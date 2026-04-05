s = input().lower()
s = ''.join(c for c in s if c.isalpha())


for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        print("Palindrome")
        break
    if i + 2 < len(s) and s[i] == s[i + 2]:
        print("Palindrome")
        break
else:
    print("Anti-palindrome")