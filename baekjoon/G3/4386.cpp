#include <bits/stdc++.h>
#define INF 1000000000

using namespace std;

int parent[10001];
vector<pair<double, pair<double, double>>> node;
vector<pair<double, double>> crd;
double result = 0;

/**
 * parent 배열에서 찾을 노드의 그룹 번호를 반환해주는 함수
 * @param x 그룹 번호를 찾을 노드
 * @return
 */
int find(int x) {
    if (parent[x] != x) {
        return parent[x] = find(parent[x]);
    }
    return x;
}

/**
 * 그룹을 합치는 함수
 * @param a 그룹을 합칠 노드 1
 * @param b 그룹을 합칠 노드 2
 */
void merge(int a, int b) {
    int x = find(a);
    int y = find(b);
    parent[y] = x;
}

/**
 * 같은 그룹인지 아닌지 알아내는 함수
 * (그룹이 같은 상태에서 합치면 Cycle 우려가 있으므로 방지하기 위함)
 * @param a 같은 그룹인지 아닌지 알아낼 노드 1
 * @param b 같은 그룹인지 아닌지 알아낼 노드 2
 * @return
 */
bool is_same_parent(int a, int b) {
    int x = find(a);
    int y = find(b);
    if(x == y) return true;
    else return false;
}

/**
 * 노드 만드는 함수
 */
void make_node() {
    for(int i = 0; i < crd.size(); i++) {
        for(int j = i + 1; j < crd.size(); j++) {
            double cost = sqrt(pow(crd[i].first - crd[j].first, 2) + pow(crd[i].second - crd[j].second, 2));
            node.push_back({cost, {i, j}});
        }
    }
    sort(node.begin(), node.end());
}

/**
 * MST 가중치 계산
 */
void calc_mst() {
    for(int i = 1; i <= crd.size(); i++) {
        parent[i] = i;
    }

    for(int i = 0; i < node.size(); i++) {
        if(!is_same_parent(node[i].second.first, node[i].second.second)) {
            merge(node[i].second.first, node[i].second.second);
            result += node[i].first;
        }
    }
}

/**
 * 입력값을 받는 함수
 */
void input() {
    int n;
    double x, y;
    cin >> n;

    for(int i = 0; i < n; i++) {
        cin >> x >> y;
        crd.push_back({x, y});
    }
}

void solve() {
    input();
    make_node();
    calc_mst();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();

    cout.precision(3);
    cout << result << '\n';
}