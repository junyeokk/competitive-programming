#include <iostream>
#include <queue>

using namespace std;

int main() {
	ios_base :: sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int n, num_q;
	queue<int> q;
	
	cin >> n;
	string str;
	
	for(int i = 0; i < n; i++) {
		cin >> str;
		if(str == "push") {
			cin >> num_q;
			q.push(num_q);
		} else if (str == "pop") {
			if(!q.empty()) {
				cout << q.front() << '\n';
				q.pop();
			} else cout << "-1" << '\n';
		} else if (str == "size") {
			cout << q.size() << '\n';
		} else if (str == "empty") {
			if(q.empty()) cout << "1" << '\n';
			else cout << "0" << '\n';
		} else if (str == "front") {
			if(!q.empty()) cout << q.front() << '\n';
			else cout << "-1" << '\n';
		} else if (str == "back") {
			if(!q.empty()) cout << q.back() << '\n';
			else cout << "-1" << '\n';
		}
	}
}