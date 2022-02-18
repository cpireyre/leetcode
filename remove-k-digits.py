def removeKdigits(num, k):
    if len(num) == k: return "0"
    res = []
    for n in num:
        while res and k and n < res[-1]:
            res.pop()
            k -= 1
        res.append(n)
    return str(int("".join(res[0:len(res)-k])))
# Runtime: 47 ms, faster than 70.05% of Python3 online submissions for Remove K Digits.
# Memory Usage: 14.2 MB, less than 67.26% of Python3 online submissions for Remove K Digits.

def bruteforce(num, k):
        return min((reduce(lambda a,b: 10*int(a)+int(b), c)) for c in combinations(num, len(num)-k))

# print(removeKdigits("1231", 1))
# print(bruteforce("1231", 1))
# print(removeKdigits("237293", 1))
# print(bruteforce("237293", 1))
# print(bruteforce("946396", 4))
# print(removeKdigits("943696", 4))
print(removeKdigits("10", 2))

# from numpy.random import randint
# for _ in range(10000):
#     num = str(randint(1, 10e5))
#     k = randint(1, len(num))
#     b = str(bruteforce(num, k))
#     m = removeKdigits(num, k)
#     if b != m:
#         print("(%s, %d): %s == %s" % (num, k, m, b))
