#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int n;
	char c;
	long long pow_j = 1, hash = 0;
	
	cin >> n;
	
	for(int i = 0; i < n; i++) {
		cin >> c;
		hash = hash + ((c - 'a' + 1) * pow_j) % 1234567891;
		pow_j = pow_j * 31 % 1234567891;
	}
	
	cout << hash % 1234567891 << '\n';
}