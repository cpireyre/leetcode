class MyHashSet:

    def __init__(self):
        self.mem = [False for _ in range(10**6 + 2)]

    def add(self, key: int) -> None:
        self.mem[key] = True

    def remove(self, key: int) -> None:
        self.mem[key] = False

    def contains(self, key: int) -> bool:
        return self.mem[key]
# Runtime: 1074 ms, faster than 24.80% of Python3 online submissions for Design HashSet.
# Memory Usage: 41.3 MB, less than 5.31% of Python3 online submissions for Design HashSet.
