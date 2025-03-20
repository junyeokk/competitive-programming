#include <iostream>
#include <queue>

using namespace std;

const int MAX = 101;
int n, m, maze[MAX][MAX];
bool visited[MAX][MAX];
int cnt[MAX][MAX] = { 0 };
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
string s;
queue<pair<int, int>> q;

void BFS(int x, int y) {
	visited[x][y] = true;
	cnt[x][y]++;
	q.push({x, y});
	
	while(!q.empty()) {
		int cur_x = q.front().first;
		int cur_y = q.front().second;
		
		q.pop();
		
		for(int i = 0; i < 4; i++) {
			int nx = cur_x + dx[i];
			int ny = cur_y + dy[i];
			
			if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
          	// if can move and not visited
			else if(maze[nx][ny] == 1 && !visited[nx][ny]) {
              	// input 'current point + 1'
				cnt[nx][ny] = cnt[cur_x][cur_y] + 1;
                // and add 'next point'
				q.push({nx, ny});
                // modify 'next point''s status by 'true' in advance
				visited[nx][ny] = true;
			}
		}
	}
}

int main() {
	cin >> n >> m;
	
	for(int i = 0; i < n; i++) {
		cin >> s;
        // modify 'number' type which input 'string' type
		for(int j = 0; j < m; j++) {
			maze[i][j] = s[j] - '0';
		}
	}
	
  	// execute BFS function and initialize (0, 0)
	BFS(0, 0);
  
  	// The last element becomes the distance by the BFS function
	cout << cnt[n - 1][m - 1] << '\n';
}