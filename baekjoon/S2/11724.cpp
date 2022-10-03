#include <iostream>
#include <vector>

using namespace std;

const int MAX = 1001;
bool visited[MAX];
vector<int> tree[MAX];

void DFS(int node_num) {
	visited[node_num] = true;
	
	for(int i = 0; i < tree[node_num].size(); i++) {
		int next = tree[node_num][i];
		
		if(!visited[next]) {
			DFS(next);
		}
	}
}

int main() {
	int n, m, cnt = 0, node1, node2;
	
	cin >> n >> m;

	for(int i = 1; i <= m; i++) {
		cin >> node1 >> node2;
		tree[node1].push_back(node2);
		tree[node2].push_back(node1);
	}
	
	for(int i = 1; i <= n; i++) {
		if(!visited[i]) {
			DFS(i);
			cnt++;
		}
	}
	
	cout << cnt << '\n';
}

