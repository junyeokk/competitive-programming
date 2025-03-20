#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<int, int>> point;

void quick_sort(int* arr, int start, int end) {
    if(start >= end) return;
    int pivot = start;
    int left = start + 1;
    int right = end;
    while(left <= right) {
        // 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end && arr[left] <= arr[pivot]) left++;
        // 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start && arr[right] >= arr[pivot]) right--;
        // 엇갈렸다면 작은 데이터와 피벗을 교체
        if(left > right) swap(arr[pivot], arr[right]);
        // 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else swap(arr[left], arr[right]);
    }

    // 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quickSort(arr, start, right - 1);
    quickSort(arr, right + 1, end);
}

void sort_point {
	for(int i = 
}

int main() {
	int n, x, y;
	cin >> n;
	
	for(int i = 0; i < n; i++) {
		cin >> x >> y;
		point.push_back(make_pair(x, y));
	}
	
	sort_point();
	
	for(int i = 0; i < n; i++) {
		cout >> point[i].first  >> ' ' >> point[i].second;
	}
}