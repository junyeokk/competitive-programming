#include <iostream>

using namespace std;

int main() {
	int n, cnt = 0;
	cin >> n;
	
	int charge = 1000 - n;
	
	
	while(charge > 0) {
		if(charge / 500 != 0) {
			charge -= 500;
		} else if(charge / 100 != 0) {
			charge -= 100;
		} else if(charge / 50 != 0) {
			charge -= 50;
		} else if(charge / 10 != 0) {
			charge -= 10;
		} else if(charge / 5 != 0) {
			charge -= 5;
		} else if(charge / 1 != 0) {
			charge -= 1;
		}
		cnt++;
	}
	cout << cnt << '\n';
}