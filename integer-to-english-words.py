from sys import argv

numerals = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        10**2: "Hundred",
        10**3: "Thousand",
        10**6: "Million",
        10**9: "Billion"}

# Laborious version below:

## Assumes num < 1000
#def numAnalysis(num):
#
#    hundreds = num // 10**2
#    tens = (num % 10**2) // 10
#    units = num % 10
#
#    ret = []
#    if hundreds:
#        ret.append(hundreds)
#        ret.append(100)
#    if 1 <= tens < 2:
#        ret.append(num % 10**2)
#        return ret
#    elif tens >= 2:
#        ret.append(tens * 10)
#    if units:
#        ret.append(units)
#    
#    return ret
#
#def num2String(lnum):
#    return " ".join(map(lambda n: numerals[n], lnum))
#
## How many billions? How many millions? How many thousands?
#def numberToWords(num):
#
#    if num <= 20:
#        return numerals[num]
#
#    ret = []
#    b = num // 10**9
#    if b:
#        ret += (numAnalysis(b))
#        ret += [10**9]
#    m = (num % 10**9) // 10**6
#    if m:
#        ret += (numAnalysis(m))
#        ret += [10**6]
#    k = (num % 10**6) // 10**3
#    if k:
#        ret += numAnalysis(k)
#        ret += [10**3]
#    rest = num % 10**3
#    if rest:
#        ret += (numAnalysis(rest))
#    print(ret)
#    return(num2String(ret))

# Slick recursive version below:
from math import log10
logsOfInterest = [9, 6, 3, 2, 1]
def numberToWords(num):
    print(num)
    if num <= 99:
        return numerals[10 * (num // 10)] + " " + numerals[num % 10]
    if num <= 20:
        return numerals[num]
    p = log10(num)
    k = max(filter(lambda x: x < p, logsOfInterest))
    return numerals[num // 10**k] + \
            " " + numerals[10**k] + \
            " " + numberToWords(num % 10**k)

def runTests(f, T):
    for t in T:
        print(t[0])
        if f(t[0]) != t[1]:
            print("KO")
            return

testCases = [(123, "One Hundred Twenty Three"),
        (12345, "Twelve Thousand Three Hundred Forty Five"),
        (1234567, "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")]

#runTests(numberToWords, testCases)
print(numberToWords(int(argv[1])))
