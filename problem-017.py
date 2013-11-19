problem = """
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

init = ',one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(',')
numLetters = {}
for num in range(0, len(init)):
    numLetters[num] = len(init[num])
numLetters.update({
        20 : len('twenty'),
        30 : len('thirty'),
        40 : len('forty'),
        50 : len('fifty'),
        60 : len('sixty'),
        70 : len('seventy'),
        80 : len('eighty'),
        90 : len('ninety'),
        100 : len('hundred'),
        1000 : len('thousand')
    })
numLetters[100] = len('hundred')
numLetters[1000] = len('thousand')

total = 0
for i in range(0, 100):
    letters = 0
    n = i
    tens = n / 10
    if tens > 1:
        letters += numLetters[tens*10] + numLetters[n%10]
    else:
        letters += numLetters[n]
        
    numLetters[i] = letters
    total += letters

for i in range(100, 1000):
    letters = 0
    n = i
    hundreds = n / 100
    letters += numLetters[hundreds] + len('hundred')
    n %= 100

    if n != 0:
        letters += len('and')
        letters += numLetters[n]

    numLetters[i] = letters
    total += letters

total += numLetters[1] + numLetters[1000]

print total
