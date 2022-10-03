#include <iostream>
#include <vector>

using namespace std;

const int MAX = 101;
int n_cpt, n_pair, node1, node2, cnt = 0;
bool visited[MAX];
vector<int> graph[MAX];

void DFS(int node_num) {
	visited[node_num] = true;
	
	for(int i = 0; i < graph[node_num].size(); i++) {
		int next = graph[node_num][i];
		
		if(!visited[next]) {
			DFS(next);
			cnt++;
		}
	}
}

int main() {
	cin >> n_cpt >> n_pair;
	
	for(int i = 1; i <= n_pair; i++) {
		cin >> node1 >> node2;
		graph[node1].push_back(node2);
		graph[node2].push_back(node1);
	}
	
	DFS(1);
	
	cout << cnt << '\n';
}