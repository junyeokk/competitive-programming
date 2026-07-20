function solution(s) {
    let answer = 0
    
    for (let i = 0; i < s.length; i++) {
        const stk = []
        let isValid = true
        
        for (let j = 0; j < s.length; j++) {
            let target = s[(i + j) % s.length]  
            if (target === '[' || target === '(' || target === '{') {
                stk.push(target);
            } else {
                if (stk.length === 0) {
                    isValid = false;
                    break;
                }
                
                let top = stk[stk.length - 1]
                if ((target === ']' && top === '[') ||
                   (target === ')' && top === '(') || 
                   (target === '}' && top === '{')) {
                    stk.pop()
                } else {
                    isValid = false
                    break
                }
            }
        }
        
        if (isValid && stk.length === 0) {
            answer += 1
        }
    }
    
    
    return answer;
}