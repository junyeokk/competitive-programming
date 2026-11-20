#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int take_home_len;
long long res;

long long binary_search(vector<long long>& tree, long long low, long long high) {
	long long mid = (low + high) / 2;
	long long cut_tree = 0;
	
	if(low > high) return res;
	
	for(auto idx = 0; idx < tree.size(); idx++) {
		if(tree[idx] - mid < 0) break;
		else cut_tree += tree[idx] - mid;
	}
	
	if(cut_tree >= take_home_len) {
		res = res < mid ? mid : res;
	}
	
	if(cut_tree > take_home_len) {
		return binary_search(tree, mid + 1, high);
	} else {
		return binary_search(tree, low, mid - 1);
	}
}

int main() {
	int n, temp;
	long long MAX;
	vector<long long> tree;
	
	cin >> n >> take_home_len;
	
	for(int i = 0; i < n; i++) {
		cin >> temp;
		tree.push_back(temp);
	}
	
	sort(tree.begin(), tree.end(), greater<int>());
	
	MAX = tree[0];
	
	cout << binary_search(tree, 0, MAX) << '\n';
}