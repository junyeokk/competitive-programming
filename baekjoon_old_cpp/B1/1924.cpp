#include <iostream>

using namespace std;

int main() {
	int m, d, check_day = 0;
	string day[7] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
	
	cin >> m >> d;
	
	for(int i = 1; i < m; i++) {
		switch(i){
			case 1:
			case 3:
			case 5:
			case 7: 
			case 8:
			case 10:
			case 12:
				check_day += 31;
				break;
			case 2:
				check_day += 28;
				break;
			case 4:
			case 6:
			case 9:
			case 11:
				check_day += 30;
				break;
		}
	}
	check_day += d;
	cout << day[check_day % 7];
}