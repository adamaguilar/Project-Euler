/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
*/
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
