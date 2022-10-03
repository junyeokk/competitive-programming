#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

const int MAX = 301;
int n;
int end_x, end_y;
int chess[MAX][MAX];
// 1시, 2시, 4시, 5시, 7시, 8시, 10시, 11시 방향
int dx[] = {1, 2, 2, 1, -1, -2, -2, -1};
int dy[] = {2, 1, -1, -2, -2, -1, 1, 2};

int BFS(int x, int y) {
	if(x == end_x && y == end_y) return 0;
	queue<pair<int, int>> q;
	q.push(make_pair(x, y));
	
	while(!q.empty()) {
		int cur_x = q.front().first;
		int cur_y = q.front().second;
		
		q.pop();
		
		for(int i = 0; i < 8; i++) {
			int nx = cur_x + dx[i];
			int ny = cur_y + dy[i];
			
			if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
			else if(chess[nx][ny] == 0) {
				chess[nx][ny] = chess[cur_x][cur_y] + 1;
				q.push(make_pair(nx, ny));
			}
			if(nx == end_x && ny == end_y) {
				return chess[end_x][end_y];
			}
		}
	}
	return -1;
}

int main() {
	int t, x, y;
	
	cin >> t;
	for(int i = 1; i <= t; i++) {
		memset(chess, 0, sizeof(chess));
		cin >> n;
		cin >> x >> y;
		cin >> end_x >> end_y;
		cout << BFS(x, y) << '\n';
	}
}