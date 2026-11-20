#include <iostream>

using namespace std;

int main() {
	const int MAX = 1001;
	int n;
	int arr[MAX] = { 0, 1, 3 };
	
	cin >> n;
	
	for(int i = 3; i <= MAX; i++) {
		arr[i] = (arr[i - 1] + 2 * arr[i - 2]) % 10007;
	}
	
	cout << arr[n] << '\n';
}