today = list(map(int, input().split()))
dday = list(map(int, input().split()))
totday = 0

def monthday(y, m):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30

    if m == 2 and isyoonnyun(y):
        return 29
    elif m == 2 and not isyoonnyun(y):
        return 28

def isyoonnyun(y):
    yoonnyunflag = False
    if y % 4 == 0:
        yoonnyunflag = True
    if y % 100 == 0:
        yoonnyunflag = False
    if y % 400 == 0:
        yoonnyunflag = True
    return yoonnyunflag

temptoday = [today[0] + 1000, today[1], today[2]]
if dday >= temptoday:
    print("gg")
    exit()

while today != dday:
    totday += 1
    
    # [0]: year, [1]: month, [2]: day
    if today[2] == monthday(today[0], today[1]):
        today[2] = 1
        if today[1] == 12:
            today[0] += 1
            today[1] = 1
        else:
            today[1] += 1
    else: 
        today[2] += 1

print(f'D-{totday}')