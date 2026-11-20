#include <iostream>
#define MAX 1001

using namespace std;

int main() {
	int n, elem, seq[MAX], dp[MAX], res = 0;
	
	cin >> n;
	
	for(int i = 1; i <= n; i++) {
		cin >> seq[i];
	}
	
	for(int i = 1; i <= n; i++) {
		dp[i] = 1;
		for(int j = 1; j < i; j++) {
			if(seq[j] < seq[i]) {
				dp[i] = max(dp[i], dp[j] + 1);
			}
		}
		res = max(dp[i], res);
	}
	cout << res << '\n';
}