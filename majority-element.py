# from collections import Counter
# def majorityElement(ns):
#     return Counter(ns).most_common()[0][0]
# Runtime: 246 ms, faster than 42.16% of Python3 online submissions for Majority Element.
# Memory Usage: 15.5 MB, less than 43.74% of Python3 online submissions for Majority Element.

# Recursive Boyer–Moore voting
# def majorityElement(ns):
#     def boyerMooreVoting(ns, x=None, counter=0):
#         if not ns:
#             return x
#         if not counter:
#             x = ns[0]
#             counter += 1
#         elif ns[0] == x:
#             counter += 1
#         else:
#             counter -= 1
#         return boyerMooreVoting(ns[1:], x, counter)
#     return boyerMooreVoting(ns)
# Memory limit exceeded, but it's lit

# Normie–Moore voting
def majorityElement(ns):
    l, x, counter = len(ns), 0, 0
    while ns:
        n = ns.pop()
        l -= 1
        if not counter:
            x, counter = n, 1
        else:
            counter += 1 if n == x else -1
        if counter > l:
            return x
    return x
# Runtime: 180 ms, faster than 71.08% of Python3 online submissions for Majority Element.
# Memory Usage: 15.4 MB, less than 81.81% of Python3 online submissions for Majority Element.

nums = [3,2,3]
print(majorityElement(nums))
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
