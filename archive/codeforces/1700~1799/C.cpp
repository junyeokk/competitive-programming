#include <bits/stdc++.h>

using namespace std;

char world[8][8] = { ".", };
bool found_line = false;

void find_line(int x, int y) {
    char flag = world[x][y];
    bool is_upon = true;
    for(int i = 0; i < 8; i++) {
        if (flag != world[i][y]) is_upon = false;
    }
    if(is_upon) {
        cout << flag << '\n';
        found_line = true;
        return;
    }

    is_upon = true;
    for(int i = 0; i < 8; i++) {
        if (flag != world[x][i]) is_upon = false;
    }
    if(is_upon) {
        cout << flag << '\n';
        found_line = true;
        return;
    }
}

void solve() {
    found_line = false;
    string s;
    for(int i = 0; i < 8; i++) {
        cin >> s;
        for(int j = 0; j < 8; j++) {
            world[i][j] = s[j];
        }
    }

    for(int i = 0; i < 8; i++) {
        for(int j = 0; j < 8; j++) {
            if(world[i][j] != '.') {
                find_line(i, j);
                if(found_line) return;
            }
        }
    }
}

int main() {
    int t;
    cin >> t;

    while(t--) {
        solve();
    }
}