#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n, c, ans = 0;
    cin >> n >> c;

    vector<int> planet(n);
    map<int, int> m;

    for(int i = 0; i < n; i++) {
        cin >> planet[i];
        m[planet[i]]++;
        if(m[planet[i]] <= c) {
            ans++;
        }
    }
    cout << ans << '\n';
}

int main() {
    int t;
    cin >> t;

    while(t--) {
        solve();
    }
}