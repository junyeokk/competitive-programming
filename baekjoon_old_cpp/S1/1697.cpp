#include <iostream>
#include <queue>

using namespace std;

const int MAX = 100001;
bool visited[MAX];
int subin, bro;

int BFS(int subin, int bro) {
	queue<pair<int, int>> q;
	q.push(make_pair(subin, 0));
	visited[subin] = true;
	
	while(!q.empty()) {
		int place_s = q.front().first;
		int cnt = q.front().second;
		
		q.pop();
		
		if(place_s == bro) return cnt;
		if(place_s + 1 < MAX && !visited[place_s + 1]) {
			q.push(make_pair(place_s + 1, cnt + 1));
			visited[place_s + 1] = true;
		}
		if(place_s - 1 >= 0 && !visited[place_s - 1]) {
			q.push(make_pair(place_s - 1, cnt + 1));
			visited[place_s - 1] = true;
		}
		if(place_s * 2 < MAX && !visited[place_s * 2]) {
			q.push(make_pair(place_s * 2, cnt + 1));
			visited[place_s * 2] = true;
		}
	}
	
	return 0;
}

int main() {
	cin >> subin >> bro;

	cout << BFS(subin, bro) << '\n';
}