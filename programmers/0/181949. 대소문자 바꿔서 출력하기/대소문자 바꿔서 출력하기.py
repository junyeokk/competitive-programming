str = input()
answer = []
for i in range(len(str)):
    answer.append(str[i].upper()) if str[i].islower() else answer.append(str[i].lower())

print(''.join(answer))