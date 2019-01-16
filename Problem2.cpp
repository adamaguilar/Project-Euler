#include <iostream>
using namespace std;

int main()
{
	int answer = 0;
	int fibonacci1 = 1;
	int fibonacci2 = 1;
	int temp = 0;
	int limit = 4000000;
	do{
		if(fibonacci1 % 2 == 0)
			answer += fibonacci1;
		temp = fibonacci1;
		fibonacci1 += fibonacci2;
		fibonacci2 = temp;
	}while(fibonacci1 < limit);
	cout << answer << endl;
	return 0;
}
