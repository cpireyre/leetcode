from functools import reduce


def summaryRanges(ns):
    if not ns:
        return ns

    def consecutives(ns):
        def acc(a, b):
            if a[-1][-1] == b - 1:
                a[-1].append(b)
            else:
                a.append([b])
            return a

        return reduce(acc, ns[1:], [[ns[0]]])

    def interval(ns):
        return (ns[0], ns[-1])

    def show(a, b):
        return "%d->%d" % (a, b) if a != b else str(a)

    return [show(*interval(xs)) for xs in consecutives(ns)]


# Runtime: 35 ms, faster than 69.76% of Python3 online submissions for Summary Ranges.
# Memory Usage: 13.8 MB, less than 88.25% of Python3 online submissions for Summary Ranges.

ns = [0, 1, 2, 4, 5, 7]
print(summaryRanges(ns))
ns = []
print(summaryRanges(ns))
ns = [1]
print(summaryRanges(ns))
