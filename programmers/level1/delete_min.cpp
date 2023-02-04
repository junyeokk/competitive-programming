#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    int min_index = min_element(arr.begin(), arr.end()) - arr.begin();
    arr.erase(arr.begin() + min_index);
    if(arr.size() != 0) {
        return arr;
    }
    return { -1 };
}