//
// Created by Junhyeok CHAE on 2022/08/24.
//
#include <iostream>
#include <stack>

using namespace std;

int main() {
    string palindrome;
    stack<char> st;
    int count = 0;

    cin >> palindrome;
    for(int i = 0; i < palindrome.length(); i++) {
        if(palindrome[i] == '(') {
            st.push(palindrome[i]);
        } else {
            st.pop();
            if(palindrome[i - 1] == '(') {
                count += st.size();
            } else {
                count++;
            }
        }
    }
    cout << count;
}