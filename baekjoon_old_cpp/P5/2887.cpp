#include <bits/stdc++.h>
#define INF 1000000000

using namespace std;

int parent[100001];
vector<pair<int, int>> vec_x;
vector<pair<int, int>> vec_y;
vector<pair<int, int>> vec_z;
vector<pair<int, pair<int, int>>> node;
int n;
int result = 0;

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

/* 시간 초과
vector<tuple<int, int, int>> crd;

void make_node_legacy() {
    for(int i = 0; i < crd.size(); i++) {
        for(int j = i + 1; j < crd.size(); j++) {
            int cost = min({abs(get<0>(crd[i]) - get<0>(crd[j])), abs(get<1>(crd[i]) - get<1>(crd[j])), abs(get<2>(crd[i]) - get<2>(crd[j]))});
            node.push_back({cost, {i, j}});
        }
    }
}
*/

/**
 * 노드 만드는 함수
 */
void make_node() {

    sort(vec_x.begin(), vec_x.end());
    sort(vec_y.begin(), vec_y.end());
    sort(vec_z.begin(), vec_z.end());

    for(int i = 0; i < n - 1; i++) {
        node.push_back({vec_x[i + 1].first - vec_x[i].first, {vec_x[i].second, vec_x[i + 1].second}});
        node.push_back({vec_y[i + 1].first - vec_y[i].first, {vec_y[i].second, vec_y[i + 1].second}});
        node.push_back({vec_z[i + 1].first - vec_z[i].first, {vec_z[i].second, vec_z[i + 1].second}});
    }

    sort(node.begin(), node.end());
}

/**
 * MST 가중치 계산
 */
void calc_mst() {
    for(int i = 1; i <= n ; i++) {
        parent[i] = i;
    }

    for(int i = 0; i < node.size(); i++) {
        if(!is_same_parent(node[i].second.first, node[i].second.second)) {
            merge(node[i].second.first, node[i].second.second);
            result += node[i].first;
        }
    }
}

void input() {
    int x, y, z;
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> x >> y >> z;
        vec_x.push_back({x, i});
        vec_y.push_back({y, i});
        vec_z.push_back({z, i});
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

    cout << result << '\n';
}