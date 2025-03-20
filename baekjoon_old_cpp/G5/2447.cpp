#include <bits/stdc++.h>
#define INF 1000000000

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

// memset(memo, -1, size of memo);
// memset(arr, 0, sizeof arr);=

void blank(int i, int j, int n) {
    if (n == 1) {
        cout << "*";
    } else if ((i / (n / 3)) % 3 == 1 && (j / (n / 3)) % 3 == 1) {
        cout << " ";
    } else {
        blank(i, j, n / 3);
    }
}

void solve(int n) {
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            blank(i, j, n);
        }
        cout << '\n';
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    solve(n);
}