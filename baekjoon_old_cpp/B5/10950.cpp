#include <iostream>

using namespace std;

int main() {
	int t; // test case
	int a, b;
	
	cin >> t;
	
	for(int i = 1; i <= t; i++) {
		cin >> a >> b;
		cout << a + b << '\n';
	}
}