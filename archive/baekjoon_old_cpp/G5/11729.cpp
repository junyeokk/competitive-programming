#include <bits/stdc++.h>

using namespace std;

void hanoi(int from, int temp, int to, int n)
{
    if (n == 1) {
        cout << from << " " << to << '\n';
    }
    else
    {
        hanoi(from, to, temp, n - 1);
        cout << from << " " << to << '\n';
        hanoi(temp, from, to, n - 1);
    }
}

void hanoi_cnt(int n)
{
    int num = 1;
    while (--n) {
        num = num * 2 + 1;
    }
    cout << num << '\n';
}

int main()
{
    int n;
    cin >> n;
    hanoi_cnt(n);
    hanoi(1, 2, 3, n);
}