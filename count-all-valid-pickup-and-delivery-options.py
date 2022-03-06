from math import factorial
# one liner recursive ver to scare the normies
# actually the combinatoics simplify significantly but oh well this works
def countOrders2(n):
    return 1 if n < 2 else (2*n - 1 + (factorial(2*n - 1) // (2 * factorial(2*n - 3)))) * countOrders2(n - 1) % (10**9 + 7)
# Runtime: 128 ms, faster than 24.15% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
# Memory Usage: 14.4 MB, less than 30.68% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
# time: 2.78 real, 6341440 peak memory footprint
