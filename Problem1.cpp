#include <iostream>
using namespace std;

int main()
{
	int counter = 0;
	int answer = 0;
	int limit = 1000;
	do{
		if(counter % 3 == 0 || counter % 5 == 0)
			answer += counter;
		counter++;
	}while(counter < limit);
	cout << answer << endl;
	return 0;
}
