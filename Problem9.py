'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math

def Pythagorean(a, b):
    c = (a ** 2) + (b ** 2)
    c = math.sqrt(c)
    return c

a = 1
b = 2
c = Pythagorean(a, b)
target = 1000

while a < target:
    b = a + 1
    while a + b + c <= target:
        c = Pythagorean(a, b)
        if a + b + c == target:
            print(a * b * c)
            break
        else:
            b = b + 1
    a = a + 1
