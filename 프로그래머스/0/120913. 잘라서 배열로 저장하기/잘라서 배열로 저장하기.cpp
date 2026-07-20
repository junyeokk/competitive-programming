#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> solution(string my_str, int n) {
    vector<string> answer;
    string s = "";
    for(int i = 1; i <= my_str.length(); i++) {
        s.append({my_str[i - 1]});
        if(i % n == 0) {
            answer.push_back({s});
            s = "";
        }
    }
    if(s != "") {
        answer.push_back({s});
    }
    return answer;
}