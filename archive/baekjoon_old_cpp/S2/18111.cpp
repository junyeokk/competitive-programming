#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main() {
	const int MIN = -1, MAX = INT_MAX;
	int n, m, inventory, elem, time_flatten;
	int min = MAX, max = MIN;
	int res_time = MAX, res_height = -1;
	vector<vector<int>> land;
	cin >> n >> m >> inventory;
	
	// 벡터 초기화
	for(int i = 0; i < n; i++) {
		land.push_back(vector<int>());
		for(int j = 0; j < m; j++) {
			cin >> elem;
			if(elem < min) min = elem;
			if(elem > max) max = elem;
			land[i].push_back(elem);
		}
	}
	
	for(int i = min; i <= max; i++) {
		int inven_temp = inventory;
		time_flatten = 0;
		for(int j = 0; j < n; j++) {
			for(int k = 0; k < m; k++) {
				if(land[j][k] > i) {
					inven_temp = inven_temp + (land[j][k] - i);
					time_flatten += 2 * (land[j][k] - i);
				} else if(land[j][k] < i) {
					inven_temp = inven_temp - (i - land[j][k]);
					time_flatten += 1 * (i - land[j][k]);
				}
			}
		}
		
		if(inven_temp >= 0) {
			if(res_time > time_flatten) {
				res_time = time_flatten;
				res_height = i;
			} else if(res_time == time_flatten) {
				if(res_height < i) {
					res_height = i;
				}
			}
		}
	}
	
	cout << res_time << " " << res_height << '\n';
}