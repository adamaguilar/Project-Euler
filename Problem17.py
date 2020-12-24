'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
words = words + [None] * 980
words[30] = "thirty"
words[40] = "forty"
words[50] = "fifty"
words[60] = "sixty"
words[70] = "seventy"
words[80] = "eighty"
words[90] = "ninety"
for i in range(1, len(words) + 1):
    if i / 10 > 2 and i / 10 < 10 and i % 10 != 0:
        words[i] = words[(i // 10) * 10] + words[i % 10]
    elif i % 100 == 0 and i / 100 < 10:
        words[i] = words[i // 100] + "hundred"
    elif i / 100 >= 1 and i / 100 < 10:
        words[i] = words[(i // 100) * 100] + "and" + words[i - ((i // 100) * 100)]
    elif i / 1000 == 1:
        words[i] = words[i // 1000] + "thousand"
words.pop(0)
print(sum(len(s) for s in words))