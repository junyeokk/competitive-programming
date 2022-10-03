#include <iostream>
#include <stack>

using namespace std;

int main() {
	int n, call_n, sum = 0;
	cin >> n;
	stack<int> books;
	
	for(int i = 1; i <= n; i++) {
		cin >> call_n;
		if(call_n) {
			books.push(call_n);
		} else {
			books.pop();
		}
	}
	
	while(books.size()) {
		sum += books.top();
		books.pop();
	}
	
	cout << sum << '\n';
}