#include <iostream>

using namespace std;

int main() {
	int pentagon = 0, flag = 7, n;
	
	cin >> n;
	
	if(n == 1) {
		cout << "5" << '\n';
		return 0;
	}
	
	pentagon += 5;
	
	for(int i = 2; i <= n; i++) {
		pentagon += flag;
		flag += 3;
		pentagon %= 45678;
	}
	
	cout << pentagon << '\n';	
}