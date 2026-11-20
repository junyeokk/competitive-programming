#include <iostream>
#include <queue>

using namespace std;

int t, n, m, k;
const int MAX = 51;
int dx[] = {-1, 1, 0, 0}; // 좌, 우, 상, 하
int dy[] = {0, 0, -1, 1};

void BFS(int cabbage[MAX][MAX], int y, int x) {
	queue<pair<int, int>> q;
	q.push(make_pair(y, x));
	
	while(!q.empty()) {
		int cur_x = q.front().first;
		int cur_y = q.front().second;
		
		q.pop();
		
		for(int i = 0; i < 4; i++) {
			int nx = cur_x + dx[i];
			int ny = cur_y + dy[i];
			
			if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
			if(cabbage[nx][ny] == 0) continue;
			if(cabbage[nx][ny] == 1) {
				cabbage[nx][ny] = 0;
				q.push(make_pair(nx, ny));
			}
		}
	}
}

int main() {
	int cab_x, cab_y;
	
	cin >> t;
	
	for(int i = 1; i <= t; i++) {
		cin >> n >> m >> k;
		int cabbage[MAX][MAX] = { 0 };
		int cnt = 0;
		
		for(int j = 0; j < k; j++) {
			cin >> cab_x >> cab_y;
			cabbage[cab_x][cab_y] = 1;
		}
		
		for(int x = 0; x < m; x++) {
			for(int y = 0; y < n; y++) {
				if(cabbage[y][x] == 0) continue;
				else {
					BFS(cabbage, y, x);
					cnt++;
				}
			}
		}
		
		cout << cnt << '\n';
	}
}