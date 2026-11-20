#include <string>
#include <vector>

#define ARRAY_MAX 100001
#define MODULAR 1234567

using namespace std;

int memo[ARRAY_MAX];

int solution(int n) {
    int answer = 0;
    memo[0] = 0;
    memo[1] = 1;
    
    for(int i = 2; i < ARRAY_MAX; i++) {
        memo[i] = (memo[i - 1] % MODULAR + memo[i - 2] % MODULAR) % MODULAR;
    }
    answer = memo[n];
    return answer;
}