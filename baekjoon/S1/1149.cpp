#include <iostream>

using namespace std;

int main() {
	const int MAX = 1001;
	int n, cost_red, cost_green, cost_blue;
	int house[MAX][3];
	
	house[0][0] = 0, house[0][1] = 0, house[0][2] = 0;
	
	cin >> n;
	
	for(int i = 1; i <= n; i++) {
		cin >> cost_red >> cost_green >> cost_blue;
		// red, green, blue 순으로
		house[i][0] = min(house[i - 1][1], house[i - 1][2]) + cost_red;
		house[i][1] = min(house[i - 1][0], house[i - 1][2]) + cost_green;
		house[i][2] = min(house[i - 1][0], house[i - 1][1]) + cost_blue;
	}
	
	cout << min(min(house[n][0], house[n][1]), house[n][2]) << '\n';
}