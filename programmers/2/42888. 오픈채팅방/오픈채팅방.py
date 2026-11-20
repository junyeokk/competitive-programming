def solution(record):
    answer = []
    userinfo = {} # key: uid, value: name
    
    # Phase 1: userinfo 구성 (이름 변경 반영하기 위함)
    for rc in record:
        # record 배열에서 원소 분리
        parts = rc.split() # 0: command, 1: uid, 2: name
        
        # 딕셔너리에 유저 정보 추가
        if parts[0] in ['Enter', 'Change']:
            userinfo[parts[1]] = parts[2]

    # Phase 2: 구성된 userinfo 출력
    for rc in record:
        # record 배열에서 원소 분리
        parts = rc.split() # 0: command, 1: uid, 2: name
        
        name = userinfo[parts[1]]
        
        if parts[0] == "Enter":
            answer.append(name + "님이 들어왔습니다.")
        elif parts[0] == "Leave":
            answer.append(name + "님이 나갔습니다.")
    
    return answer