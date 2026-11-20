from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    dq = deque([0] * bridge_length)
    cur_weight = 0
    truck_weights = deque(truck_weights)
    
    while cur_weight > 0 or truck_weights:
        answer += 1
        cur_weight -= dq.popleft()
        
        if truck_weights and cur_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            cur_weight += truck
            dq.append(truck)
        else:
            dq.append(0)
    
    return answer