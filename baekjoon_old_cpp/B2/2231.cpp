#include <iostream>

using namespace std;

int main() {
	int n, idx = 0;
	int part[6] = { 0 };
	cin >> n;
	
	for(int i = n - 54; i < n; i++) {
		int part_cnt = 0;
		int i_temp = i;
		while(i_temp != 0) {
			part_cnt = part_cnt + i_temp % 10;
			i_temp /= 10;
		}
		if((i + part_cnt) == n) {
			cout << i << '\n';
			return 0;
		}
	}
	cout << "0" << '\n';
}