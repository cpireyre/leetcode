from typing import *

# Runtime: 1154 ms, faster than 54.56% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25 MB, less than 80.69% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Not sure how to make it faster
#def maxProfit(prices: List[int]) -> int:
#    index = prices[0]
#    maxProfit = 0
#    for price in prices[1:]:
#        profit = price - index
#        if profit > maxProfit:
#            maxProfit = profit
#        if price < index:
#            index = price
#    return maxProfit

# Very cool one liner from the Leetcode forum:
from itertools import accumulate
def maxProfit(prices: List[int]) -> int:
    return max(x - y for x, y in zip(prices, list(accumulate(prices, min))))
# Terrible performance but definitely very cool

# Another cool one from Leetcode:
def maxProfit(prices: List[int]) -> int:
    sum_max=0
    current_subarray=0
    returns=[prices[i+1]-prices[i] for i in range(len(prices)-1)]
    for x in returns:
    current_subarray=max(current_subarray+x,x)
    sum_max=max(sum_max,current_subarray)
    return sum_max
# Worse performance profile but it shows how this is isomorphic to
# maximum subarray sum, which is interesting

# List comprehension for memes
#def maxProfit(prices: List[int]) -> int:
#    l = len(prices)
#    return max((prices[y] - prices[x] \
#            for x in range(l) \
#            for y in range(x + 1, l) \
#            if prices[y] > prices[x]), \
#            default=0)
# Time limit exceeded lol



#prices = [7,1,5,3,6,4]
#print(maxProfit(prices))
#prices = [7,6,4,3,1]
#print(maxProfit(prices))
#prices = [10,100,2,100,1]
#print(maxProfit(prices))
#prices = [3]
#print(maxProfit(prices))
prices = [3,2,6,5,0,3]
print(list(accumulate(prices, min)))
print(maxProfit(prices))
