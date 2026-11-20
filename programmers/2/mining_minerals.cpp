#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ll;
vector<ll> v;

void solve() {
    sort(v.begin(), v.end());
    cout << v.front() << " " << v[(v.size() - 1) / 2] << " " << v.back();
}

void input() {
    int n;
    cin >> n;
    v.push_back(n);
}

int main() {
    int t;
    cin >> t;

    while(t--) {
        input();
    }
    solve();
}