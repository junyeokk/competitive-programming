#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string my_string) {
    vector<char> aeiou = {'a', 'e', 'i', 'o', 'u'};
    
    for (auto i : aeiou) {
        for(int j = 0; j < my_string.size(); j++) {
            while(my_string[j] == i) {
                my_string.erase(my_string.begin() + j);
            }
        }
    }
    return my_string;
}