#include <iostream>
#include <deque>

using namespace std;

int main() {
	bool is_head_left = true, can_print = true;
	int test_case, poss_n = 0, idk;
	
	string arr, temp, comb;
	
	deque<int> dq;
	cin >> test_case;
	
	for(int t = 1; t <= test_case; t++) {
		is_head_left = true;
		can_print = true;
		cin >> comb;
		cin >> idk;	
		cin >> arr;
		// 배열로 받은 값을 숫자만 빼내서 덱에 저장하기
		for(int i = 0; i < arr.length(); i++) {
			if(arr[i] == '[') continue;
			else if('0' <= arr[i] && arr[i] <= '9') {
				temp += arr[i];
			}
			else if(arr[i] == ',' || arr[i] == ']') {
				if(!temp.empty()) {
					dq.push_back(stoi(temp)); // string to int
					temp.clear();
				}
			}
		}
		
		for(int i = 0; i < comb.length(); i++) {
			if(comb[i] == 'R') {
				is_head_left = !is_head_left;
			} else if (comb[i] == 'D' && !dq.empty()) {
				if(is_head_left) {
					dq.pop_front();
				} else {
					dq.pop_back();
				}
			} else {
				can_print = false;
				cout << "error" << '\n';
				break;
			}
		}
		
		if(can_print && is_head_left) {
			cout << "[";
			while(!dq.empty()) {
				cout << dq.front();
				dq.pop_front();
				if(!dq.empty()) cout << ",";
			}
			cout << "]\n";
		}
		else if(can_print && !is_head_left) {
			cout << "[";
			while(!dq.empty()) {
				cout << dq.back();
				dq.pop_back();
				if(!dq.empty()) cout << ",";
			}
			cout << "]\n";
		}
	}
}




