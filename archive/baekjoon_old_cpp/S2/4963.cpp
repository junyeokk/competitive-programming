#include <iostream>
#include <queue>

using namespace std;

const int MAX = 51;
int w, h, elem;
// 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
int dx[] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[] = {1, 1, 0, -1, -1, -1, 0, 1};
int island[MAX][MAX];

void BFS(bool visited[MAX][MAX], int x, int y) {
	// 인자로 온 x와 y를 큐에 추가
	queue<pair<int, int>> q;
	q.push(make_pair(x, y));
	visited[x][y] = true;
	
	while(!q.empty()) {
		// 큐의 현재 원소를 꺼냄
		int cur_x = q.front().first;
		int cur_y = q.front().second;
		
		q.pop();
		
		// 섬 주위를 확인해서 (대각선 포함)
		for(int i = 0; i < 8; i++) {
			int nx = cur_x + dx[i];
			int ny = cur_y + dy[i];
			
			// 범위를 벗어나지 않고 섬이라면 큐에 추가
			if(nx < 0 || nx >= w || ny < 0 || ny >= h) continue;
			else if (island[nx][ny] == 1 && !visited[nx][ny]) {
				q.push(make_pair(nx, ny));
				visited[nx][ny] = true;
			}
		}
	}
}

int main() {
	while(true) {
		bool visited[MAX][MAX] = { false };
		int cnt = 0;
		cin >> w >> h;
		
		if(w == 0 && h == 0) return 0;
		
		for(int y = 0; y < h; y++) {
			for(int x = 0; x < w; x++) {
				cin >> elem;
				island[x][y] = elem;
			}
		}
		
		for(int y = 0; y < h; y++) {
			for(int x = 0; x < w; x++) {
				if(island[x][y] == 1 && !visited[x][y]) {
					BFS(visited, x, y);
					cnt++;
				}
			}
		}
		
		cout << cnt << '\n';
	}
}