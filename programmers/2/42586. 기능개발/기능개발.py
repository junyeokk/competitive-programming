import math

def solution(progresses, speeds):
    answer = []
    bcnt = 1
    t = []
    idx = 0
    
    for i in range(len(progresses)):
        td = math.ceil((100 - progresses[i]) / speeds[i])
        t.append(td)
    
    deadline = t[0]
    for i in range(1, len(t)):
        if t[i] <= deadline:
            bcnt += 1
        else:
            answer.append(bcnt)
            bcnt = 1
            deadline = t[i]
    answer.append(bcnt)
    
    return answer