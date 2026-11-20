#include <iostream>
#include <cstdlib>

using namespace std;

int main() {
    int a, b, c;
    int first_time, second_time;
    int n;

    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> a >> b >> c;
        first_time = a - 1;
        second_time = abs(b - c) + c - 1;

        if(first_time < second_time) cout << "1\n";
        else if(first_time > second_time) cout << "2\n";
        else cout << "3\n";
    }
}