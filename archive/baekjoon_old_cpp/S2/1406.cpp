#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string init;
    cin >> init;
    list<char> L;
    for (auto c : init) {
        L.push_back(c);
    }
    auto cursor = L.end();
    int q;
    cin >> q;
    while (q--) {
        char op;
        cin >> op;
        if (op == 'P') { // P $: $라는 문자를 커서 왼쪽에 추가
            char add;
            cin >> add;
            L.insert(cursor, add);
        } else if (op == 'L') { // 커서를 왼쪽으로 한 칸 옮김 (맨 앞이면 무시)
            if(cursor != L.begin()) cursor--;
        } else if (op == 'D') { // 커서를 오른쪽으로 한 칸 옮김 (맨 뒤면 무시)
            if(cursor != L.end()) cursor++;
        } else { // 커서 왼쪽에 있는 문자를 삭제함 (맨 앞이면 무시)
            if(cursor != L.begin()) {
                cursor--;
                cursor = L.erase(cursor);
            }
        }
    }
    for (auto c : L) cout << c;
}