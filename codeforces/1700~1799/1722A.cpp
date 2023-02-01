#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n;
    cin >> n;

    string name = "Timur";
    sort(name.begin(), name.end());

    string s;
    cin >> s;
    sort(s.begin(), s.end());
    cout << (name == s ? "YES" : "NO") << '\n';
}


int main() {
    int t;
    cin >> t;

    while(t--) {
        solve();
    }
}