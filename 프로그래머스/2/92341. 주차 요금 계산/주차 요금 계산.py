from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    
    intime = {}
    tottime = defaultdict(int)
    
    for r in records:
        time, car, action = r.split(" ")
        hh, mm = time.split(":")
        t = int(hh) * 60 + int(mm)
        
        # 제 시간에 출차
        if action == "IN":
            intime[car] = t
        elif action == "OUT":
            tottime[car] += t - intime[car]
            del intime[car]
    
    # 제 시간에 출차 안 한 차들
    for ic in intime:
        tottime[ic] += 1439 - intime[ic] # 1439 <- 23:59를 분으로 치환
    
    cars = sorted(tottime.keys())
    for t in cars:
        print(tottime[t])
        if tottime[t] < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((tottime[t] - fees[0]) / fees[2]) * fees[3])
    
    return answer