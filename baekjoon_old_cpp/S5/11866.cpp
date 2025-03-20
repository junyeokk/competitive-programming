//
// Created by Junhyeok CHAE on 2022/08/24.
//
#include <iostream>
#include <queue>

using namespace std;

int main() {
    // N: 사람, K: K번째 있는 사람 제거
    int N, K;
    int count = 0, comma = 0;
    string str = "";
    cin >> N >> K;

    queue<int> q;
    for(int i = 1; i <= N; i++) {
        q.push(i);
    }

    cout << "<";
    while(q.size() > 1) {
        int temp = q.front();
        q.pop();
        if(count == K - 1) {
            cout << temp << ", ";
            count = 0;
        } else {
            count++;
            q.push(temp);
        }
    }

    cout << q.front() << ">";
}