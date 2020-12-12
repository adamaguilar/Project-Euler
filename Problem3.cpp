/*
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*/
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
