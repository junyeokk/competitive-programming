def solution(tickets):
    passport = {}
    visited = {}
    
    for t in tickets:
        if t[0] in passport:
            passport[t[0]].append(t[1])
        else:
            passport[t[0]] = [t[1]]

    for key in passport:
        passport[key].sort()
        
    def dfs(ap, path):
        if len(path) == len(tickets) + 1:
            return path
        else:
            for i, dest in enumerate(passport.get(ap, [])):
                if not visited.get((ap, i), False):
                    visited[(ap, i)] = True
                    result = dfs(dest, path + [dest])
                    if result:
                        return result
                    visited[(ap, i)] = False
            return None
    return dfs("ICN", ["ICN"])