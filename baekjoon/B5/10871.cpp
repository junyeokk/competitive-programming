#include <iostream>

using namespace std;

int main() {
	int n, x, cmp;
	
	cin >> n >> x;
	
	for(int i = 1; i <= n; i++) {
		cin >> cmp;
		if(cmp < x) {
			cout << cmp << " ";
		}
	}
}