'''
The squareOfSums of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the squareOfSums of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the squareOfSums of the squares of the first ten natural numbers and the square of the squareOfSums is
3025 - 385 = 2640
Find the difference between the squareOfSums of the squares of the first one hundred natural numbers and the square of the squareOfSums.
'''
numbers = range(1,101)
squareOfSums = 0
sumOfSquares = 0
for n in numbers:
    squareOfSums = squareOfSums + n
    sumOfSquares = sumOfSquares + (n * n)
squareOfSums = squareOfSums * squareOfSums
difference = squareOfSums - sumOfSquares
print(difference)