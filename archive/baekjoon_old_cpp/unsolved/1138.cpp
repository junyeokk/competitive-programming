#include <iostream>

using namespace std;

int main() {
	int n, elem, cnt, order = 1;
	int human[11] = { 0 };
	cin >> n;
	
	for(int i = 0; i < n; i++) {
		cnt = 0;
		cin >> elem;
		for(int j = 0; j < n; j++) {
			if(cnt == elem && human[j] == 0) {
				human[j] = order++;
				break;
			}
			if(human[j] == 0) {
				cnt++;	
			}
		}
	}
	
	for(int i = 0; i < n; i++) {
		cout << human[i] << " ";
	}
}