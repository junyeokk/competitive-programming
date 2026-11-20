function solution(participant, completion) {
    const hashtable = {}
    
    for (const p of participant) {
        if (hashtable[p]) {
            hashtable[p]++
        } else {
            hashtable[p] = 1
        }
    }
    
    for (const c of completion) {
        hashtable[c]--
    }
    
    for (const key of participant) {
        if (hashtable[key] == 1) {
            return key
        }
    }
}