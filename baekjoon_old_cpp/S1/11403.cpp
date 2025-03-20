#include <iostream>
using namespace std;

const int MAX = 101;
int n, elem;
int graph[MAX][MAX];

int main() {
	cin >> n;
	
	for(int i = 1; i <= n; i++) {
		for(int j = 1; j <= n; j++) {
			cin >> elem;
			graph[i][j] = elem;
		}
	}
	
	for(int k = 1; k <= n; k++) {
		for(int a = 1; a <= n; a++) {
			for(int b = 1; b <= n; b++) {
				if(graph[a][k] && graph[k][b]) {
					graph[a][b] = 1;
				}
			}
		}
	}
	
	for(int i = 1; i <= n; i++) {
		for(int j = 1; j <= n; j++) {
			cout << graph[i][j] << " ";
		}
		cout << '\n';
	}
}