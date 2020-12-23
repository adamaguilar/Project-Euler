'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
'''
number = 2 ** 1000
sum = 0
while number >= 1:
    sum = sum + (number % 10)
    number = number // 10
print(sum)