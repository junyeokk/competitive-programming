#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int n, elem, res = 0, idx;
	vector<int> seq;
	
	seq.push_back(-1000000001);
	
	cin >> n;
	
	for(int i = 1; i <= n; i++) {
		cin >> elem;
		// 벡터의 가장 마지막 값보다 크다면 벡터에 push
		if(elem > seq.back()) {
			seq.push_back(elem);
		}
		// 그렇지 않다면 새로 받은 원소(elem)보다 큰 값 중 처음으로 나타나는 위치에 elem을 push
		else {
			idx = lower_bound(seq.begin(), seq.end(), elem) - seq.begin();
			seq[idx] = elem;
		}
	}
	cout << seq.size() - 1 << '\n';
}