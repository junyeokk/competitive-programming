def solution(sequence, k):
    answer = []
    
    i, j = 0, 0
    csum = 0
    bw = 999999999 # best window size
    
    while i < len(sequence):
        csum += sequence[i]
        
        while csum > k:
            csum -= sequence[j]
            j += 1
        
        wsize = i - j + 1
        
        if csum == k and wsize < bw:
            answer = []
            answer.append(j)
            answer.append(i)
            bw = wsize
        
        i += 1
    
    return answer