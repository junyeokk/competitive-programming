def solution(bandage, health, attacks):
    answer = 0
    max_h = health
    
    for i in range(len(attacks) - 1):
        at, ad = attacks[i][0], attacks[i][1]
        health -= ad
        if health <= 0:
            return -1
        cs = 0 # 연속 성공
        
        n_at = attacks[i + 1][0]
        t, x, y = bandage
        for j in range(at + 1, n_at):
            cs += 1
            health += x
            if t == cs:
                health += y
                cs = 0
            if max_h < health:
                health = max_h
        print(health)
    health -= attacks[len(attacks) - 1][1]
    
    if health <= 0:
        return -1
    
    return health