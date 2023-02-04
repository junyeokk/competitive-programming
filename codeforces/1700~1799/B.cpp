#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> s(n);

    for(int i = 0; i < n; i++) {
        cin >> s[i];
    }
    sort(s.begin(), s.end());
    for(int i = 0; i < n - 1; i++) {
        if(s[i] >= s[i + 1]) {
            cout << "NO" << '\n';
            return;
        }
    }
    cout << "YES" << '\n';
}

int main() {
    int t;
    cin >> t;

    while(t--) {
        solve();
    }
}