//
// Created by Junhyeok CHAE on 2022/08/24.
//
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> card;

int binary_search(int n) {
    int low = 0;
    int high = card.size() - 1;

    while(low <= high) {
        int mid = (low + high) / 2;
        if(card[mid] == n) {
            return 1;
        } else if (card[mid] < n) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return 0;
}

int main() {
    // N: 상근이가 가지고 있는 숫자 카드의 개수, M: 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 카드의 개수
    int N, M;
    int number_card;
    int has_card;
    vector<int> check;
    vector<int> result;

    cin >> N;
    for(int i = 0; i < N; i++) {
        cin >> number_card;
        card.push_back(number_card);
    }

    sort(card.begin(), card.end());

    cin >> M;
    for(int i = 0; i < M; i++) {
        cin >> has_card;
        check.push_back(has_card);
    }

    for(int i : check) {
        result.push_back(binary_search(i));
    }

    for(int i : result) {
        cout << i << " ";
    }
}