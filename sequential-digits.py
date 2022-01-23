from math import log10, ceil
#from sys import argv

def sequentialDigitsOfLength(length):

    acc = 0
    inc = 0
    for i in range(1, length + 1):
        acc *= 10 
        acc += i
        inc *= 10
        inc += 1

    digits = range(acc, 10**length, inc)
    return list(digits)[0:(10-length)]

def sequentialDigitsUpTo(n):
    length = ceil(log10(n))
    nums = []
    for d in range(2, length + 1):
        nums += sequentialDigitsOfLength(d)
    return [k for k in nums if k <= n]

#n = int(argv[1])
#print(sequentialDigitsUpTo(n))
