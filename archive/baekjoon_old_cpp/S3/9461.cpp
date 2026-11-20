#include <iostream>

using namespace std;

int main() {
	int test_case, n;
	long long arr[101] = {0, 1, 1, 1, 2, 2};
	
	for(int i = 6; i <= 100; i++) {
		arr[i] = arr[i - 1] + arr[i - 5];
	}
	
	cin >> test_case;
	
	for(int i = 1; i <= test_case; i++) {
		cin >> n;
		cout << arr[n] << '\n';
	}
}