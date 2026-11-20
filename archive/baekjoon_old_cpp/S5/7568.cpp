#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<pair<pair<int, int>, int>> dungchi;

void print() {
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < n; j++) {
			if(i == j) continue;
			else if(dungchi[i].first.first < dungchi[j].first.first && dungchi[i].first.second < dungchi[j].first.second) dungchi[i].second++;
		}
	}
	for(int i = 0; i < n; i++) {
		cout << dungchi[i].second << ' ';
	}
}

int main() {
	int x, y;
	cin >> n;
	
	for(int i = 1; i <= n; i++) {
		cin >> x >> y;
		dungchi.push_back(make_pair(make_pair(x, y), 1));
	}
	
	print();
}