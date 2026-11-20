def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        s = ""
        for character in skill_tree:
            if character in skill:
                s += character
        
        if skill[:len(s)] == s:
            answer += 1
    
    return answer