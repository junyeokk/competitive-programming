#include <bits/stdc++.h>
#define INF 1000000000

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

// memset(memo, -1, size of memo);
// memset(arr, 0, sizeof arr);

int a[1000000], b[1000000], c[1000000];

void solve() {
    int n, m;
    int idx_a = 0, idx_b = 0;

    cin >> n >> m;

    for(int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for(int i = 0; i < m; i++) {
        cin >> b[i];
    }

    for(int i = 0; i < n + m; i++) {
        if(idx_b == m) c[i] = a[idx_a++]; // b 인덱스가 끝까지 갔으면 a 원소 삽입
        else if(idx_a == n) c[i] = b[idx_b++]; // a 인덱스가 끝까지 갔으면 b 원소 삽입
        else if(a[idx_a] <= b[idx_b]) c[i] = a[idx_a++]; // a 원소가 b 원소보다 작으면 a 원소 삽입
        else c[i] = b[idx_b++]; // b 원소가 a 원소보다 작으면 b 원소 삽입
    }

    for(int i = 0; i < n + m; i++) {
        cout << c[i] << ' ';
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
}