#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int x;

    while(n > 0) {
        int temp = n / 10 * 10;
        x = n - temp;
        n /= 10;
        answer += x;
    }
    
    return answer;
}