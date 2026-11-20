#include <bits/stdc++.h>

using namespace std;

void solve() {
    vector<int> s(3);

    for(int i = 0; i < 3; i++) {
        cin >> s[i];
    }
    sort(s.begin(), s.end());
    if(s[0] + s[1] == s[2]) cout << "YES" << '\n';
    else cout << "NO" << '\n';
}

int main() {
    int t;
    cin >> t;

    while(t--) {
        solve();
    }
}