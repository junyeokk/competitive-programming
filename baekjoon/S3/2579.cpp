#include <iostream>
#define MAX 301

using namespace std;

int main() {
	int n, temp;
	int stair[MAX];
	int max_score[MAX];
	cin >> n;
	
	for(int i = 1; i <= n; i++) {
		cin >> temp;
		stair[i] = temp;
	}
	
	max_score[0] = 0;
	max_score[1] = stair[1];
	max_score[2] = stair[1] + stair[2];
	
	for(int i = 3; i <= MAX; i++) {
		max_score[i] = max(max_score[i - 2] + stair[i], max_score[i - 3] + stair[i - 1] + stair[i]);
	}
	
	cout << max_score[n] << '\n';
}