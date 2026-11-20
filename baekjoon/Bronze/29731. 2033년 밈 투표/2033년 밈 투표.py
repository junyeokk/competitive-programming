n = int(input())

s = ["Never gonna give you up", 
"Never gonna let you down", 
"Never gonna run around and desert you", 
"Never gonna make you cry",
"Never gonna say goodbye",
"Never gonna tell a lie and hurt you",
"Never gonna stop"]

flag = False

for i in range(n):
    t = input()
    if t not in s:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")