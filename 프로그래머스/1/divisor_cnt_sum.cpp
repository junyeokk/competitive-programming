#include <string>
#include <vector>

using namespace std;

int cnt_div(int n) {
    int cnt = 0;
    for(int i = 1; i <= n; i++) {
        if(n % i == 0) cnt++;
    }
    return cnt;
}

int is_cnt_even(int n) {
    if(cnt_div(n) % 2 == 0) return 1;
    else return -1;
}

int solution(int left, int right) {
    int answer = 0;
    for(int i = left; i <= right; i++) {
        answer += is_cnt_even(i) * i;
    }
    return answer;
}