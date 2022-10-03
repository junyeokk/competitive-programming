#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int n, elem, res = 0, flag = 0;
	vector<int> v;
	
	cin >> n;
	
	for(int i = 0; i < n; i++) {
		cin >> elem;
		v.push_back(elem);
	}
	
	sort(v.begin(), v.end());
	
	for(int i = 0; i < n; i++) {
		flag += v[i];
		res += flag;
	}
	
	cout << res << '\n';
}