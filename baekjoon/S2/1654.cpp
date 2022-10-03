#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int k, need_wire;
long long res;

long long binary_search(vector<long long>& wire, long long low, long long high) {
	long long mid = (low + high) / 2;
	long long cut_wire_cnt = 0;
	
	if(low > high) return res;
	
	for(auto idx = 0; idx < wire.size(); idx++) {
		if(wire[idx] - mid < 0) break;
        else if(mid == 0) cut_wire_cnt += wire[idx];
		else cut_wire_cnt += wire[idx] / mid;
	}
	
	if(cut_wire_cnt >= need_wire) { // 만약 자른 랜선의 개수가 필요한 랜선의 개수보다 크거나 같다면
		res = mid > res ? mid : res; // 랜선의 최대 길이를 알고 싶으므로 최대 길이가 나올 수 있도록 res를 갱신함
	}
	
	if(need_wire > cut_wire_cnt) {
		binary_search(wire, low, mid - 1);
	} else {
		binary_search(wire, mid + 1, high);
	}
	
	return res;
}

int main() {
	long long elem, MAX;
	vector<long long> wire;
	
	cin >> k >> need_wire;
	
	for(int i = 0; i < k; i++) {
		cin >> elem;
		wire.push_back(elem);
	}
	
	sort(wire.begin(), wire.end(), greater<int>());
	
	MAX = wire[0];
	
	cout << binary_search(wire, 0, MAX) << '\n';
}