#include <iostream>
#include <queue>

using namespace std;

struct cmp {
	bool operator()(int n1, int n2) {
		if(abs(n1) > abs(n2)) return true;
		else if(abs(n1) == abs(n2)) {
			if(n1 > n2) return true;
			else return false;
		}
		return false;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int n, x;
	priority_queue<int, vector<int>, cmp> pq;
	
	cin >> n;
	for(int i = 0; i < n; i++) {
		cin >> x;
		if(x == 0) {
			if(pq.empty()) cout << "0" << '\n';
			else {
				cout << pq.top() << '\n';
				pq.pop();
			}
		} else {
			pq.push(x);
		}
	}
}