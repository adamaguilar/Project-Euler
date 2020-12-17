'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
import math
prime = [2]

def isPrime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

number = 3

while number <= 2000000:
    if isPrime(number) == True:
        prime.append(number)
    number = number + 2

print(sum(prime))