#include <bits/stdc++.h>

using namespace std;

void solve() {
    int x;
    cin >> x;
    if(x % 25 == 0) {
        cout << x / 25 << '\n';
    } else {
        cout << (x / 25) + 1 << '\n';
    }
}

int main() {
    int t;
    cin >> t;

    while(t--) {
        solve();
    }
}