#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX = 26;
vector<int> danji_cnt;
queue<pair<int, int>> q;
int map[MAX][MAX] = { 0 };
bool visited[MAX][MAX];
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
int n, danji = 0;

void BFS(int x, int y) {
	int danji_cnt_each = 0;
	q.push(make_pair(x, y));
	visited[x][y] = true;
	danji_cnt_each++;
	while(!q.empty()) {
		int cur_x = q.front().first;
		int cur_y = q.front().second;
		
		q.pop();
		
		for(int i = 0; i < 4; i++) {
			int nx = cur_x + dx[i];
			int ny = cur_y + dy[i];
			
			if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
			if(map[nx][ny] == 1 && !visited[nx][ny]) {
				visited[nx][ny] = true;
				q.push(make_pair(nx, ny));
				danji_cnt_each++;
			}
		}
	}
	if(danji_cnt_each != 0) {
		danji++;
		danji_cnt.push_back(danji_cnt_each);
	}
}

int main() {
	string s;
	cin >> n;
	
	for(int i = 0; i < n; i++) {
		cin >> s;
		for(int j = 0; j < n; j++) {
			map[i][j] = s[j] - '0';
		}
	}
	
	// 지도에 있는 모든 곳에 BFS 탐색
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < n; j++) {
			if(map[i][j] && !visited[i][j]) {
				BFS(i, j);
			}
		}
	}
	
	sort(danji_cnt.begin(), danji_cnt.end());
	
	cout << danji << '\n';
	for(int i = 0; i < danji; i++) {
		cout << danji_cnt[i] << '\n';
	}
}