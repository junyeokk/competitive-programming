#include <iostream>

using namespace std;

int main() {
	int n;
	int arr[45] = {1, 1, };
	
	cin >> n;
	
	for(int i = 2; i < 45; i++) {
		arr[i] = arr[i - 1] + arr[i - 2];
	}
	
	if(n == 1) cout << "0 1";
	else cout << arr[n - 2] << " " << arr[n - 1];
}