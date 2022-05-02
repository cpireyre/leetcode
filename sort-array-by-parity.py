def sortArrayByParity(nums):
   return [e for e in nums if not e % 2] + [o for o in nums if o % 2]
# Runtime: 88 ms, faster than 72.64% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 14.6 MB, less than 63.70% of Python3 online submissions for Sort Array By Parity.
