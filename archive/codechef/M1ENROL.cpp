#include <bits/stdc++.h>

using namespace std;

void solve() {
    int x, y;
    cin >> x >> y;

    if(y - x >= 0) {
        cout << y - x << '\n';
    } else {
        cout << 0 << '\n';
    }
}

int main() {
    int t;
    cin >> t;

    while(t--) {
        solve();
    }
}