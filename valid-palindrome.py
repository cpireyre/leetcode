def isPalindrome(s):
    s = list(c for c in s.lower() if c.isalnum())
    return all(a == b for a, b in zip(s, reversed(s)))
# Runtime: 87 ms, faster than 24.87% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 15.2 MB, less than 29.32% of Python3 online submissions for Valid Palindrome.

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
s = "race a car"
print(isPalindrome(s))
s = " "
print(isPalindrome(s))
s = "0P"
print(isPalindrome(s))
