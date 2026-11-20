def solution(word):
    cnt = [0]
    
    def dfs(prefix):
        cnt[0] += 1
        if prefix == word:
            return True
        if len(prefix) == 5:
            return False
        for ch in 'AEIOU':
            if dfs(prefix + ch):
                return True
        return False
    
    dfs('')
    return cnt[0] - 1