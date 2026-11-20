#include <iostream>
#include <vector>

using namespace std;

int main() {
    int q, n;
    string s;
    vector<char> decode_s;
    cin >> q;

    for(int i = 0; i < q; i++) {
        cin >> n;
        cin >> s;
        for(int j = s.size() - 1; j >= 0; j--) {
            if(s[j] == '0') {
                int temp = (s[j - 2] - 48) * 10 + (s[j - 1] - 48);
                decode_s.push_back(temp + 96);
                j -= 2;
            } else {
                decode_s.push_back(s[j] + 48);
            }
        }
        for(auto j = decode_s.rbegin(); j != decode_s.rend(); j++) {
            cout << *j << "";
        }
        decode_s.clear();
        cout << '\n';
    }
}