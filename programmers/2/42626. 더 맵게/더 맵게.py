import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    if scoville[0] >= K:
        return 0
    
    while len(scoville) > 1:
        l1, l2 = heapq.heappop(scoville), heapq.heappop(scoville)
        t = l1 + l2 * 2
        heapq.heappush(scoville, t)
        answer += 1
        if scoville[0] >= K:
            return answer

    answer = -1
    return answer