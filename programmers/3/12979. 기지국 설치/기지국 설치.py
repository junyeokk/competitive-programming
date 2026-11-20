def solution(n, stations, w):
    answer = 0
    coverage = 2 * w + 1

    # Phase 1: [1번 아파트 옥상]부터 [마지막 기지국 커버리지 옥상]까지
    start = 1
    
    for station in stations:
        left, right = station - w, station + w
        
        # 현재 기지국의 왼쪽 범위 바깥에 전파가 미치지 않는 구간이 있다면,
        # 그 구간의 길이를 계산하고 필요한 추가 기지국의 수를 구함
        if start < left: 
            length = left - start
            answer += (length + coverage - 1) // coverage # 필요한 기지국 수 계산 식
        
        # start 초기화
        start = right + 1
    
    # Phase 2: [마지막 기지국 커버리지 옥상]이 커버하지 못 하는 곳이 있다면 추가
    # start가 위에 있는 for문에서 초기화 되므로 바로 n과 비교해도 됨
    if start <= n:
        length = n - start + 1
        answer += (length + coverage - 1) // coverage
    
    return answer
