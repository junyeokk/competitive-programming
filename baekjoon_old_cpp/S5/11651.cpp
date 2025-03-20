#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<int, int>> point;

bool cmp(const pair<int, int> &x, const pair<int, int> &y) {
	if(x.second != y.second) {
		return x.second < y.second;	
	} else {
		return x.first < y.first;
	}
}

int main() {
	int n, x, y;
	
	cin >> n;
	
	for(int i = 0; i < n; i++) {
		cin >> x >> y;
		point.push_back(make_pair(x, y));
	}
	
	sort(point.begin(), point.end(), cmp);
	
	for(int i = 0; i < point.size(); i++) {
		cout << point[i].first << " " << point[i].second << '\n';
	}
}