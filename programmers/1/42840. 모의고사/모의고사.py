def solution(answers):
    res = []
    
    # 수포자들 패턴
    zzikki = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # 점수 저장할 리스트
    score = [0] * 3
    
    # 각 수포자들의 패턴과 정답이 얼마나 일치하는지 확인
    for i in range(0, 3):
        idx = 0
        for answer in answers:
            if answer == zzikki[i][idx % len(zzikki[i])]:
                score[i] += 1
            idx += 1

    # 가장 높은 점수를 가진 수포자들의 번호를 찾아서 리스트에 담음
    for i in range(0, 3):
        if max(score) == score[i]:
            res.append(i + 1)

    return res