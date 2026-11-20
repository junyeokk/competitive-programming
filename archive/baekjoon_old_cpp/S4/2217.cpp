#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int n, elem, cnt = 1, power_max = -1;
	vector<int> v;
	cin >> n;
	
	for(int i = 0; i < n; i++) {
		cin >> elem;
		v.push_back(elem);
	}
	
	sort(v.begin(), v.end(), greater<int>());
	
	for(int i = 0; i < n; i++) {
		if(power_max < cnt * v[i]) {
			power_max = cnt * v[i];
		}
		cnt++;
	}
	cout << power_max << '\n';
}