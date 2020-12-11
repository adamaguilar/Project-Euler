#include <iostream>
using namespace std;

int main()
{
    long long int number = 600851475143, check;
    for(check = 3; check < number; check += 2)
    {
        while(number % check == 0)
            number /= check;
    }
    cout << check;
}