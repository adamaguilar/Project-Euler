/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int numbers[6];
    vector<int> answers;
    for(int i = 100; i < 1000; i++)
    {
        for(int j = 999; j > 100; j--)
        {
            int product = i * j;
            int number = product;
            for (int k = 5; k >= 0; k--)
            {
                numbers[k] = product % 10;
                product /= 10;
            }
            int a = 0, b = 5;
            while(a < 3)
            {
                if(numbers[a] != numbers[b])
                    break;
                else if(a == 2 && b == 3)
                    answers.push_back(number);
                a++;
                b--;
            }
        }
    }
    sort(answers.begin(), answers.end()); 
    cout << answers.back();
    return 0;
}