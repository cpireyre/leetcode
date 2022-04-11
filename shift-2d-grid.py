from itertools import chain, cycle, islice


def shiftGrid(grid, k):
    def divide(n, iterable):
        try:
            iterable[:0]
        except TypeError:
            seq = tuple(iterable)
        else:
            seq = iterable

        q, r = divmod(len(seq), n)

        ret = []
        stop = 0
        for i in range(1, n + 1):
            start = stop
            stop += q + 1 if i <= r else q
            ret.append(iter(seq[start:stop]))

        return ret

    H, W = len(grid), len(grid[0])
    total = H * W
    shift = (total - k) % total
    return [
        list(_)
        for _ in divide(
            H, islice(cycle(chain.from_iterable(grid)), shift, shift + total)
        )
    ]
# Runtime: 236 ms, faster than 50.69% of Python3 online submissions for Shift 2D Grid.
# Memory Usage: 14.6 MB, less than 13.09% of Python3 online submissions for Shift 2D Grid.


grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
k = 4
print(shiftGrid(grid, k))
