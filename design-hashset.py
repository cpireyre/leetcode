class MyHashSet:

    def __init__(self):
        self.primes = list(reversed([
            53,
            97,
            193,
            389,
            769,
            1543,
            3079,
            6151,
            12289,
            24593,
            49157,
            98317,
            196613,
            ]))
        self.size = self.primes.pop()
        self.mem = [None for _ in range(self.size + 1)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            while self.mem[key % self.size] != None:
                self.rehash()
            self.mem[key % self.size] = key

    def rehash(self):
        vals = [v for v in self.mem if v]
        self.size = self.primes.pop()
        self.mem = [None for _ in range(self.size + 1)]
        for v in vals:
            self.add(v)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.mem[key % self.size] = None

    def contains(self, key: int) -> bool:
        return self.mem[key % self.size] == key


# Runtime: 312 ms, faster than 48.75% of Python3 online submissions for Design HashSet.
# Memory Usage: 21.4 MB, less than 21.37% of Python3 online submissions for Design HashSet.
