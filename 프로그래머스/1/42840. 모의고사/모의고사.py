def solution(answers):
    res = []
    
    zzikki = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    score = [0] * 3
    
    for i in range(0, 3):
        idx = 0
        for answer in answers:
            if answer == zzikki[i][idx % len(zzikki[i])]:
                score[i] += 1
            idx += 1

    for i in range(0, 3):
        if max(score) == score[i]:
            res.append(i + 1)

    return res