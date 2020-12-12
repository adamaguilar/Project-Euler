'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
numbers = list(range(1,20))
def divisible(number):
    for n in numbers:
        if number % n != 0:
            return False
        if n == numbers[-1]:
            return True

number = 2
while not (divisible(number)):
    number = number + 2
print (number)