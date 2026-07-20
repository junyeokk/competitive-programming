from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    
    emoticon_plus_users = 0
    emoticon_price = 0
    
    n = len(emoticons)
    discounts = [10, 20, 30, 40]    
    for p in product(discounts, repeat=n):
        for u in users:
            total = 0
            for i in range(n):
                if u[0] <= p[i]:
                    total += emoticons[i] * (100 - p[i]) / 100
            if total >= u[1]:
                emoticon_plus_users += 1
            else:
                emoticon_price += total
        if answer[0] < emoticon_plus_users:
            answer[0] = emoticon_plus_users
            answer[1] = emoticon_price
        elif answer[0] == emoticon_plus_users:
            if answer[1] < emoticon_price:
                answer[1] = emoticon_price
        emoticon_plus_users = 0
        emoticon_price = 0
    return answer