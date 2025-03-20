#include <bits/stdc++.h>
#define INF 1000000000

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

// memset(memo, -1, size of memo);
// memset(arr, 0, sizeof arr);

int t;
int freq[2000001];

void solve() {
    for(int i = 0; i < t; i++) {
        int a;
        cin >> a;
        freq[a + 1000000]++;
    }
    for(int i = 0; i <= 2000000; i++) {
        while(freq[i]--) {
            cout << i - 1000000 << '\n';
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> t;

    solve();
}