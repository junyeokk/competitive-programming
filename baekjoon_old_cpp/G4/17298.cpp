#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
	int n, elem;
	vector<int> v_elem;
	stack<int> s;
	
	cin >> n;
	
	// 각 원소들을 벡터에 저장
	for(int i = 0; i < n; i++) {
		cin >> elem;
		v_elem.push_back(elem);
	}
	
	// 정답을 넣을 벡터 생성, -1로 초기화
	vector<int> res(v_elem.size(), -1);
	
	for(int i = 0; i < n; i++) {
		// 스택이 비어있지 않아야 함 + 스택에 있는 값을 인덱스로 하는 원소 값이 벡터 안에 있는 값보다 작다면 그 값은 '오큰수'이므로 스택에 있는 값을 인덱스로 하는 원소 값의 res 벡터를 바꿔줌
		while(!s.empty() && v_elem[s.top()] < v_elem[i]) {
			res[s.top()] = v_elem[i];
			s.pop();
		}
		// 모든 값의 오큰수를 찾아야 하기 때문에 비교를 했다면 스택에 들어가야 함 
		s.push(i);
	}
	
	for(int i = 0 ; i < n; i++) {
		cout << res[i] << " ";
	}
}