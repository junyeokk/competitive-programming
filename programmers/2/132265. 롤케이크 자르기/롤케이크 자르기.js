function solution(topping) {
    let cnt = 0
    
    let ob = new Set() // 형: Set
    let yb = new Map() // 동생: Map
    
    // 동생에게 모든 토핑 넣기
    for (let t of topping) {
        yb.set(t, (yb.get(t) || 0) + 1);
    }
    
    // 형에게 하나씩 옮기면서 비교
    for (let t of topping) {
        ob.add(t);
        yb.set(t, yb.get(t) - 1);
     
        if (yb.get(t) === 0) {
            yb.delete(t);
        }
        
        if (ob.size === yb.size) {
            cnt += 1
        }
    }
    
    return cnt;
}