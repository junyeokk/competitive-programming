function solution(s) {
    let cnt = 0
    let sum = 0
    
    while(s !== '1') {
        s = s.split('');
        cnt += 1;
        sum += s.filter(c => c === '0').length;
        s = s.filter(c => c === '1').length.toString(2);
    }
    
    return [cnt, sum];
}