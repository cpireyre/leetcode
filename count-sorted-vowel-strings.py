from itertools import combinations_with_replacement
def countVowelStrings(n):
    return len([_ for _ in combinations_with_replacement("aeiou", n)])
# Runtime: 1407 ms, faster than 13.47% of Python3 online submissions for Count Sorted Vowel Strings.
# Memory Usage: 161.2 MB, less than 5.08% of Python3 online submissions for Count Sorted Vowel Strings.


print(countVowelStrings(1)) # 5
print(countVowelStrings(2)) # 15
print(countVowelStrings(33)) # 66045
print(countVowelStrings(50)) 
