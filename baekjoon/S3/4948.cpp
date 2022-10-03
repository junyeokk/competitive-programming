#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

const int MAX = 123457 * 2;

bool check[MAX];

void filter() {
	check[1] = true;
	
	for(int i = 2; i <= sqrt(MAX); i++) {
		if(check[i]) continue;
		for(int j = i + i; j <= MAX; j += i) {
			check[j] = true;
		}
	}
}

int count_sieve(int n) {
	int cnt = 0;
	
	for(int i = n + 1; i <= 2 * n; i++) {
		if(!check[i]) cnt++;
	}
	
	return cnt;
}

int main() {
	int n;
	
	filter();
	
	while(1) {
		cin >> n;
		if (n == 0) return 0;
		cout << count_sieve(n) << '\n';
	}
}