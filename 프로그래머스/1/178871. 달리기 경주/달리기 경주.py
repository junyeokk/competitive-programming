def solution(players, callings):
    rank = {}
    for i, name in enumerate(players):
        rank[name] = i
    
    for c in callings:
        i = rank[c]
        f = players[i - 1]
        players[i - 1], players[i] = players[i], players[i - 1]
        rank[c] = i - 1
        rank[f] = i

    return players