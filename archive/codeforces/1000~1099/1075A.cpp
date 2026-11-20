#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

void solve() {
    ll n, x, y;
    cin >> n;
    cin >> x >> y;

    ll white_dis = max(x - 1, y - 1);
    ll black_dis = max(n - x, n - y);

    if (white_dis > black_dis) cout << "Black";
    else cout << "White";
}

int main() {
    solve();
}