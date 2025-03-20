#include <iostream>

using namespace std;

int main() {
	const int MAX = 501;
	int n, elem, max_sum = -1;
	int tri[MAX][MAX];

	cin >> n;
	
	cin >> tri[1][1];
	
	for(int i = 2; i <= n; i++) {
		for(int j = 1; j <= i; j++) {
			cin >> elem;
			tri[i][j] = max(tri[i - 1][j - 1], tri[i - 1][j]) + elem;
		}
	}
	
	for(int i = 1; i <= n; i++) {
		if(max_sum < tri[n][i]) {
			max_sum = tri[n][i];
		}
	}
	
	cout << max_sum << '\n';
}