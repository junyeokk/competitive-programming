#include <iostream>
#include <vector>

using namespace std;

int main() {
	int m, n, sum = 0;
	vector<int> res;
	
	cin >> m >> n;
	
	for(int i = 1; i <= 100; i++) {
		if( (i * i >= m) && (i * i <= n) ) res.push_back(i * i);
	}
	
	if(!(res.size())) cout << "-1";
	else {
		for(int i = 0; i < res.size(); i++) {
			sum += res[i];
		}
		cout << sum << '\n';
		cout << res.front() << '\n';
	}
}