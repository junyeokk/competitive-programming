#include <iostream>
#include <queue>

using namespace std;

int main() {
	int test_case, docu_cnt, docu_rank, docu_importance, count;
	cin >> test_case;
	
	for(int i = 0; i < test_case; i++) {
		count = 0;
		cin >> docu_cnt >> docu_rank;
		
		// // 큐랑 우선순위 큐 초기화 (중요)
		queue<pair<int, int>> q; 
		priority_queue<int, vector<int>, less<int>> pq;
		
		for(int j = 0; j < docu_cnt; j++) {
			cin >> docu_importance;
			q.push({ j, docu_importance }); // 인덱스 값과 중요도를 같이 넣음
			pq.push(docu_importance);
		}
		
		while(!q.empty()) {
			int index = q.front().first;
			int value = q.front().second;
			q.pop();
		
			if(pq.top() == value) { // 우선순위가 높은 것 먼저 찾음
				pq.pop(); // 찾으면 pop 한 다음에
				count++; // 몇 번째로 뽑혔는지 알 수 있도록 count 올림
				if(index == docu_rank) { // 지금 보고 있는 숫자가 내가 알고 싶었던 그 숫자가 맞는지 검사하고 맞으면 count 출력
					cout << count << '\n';
					break;
				}
			}
			else q.push({ index, value }); // 아니면 다시 q에 넣기
		}
	}
}