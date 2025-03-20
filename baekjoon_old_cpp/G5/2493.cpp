#include <iostream>
#include <stack>

using namespace std;

int main() {
	ios_base :: sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int n, tower_size;
	cin >> n;
	stack<pair<int, int>> s;
	
	for(int i = 1; i <= n; i++) {
		// 탑 길이를 받아서
		cin >> tower_size;
		// 스택이 비어있지 않을 동안
		while(!s.empty()) {
			// 원래 스택에 있던 탑 길이 비교 후 스택에 있는 길이가 더 크면
			if(s.top().second > tower_size) {
				// 스택에 있는 탑의 순서 출력
				cout << s.top().first << " ";
				break;
			}
			// 스택에 있는 탑 길이가 짧으면 지우기
			s.pop();
		}
		// 그래서 아무것도 없으면 0 출력
		if(s.empty()) cout << "0" << " ";
		// 다음에 오는 것과 비교하기 위해 넣어놓음
		s.push(make_pair(i, tower_size));
	}
}