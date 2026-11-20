#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

vector<string> split(string str, char delimiter) {
	vector<string> internal;
	stringstream ss(str);
	string temp;
	
	while(getline(ss, temp, delimiter)) {
		internal.push_back(temp);
	}
	
	return internal;
}

int main() {
	string s;
	int k, d, a;
	
	cin >> s;
	
	vector<string> split_s = split(s, '/');
	
	stringstream temp1(split_s[0]);
	temp1 >> k;
	
	stringstream temp2(split_s[1]);
	temp2 >> d;
	
	stringstream temp3(split_s[2]);
	temp3 >> a;
	
	if(k + a < d || d == 0) cout << "hasu" << '\n';
	else cout << "gosu" << '\n';
}