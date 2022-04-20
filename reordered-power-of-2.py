from itertools import permutations


def reorderedPowerOf2(n):
    return any(
        p.bit_count() == 1
        for p in map(
            lambda xs: int("".join(xs)),
            filter(lambda xs: xs[0] != "0", permutations(str(n))),
        )
    )
# Runtime: 3151 ms, faster than 9.63% of Python3 online submissions for Reordered Power of 2.
# Memory Usage: 14 MB, less than 19.27% of Python3 online submissions for Reordered Power of 2.


n = 1
print(reorderedPowerOf2(n))
n = 10
print(reorderedPowerOf2(n))
