#include <iostream>
#include <climits>
#include <vector>
#include <queue>

using namespace std;

const int MAX = 100001;
const int INF = INT_MAX;

// 노드의 개수 (n), 간선의 개수 (m), 시작 노드 번호 (start)
// 노드의 개수는 최대 100,000개라고 가정
int n, m, start;

// 각 노드에 연결되어 있는 노드에 대한 정보를 담는 배열
vector<pair<int, int>> graph[MAX];

// 최단거리 테이블 만들기
int d[MAX];

void dijkstra(int start) {
	priority_queue<pair<int, int>> pq;
	
	// 시작 노드로 가기 위한 최단경로는 0으로 설정하여, 큐에 삽입
	pq.push(make_pair(0, start));
	
	d[start] = 0;
	
	while(!pq.empty()) { // 큐가 비어있지 않다면
		// 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
		int dist = -pq.top().first; // 현재 노드까지의 비용
		int now = pq.top().second; // 현재 노드
		pq.pop();
		
		// 현재 노드가 이미 처리된 적이 있으면 무시
		if(d[now] < dist) continue;
		
		// 현재 노드와 연결된 인접한 노드들을 확인
		for(int i = 0; i < graph[now].size(); i++) {
			int cost = dist + graph[now][i].second;
			// 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
			if(cost < d[graph[now][i].first]) {
				// 비용 갱신
				d[graph[now][i].first] = cost;
				pq.push(make_pair(-cost, graph[now][i].first));
			}
		}
	}
}

int main() {
	cin >> n >> m >> start;
	
	// 모든 간선 정보 입력받기
	for(int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		
		// a번 노드에서 b번 노드로 가는 비용이 c
		graph[a].push_back(make_pair(b, c));
	}
	// 최단거리 테이블을 무한으로 초기화
	fill(d, d + MAX, INF);
	
	// 다익스트라 알고리즘 수행
	dijkstra(start);
	
	// 모든 노드로 가기 위한 최단 거리 출력
	for(int i = 1; i <= n; i++) {
		// 도달할 수 없는 경우, 무한으로 출력
		if(d[i] == INF) {
			cout << "INF" << '\n';
		}
		// 도달할 수 있는 경우 최단거리 출력
		else {
			cout << d[i] << '\n';
		}
	}
}