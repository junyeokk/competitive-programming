#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int n, sum = 0, visit[8001], max_mode = 0, max_idx = 0, max_n = -4000, min_n = 4000;
vector<int> statistics;

int mode() {
	int mode_f;
	for(int i = 0; i < statistics.size(); i++) {
		visit[statistics[i] + 4000]++;
		max_n = max(max_n, statistics[i]);
		min_n = min(min_n, statistics[i]);
	}
	for(int i = 0; i < 8001; i++) {
		if(visit[i] > max_mode) {
			max_mode = visit[i];
			max_idx = i;
			mode_f = i - 4000;
		}
	}
	for(int i = 0; i < 8001; i++) {
		if((visit[i] == max_mode) && max_idx < i) {
			mode_f = i - 4000;
			break;
		}
	}
	return mode_f;
}

void print() {
	cout << round(sum / (double)n) << '\n';
	sort(statistics.begin(), statistics.end());	
	cout << statistics[round(statistics.size() / 2)] << '\n';
	cout << mode() << '\n';
	cout << max_n - min_n << '\n';
}

int main() {
	int elem;
	cin >> n;
	
	for(int i = 0; i < n; i++) {
		cin >> elem;
		sum += elem;
		statistics.push_back(elem);
	}
	
	print();
}