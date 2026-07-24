#include <iostream>

using namespace std;
int solution(int n)
{
    int answer = 0;

    while(n > 0) {
        int x = 0;
        int temp = n / 10;
        temp *= 10;
        x = n - temp;
        answer += x;
        n /= 10;
    }
    
    return answer;
}