#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll POW(ll a, ll b, ll m) {
    if(b == 1) return a % m; // 초기 조건
    ll val = POW(a, b / 2, m);
    val = val * val % m;
    if(b % 2 == 0) return val;// 짝수면 val 반환
    return val * a % m;// 홀수면 a 곱하고 반환
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll a, b, c;
    cin >> a >> b >> c;
    cout << POW(a, b, c);
}