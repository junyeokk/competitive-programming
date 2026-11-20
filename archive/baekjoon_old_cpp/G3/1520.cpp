#include <iostream>

using namespace std;

const int MAX = 501;
int n, m;
int downhill[MAX][MAX];
int dp[MAX][MAX];

int dx[] = {-1, 1, 0, 0}; // 좌, 우, 상, 하
int dy[] = {0 , 0, -1, 1};

int DFS(int x, int y) {
	if(x == n - 1 && y == m - 1) return 1;
	if(dp[x][y] != -1) return dp[x][y];
	
	dp[x][y] = 0;
	for(int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		
		if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
		if(downhill[nx][ny] < downhill[x][y]) {
			dp[x][y] = dp[x][y] + DFS(nx, ny);
		}
	}
	return dp[x][y];
}

int main() {
	int elem;
	cin >> n >> m;
	
	for(int x = 0; x < n; x++) {
		for(int y = 0; y < m; y++) {
			cin >> elem;
			downhill[x][y] = elem;
			dp[x][y] = -1;
		}
	}
	
	cout << DFS(0, 0) << '\n';
}