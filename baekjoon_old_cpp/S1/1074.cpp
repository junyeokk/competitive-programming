#include <bits/stdc++.h>

using namespace std;

int func(int n, int r, int c) {
    if(n == 0) return 0;
    int half = 1 << (n - 1);
    if(r < half && c < half) return func(n - 1, r, c); // 0번
    if(r < half && c >= half) return half * half + func(n - 1, r, c - half); // 1번
    if(r >= half && c < half) return 2 * half * half + func(n - 1, r - half, c); // 2번
    return 3 * half * half + func(n - 1, r - half, c - half); // 3번
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, r, c;
    cin >> n >> r >> c;
    cout << func(n, r, c);
}