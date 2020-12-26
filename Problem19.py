'''
You are given the following information, but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30]
day = 1
count = 0
for year in range(1900, 2001):
    for month in range(0, 12):
        day = day + months[month]
        if year % 4 == 0 and month == 1:
            day = day + 1
        if day % 7 == 0 and year > 1900:
            count = count + 1
print(count)
