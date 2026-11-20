#include <iostream>
#include <queue>

using namespace std;

const int MAX = 1001;
int n, m, elem, res = 0;
int dx[] = {-1, 1, 0, 0}; // 좌, 우, 상, 하
int dy[] = {0, 0, -1, 1};
queue<pair<int, int>> q;
int tomato[MAX][MAX];

void BFS() {
	while(!q.empty()) {
		// 큐의 현재 원소(익은 토마토)를 꺼낸다.
		int cur_x = q.front().first;
		int cur_y = q.front().second;
		
		q.pop();
		
		// 익은 토마토의 주변을 확인해서,
		for(int i = 0; i < 4; i++) {
			int nx = cur_x + dx[i];
			int ny = cur_y + dy[i];
			
			// 범위를 벗어나지 않고 익지 않은 토마토이면 큐에 추가 후 1 더함
			if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
			else if(tomato[nx][ny] == 0) {
				tomato[nx][ny] = tomato[cur_x][cur_y] + 1;
				q.push({nx, ny});
			}
			
		}
	}
}

int main() {
	int result = 0;
	cin >> n >> m;
	
	// 2차원 배열 초기화
	for(int i = 0; i < m; i++) {
		for(int j = 0; j < n; j++) {
			cin >> elem;
			tomato[j][i] = elem;
			// 익은 토마토는 큐에 추가
			if(tomato[j][i] == 1) {
				q.push({j, i});
			}
		}
	}
	
	BFS();
	
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			// 안 익은 토마토가 있으면 -1
			if(tomato[i][j] == 0) {
				cout << "-1" << '\n';
				return 0;
			}
			
			// 결과적으로 제일 큰 숫자를 담아야지 걸린 일수를 계산할 수 있음
			if(result < tomato[i][j]) {
				result = tomato[i][j];
			} 
		}
	}
	
	cout << result - 1 << '\n';
}