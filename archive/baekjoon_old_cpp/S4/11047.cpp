#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int n, k, elem, cnt = 0;
	vector<int> v;
	
	cin >> n >> k;
	for(int i = 1; i <= n; i++) {
		cin >> elem;
		v.push_back(elem);
	}
	
	sort(v.begin(), v.end(), greater<int>());
	
	// k원이 0원이 될 때까지 필요한 동전의 개수를 count
	while(k > 0) {
		for(int i = 0; i < n; i++) {
			if(k / v[i] != 0) {
				k -= v[i];
				cnt++;
				break;
			}
		}
	}
	
	cout << cnt << '\n';
}