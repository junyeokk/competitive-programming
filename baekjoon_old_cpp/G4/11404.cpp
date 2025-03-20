#include <iostream>

using namespace std;

const int INF = 99999999;
const int MAX = 101;
int graph[MAX][MAX];

int main() {
	int node_num, vertex;
	
	cin >> node_num;
	cin >> vertex;
	
	// 최단거리 테이블을 모두 무한으로 초기화
	for(int i = 1; i <= MAX; i++) {
		for(int j = 1; j <= MAX; j++) {
			graph[i][j] = INF;
		}
	}
	
	// 자기 자신에서 자신으로 가는 비용은 0으로 초기화
	for(int a = 1; a <= node_num; a++) {
		for(int b = 1; b <= node_num; b++) {
			if(a == b) graph[a][b] = 0;
		}
	}
	
	// 각 간선에 대한 정보를 입력받아 그 값으로 초기화
	for(int i = 1; i <= vertex; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		// 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있음 -> 여러개라면 그 중 작은 값이 노선이 되어야 함
		if(!graph[a][b]) graph[a][b] = c;
		else graph[a][b] = min(graph[a][b], c);
	}
	
	// 플루이드 와샬 알고리즘
	for(int k = 1; k <= node_num; k++) {
		for(int i = 1; i <= node_num; i++) {
			for(int j = 1; j <= node_num; j++) {
				graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j]);
			}
		}
	}
	
	for(int i = 1; i <= node_num; i++) {
		for(int j = 1; j <= node_num; j++) {
			if(graph[i][j] == INF) {
				cout << 0 << " ";
			} else {
				cout << graph[i][j] << " ";	
			}
		}
		cout << '\n';
	}
}