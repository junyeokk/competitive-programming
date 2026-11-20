#include <string>
#include <vector>

using namespace std;
typedef long long ll;

vector<int> solution(ll n) {
    vector<int> answer;
    
    while(n > 0) {
        int temp = n - (n / 10 * 10);
        answer.push_back(temp);
        n /= 10;
    }
    
    return answer;
}