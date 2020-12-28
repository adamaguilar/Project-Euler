'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
'''
import math

number = 1
sums = {}
amicable = set()

while number < 10000:
    sum = 0
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0 and number != i:
            sum = sum + i
            if number / i != i and number / i != number:
                sum = sum + (number / i)
    if sum != 0:
        sums[number] = int(sum)
    number = number + 1

total = 0

for num in sums:
    if sums[num] in sums and sums[sums[num]] == num and num != sums[num]:
        amicable.add(num)

for num in amicable:
    total = total + num

print(total)