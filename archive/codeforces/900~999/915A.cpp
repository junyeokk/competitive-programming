#include <bits/stdc++.h>

using namespace std;

void solve() {
    int n, k, an, min_quo;
    cin >> n >> k;
    vector<int> vi;

    for(int i = 0; i < n; i++) {
        cin >> an;
        if(k % an == 0) {
            min_quo = min(k / an, min_quo);
        }
    }
    cout << min_quo;
}

int main() {
    solve();
}