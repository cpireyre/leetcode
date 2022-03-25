from more_itertools import first, last
def divide(n, iterable):
    if n < 1:
        raise ValueError('n must be at least 1')

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

def twoCitySchedCost(costs):
    noflip, flip = divide(2, sorted(costs, key=lambda t: t[0] - t[1]))
    return sum(t[0] for t in noflip) + sum(t[1] for t in flip)
# Runtime: 70 ms, faster than 30.29% of Python3 online submissions for Two City Scheduling.
# Memory Usage: 13.9 MB, less than 45.30% of Python3 online submissions for Two City Scheduling.

# costs = [[10,20],[30,200],[400,50],[30,20]] # 110
# costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]] # 1859
# costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]] # 3086
# costs = [[70,311],[74,927],[732,711],[126,583],[857,118],[97,928],[975,843],[175,221],[284,929],[816,602],[689,863],[721,888]] # 4723
# costs = [(100, 10), (1000, 100)] # 200
# costs = [(1000, 100), (100, 10)] # 200
print(twoCitySchedCost(costs))
