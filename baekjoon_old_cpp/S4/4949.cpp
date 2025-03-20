#include <iostream>
#include <stack>

using namespace std;

int main() {
	while(true) {
		stack<char> s;
		string str;
		getline(cin, str);
		
		if(str == ".") {
			break;
		}
		
		bool is_unbalanced = false;
		for(int i = 0; i < str.length(); i++) {
			if(str[i] == '(' || str[i] == '[') {
				s.push(str[i]);	
			} 
			else if(str[i] == ')') {
				if(!s.empty() && s.top() == '(') {
					s.pop();
				} else {
					is_unbalanced = true;
					break;
				}
			}
			else if(str[i] == ']') {
				if(!s.empty() && s.top() == '[') {
					s.pop();
				} else {
					is_unbalanced = true;
					break;
				}
			}
		}
		if(is_unbalanced || !s.empty()) cout << "no" << '\n';
		else cout << "yes" << '\n';
	}
	return 0;
}