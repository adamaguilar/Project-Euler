'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''
prime = list()

def isPrime(number):
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False
    return True

number = 2

while len(prime) != 10001:
    if isPrime(number) == True:
        prime.append(number)
    number = number + 1

print(prime[-1])