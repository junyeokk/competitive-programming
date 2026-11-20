//
// Created by Junhyeok CHAE on 2022/08/24.
//
#include <iostream>

using namespace std;

// 규완이가 적어놓고 간 문자열
string s;

bool isPalindrome(int idx) {
    int half = (s.length() - idx) / 2;
    for(int i = 0; i < half; i++) {
        if(s[i + idx] != s[s.length() - 1 - i]) {
            return false;
        }
    }
    return true;
}

int main() {
    cin >> s;

    for(int check = 0; check < s.length(); check++) {
        if(isPalindrome(check)) {
            cout << check + s.length();
            return 0;
        }
    }
}